import sys
import time
import ctypes
import keyboard
import pyautogui
import win32api
import win32gui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QThread, Signal, QElapsedTimer
from PySide6.QtGui import QIcon
from ui import Ui_MainWindow
from clicker import MouseController
import os


def make_lparam(x: int, y: int) -> int:
    return (y << 16) | x


class GlobalHotkeyListener(QThread):
    hotkey_signal = Signal()

    def run(self):
        keyboard.add_hotkey('F8', self.hotkey_signal.emit)
        keyboard.wait()


class ClickThread(QThread):
    def __init__(self, repeat, is_repeat, delay, click_inside, click_button,
                 click_type, x, y, hwnd, custom_location):
        super().__init__()

        self.running = False
        self.repeat = repeat
        self.is_repeat = is_repeat
        self.delay = delay
        self.click_inside = click_inside
        self.click_button = click_button
        self.click_type = click_type
        self.x = x
        self.y = y
        self.hwnd = hwnd
        self.custom_location = custom_location
        self.click_count = 1

        # Windows message constants
        self.WM_MESSAGES = {
            "left": (0x0201, 0x0202, 0x0001),
            "right": (0x0204, 0x0205, 0x0002),
            "middle": (0x0207, 0x0208, 0x0010),
        }

    def run(self):
        mouse = MouseController()
        lparam = make_lparam(self.x, self.y) if self.x is not None else None

        down_msg, up_msg, key_flag = self.WM_MESSAGES.get(
            self.click_button, self.WM_MESSAGES["left"]
        )

        def send_click():
            self.click_count += 1
            ctypes.windll.user32.SendMessageW(self.hwnd, down_msg, key_flag, lparam)
            ctypes.windll.user32.SendMessageW(self.hwnd, up_msg, 0, lparam)

        def send_click_custom():
            self.click_count += 1
            mouse.click(self.x, self.y)

        def send_click_current():
            self.click_count += 1
            mouse.click_current_position(button=self.click_button)

        if self.click_inside:
            click_method = send_click
        elif self.custom_location:
            click_method = send_click_custom
        else:
            click_method = send_click_current

        self.running = True
        timer = QElapsedTimer()
        timer.start()

        def should_continue():
            return self.running and (self.click_count <= self.repeat if self.is_repeat else True)

        while should_continue():
            click_method()
            if self.click_type == "double":
                click_method()


            #time.sleep(self.delay / 1000)
            timer.restart()
            while timer.elapsed() < self.delay:
                if not self.running:
                    return
                #self.msleep(10) 

    def stop(self):
        self.running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Shadow Clicker")

        if getattr(sys, 'frozen', False):
            icon_path = os.path.join(sys._MEIPASS, "icon.ico")
        else:
            icon_path = os.path.abspath("icon.ico")
            
        self.setWindowIcon(QIcon(icon_path))
        self.ui.pushButton_setHotkey.setEnabled(False)

        self.click_thread = None
        self.click_count = 0

        self.ui.pushButton_pickLocation.pressed.connect(self.pick_location)
        self.ui.pushButton_start.pressed.connect(self.start_clicker)
        self.ui.pushButton_stop.pressed.connect(self.stop_clicker)

        self.hotkey_listener = GlobalHotkeyListener()
        self.hotkey_listener.hotkey_signal.connect(self.toggle_clicker_via_hotkey)
        self.hotkey_listener.start()

    def toggle_clicker_via_hotkey(self):
        if self.ui.pushButton_start.isEnabled():
            self.start_clicker()
        else:
            self.stop_clicker()

    def start_clicker(self):
        self.ui.pushButton_start.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(True)

        delay = self.get_delay()
        repeat = self.ui.spinBox_repeat.value()
        is_repeat = self.ui.radioButton_repeat.isChecked()
        click_inside = self.ui.radioButton_insideClicker.isChecked()
        click_button = self.ui.comboBox_clickButton.currentText().lower()
        click_type = self.ui.comboBox_clickType.currentText().lower()
        custom_location = self.ui.radioButton_customLocation.isChecked()

        if custom_location or click_inside:
            x = self.ui.spinBox_x.value()
            y = self.ui.spinBox_y.value()
            hwnd = self.ui.spinBox_hwnd.value()
        else:
            x = y = hwnd = None

        self.click_thread = ClickThread(
            repeat, is_repeat, delay, click_inside, click_button,
            click_type, x, y, hwnd, custom_location
        )
        self.click_thread.start()

    def stop_clicker(self):
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(False)

        if self.click_thread:
            self.click_thread.stop()
            self.click_thread.wait()

    def get_window_info(self):
        x, y = win32api.GetCursorPos()
        hwnd = win32gui.WindowFromPoint((x, y))
        if hwnd:
            left, top, _, _ = win32gui.GetWindowRect(hwnd)
            return hwnd, x - left, y - top
        return None, None, None

    def pick_location(self):
        self.ui.pushButton_pickLocation.setDisabled(True)
        self.ui.pushButton_pickLocation.setText("Press CTRL")

        def check_position():
            if keyboard.is_pressed("ctrl"):
                timer.stop()
                self.ui.pushButton_pickLocation.setEnabled(True)
                self.ui.pushButton_pickLocation.setText("Pick location")
                return

            if self.ui.radioButton_normalClicker.isChecked():
                x, y = pyautogui.position()
                self.ui.spinBox_x.setValue(x)
                self.ui.spinBox_y.setValue(y)
            else:
                hwnd, x, y = self.get_window_info()
                self.ui.spinBox_x.setValue(x)
                self.ui.spinBox_y.setValue(y)
                self.ui.spinBox_hwnd.setValue(hwnd)

        timer = QTimer(self)
        timer.timeout.connect(check_position)
        timer.start(10)

    def get_delay(self):
        return (
            self.ui.spinBox_mins.value() * 60000 +
            self.ui.spinBox_secs.value() * 1000 +
            self.ui.spinBox_miliseconds.value()
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
