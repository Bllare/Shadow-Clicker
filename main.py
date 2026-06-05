import sys
import time
import json
import ctypes
import math
import keyboard
import pyautogui
import win32api
import win32gui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, QThread, Signal, QElapsedTimer
from PySide6.QtGui import QIcon
from ui import Ui_MainWindow
from clicker import MouseController
import random
import os


def make_lparam(x: int, y: int) -> int:
    return (y << 16) | x


class GlobalHotkeyListener(QThread):
    hotkey_signal = Signal()
    hotkey_released_signal = Signal()

    def __init__(self, hotkey='F8'):
        super().__init__()
        self.hotkey = hotkey
        self._running = True
        self._kb_hook = None
        self._key_held = False

    def set_hotkey(self, hotkey):
        self._remove_hooks()
        self.hotkey = hotkey
        self._key_held = False
        self._install_hooks()

    def _remove_hooks(self):
        if self._kb_hook:
            keyboard.unhook(self._kb_hook)
            self._kb_hook = None

    def _install_hooks(self):
        hk = self.hotkey.lower()
        def on_kb(e):
            if not self._running:
                return
            if e.name.lower() == hk:
                if e.event_type == 'down' and not self._key_held:
                    self._key_held = True
                    self.hotkey_signal.emit()
                elif e.event_type == 'up' and self._key_held:
                    self._key_held = False
                    self.hotkey_released_signal.emit()
        self._kb_hook = keyboard.hook(on_kb)

    def run(self):
        self._install_hooks()
        while self._running:
            self.msleep(100)

    def stop_listener(self):
        self._running = False
        self._remove_hooks()


class HotkeyCaptureThread(QThread):
    key_captured = Signal(str)

    def run(self):
        captured = [None]
        ready = [False]

        def on_key(e):
            if captured[0] is not None:
                return
            if not ready[0]:
                return
            if e.event_type == 'down':
                key_name = e.name
                if len(key_name) == 1 or key_name.lower() in ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12',
                                                               'insert','delete','home','end','page up','page down',
                                                               'up','down','left','right','space','enter','tab','escape',
                                                               'backspace','caps lock','shift','ctrl','alt']:
                    captured[0] = key_name
                    self.key_captured.emit(key_name)
                    return False

        hook_kb = keyboard.hook(on_key)
        self.msleep(300)
        ready[0] = True

        while captured[0] is None:
            self.msleep(50)
        keyboard.unhook(hook_kb)


def smooth_move_to(from_x, from_y, to_x, to_y, steps=5):
    for i in range(1, steps + 1):
        t = i / steps
        cx = from_x + (to_x - from_x) * t + random.randint(-1, 1)
        cy = from_y + (to_y - from_y) * t + random.randint(-1, 1)
        pyautogui.moveTo(int(cx), int(cy))
        time.sleep(random.uniform(0.002, 0.008))


class ClickThread(QThread):
    def __init__(self, repeat, is_repeat, delay, click_inside, click_button,
                 click_type, x, y, hwnd, custom_location, hold_duration=0,
                 mouse_shake=False, shake_min=0, shake_max=10,
                 random_delay=False, delay_min=0, delay_max=50):
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
        self.hold_duration = hold_duration
        self.mouse_shake = mouse_shake
        self.shake_min = shake_min
        self.shake_max = shake_max
        self.random_delay = random_delay
        self.delay_min = delay_min
        self.delay_max = delay_max
        self.click_count = 1

        self.WM_MESSAGES = {
            "left": (0x0201, 0x0202, 0x0001),
            "right": (0x0204, 0x0205, 0x0002),
            "middle": (0x0207, 0x0208, 0x0010),
        }

    def run(self):
        mouse_ctrl = MouseController()
        lparam = make_lparam(self.x, self.y) if self.x is not None else None

        down_msg, up_msg, key_flag = self.WM_MESSAGES.get(
            self.click_button, self.WM_MESSAGES["left"]
        )

        def make_shake_lparam(sx, sy):
            return make_lparam(self.x + sx, self.y + sy)

        def send_hold():
            self.click_count += 1
            if self.mouse_shake and self.shake_max > 0:
                sx, sy = do_shake()
                slparam = make_shake_lparam(sx, sy)
                ctypes.windll.user32.SendMessageW(self.hwnd, down_msg, key_flag, slparam)
                if self.hold_duration > 0:
                    self.msleep(int(self.hold_duration))
                ctypes.windll.user32.SendMessageW(self.hwnd, up_msg, 0, slparam)
            else:
                ctypes.windll.user32.SendMessageW(self.hwnd, down_msg, key_flag, lparam)
                if self.hold_duration > 0:
                    self.msleep(int(self.hold_duration))
                ctypes.windll.user32.SendMessageW(self.hwnd, up_msg, 0, lparam)

        def send_click():
            self.click_count += 1
            if self.mouse_shake and self.shake_max > 0:
                sx, sy = do_shake()
                slparam = make_shake_lparam(sx, sy)
                ctypes.windll.user32.SendMessageW(self.hwnd, down_msg, key_flag, slparam)
                ctypes.windll.user32.SendMessageW(self.hwnd, up_msg, 0, slparam)
            else:
                ctypes.windll.user32.SendMessageW(self.hwnd, down_msg, key_flag, lparam)
                ctypes.windll.user32.SendMessageW(self.hwnd, up_msg, 0, lparam)

        def send_click_custom():
            self.click_count += 1
            cx, cy = self.x, self.y
            if self.mouse_shake and self.shake_max > 0:
                sx, sy = do_shake()
                cx, cy = self.x + sx, self.y + sy
            if self.hold_duration > 0:
                mouse_ctrl.click(cx, cy, button=self.click_button, hold=True, hold_duration=self.hold_duration)
            else:
                mouse_ctrl.click(cx, cy, button=self.click_button)

        def send_click_current():
            self.click_count += 1
            if self.mouse_shake and self.shake_max > 0:
                ox, oy = pyautogui.position()
                offset = random.randint(self.shake_min, self.shake_max)
                angle = random.uniform(0, 2 * math.pi)
                nx = ox + int(offset * math.cos(angle))
                ny = oy + int(offset * math.sin(angle))
                smooth_move_to(ox, oy, nx, ny, steps=random.randint(3, 6))
                pyautogui.moveTo(ox, oy)
            if self.hold_duration > 0:
                mouse_ctrl.click_current_position(button=self.click_button, hold=True, hold_duration=self.hold_duration)
            else:
                mouse_ctrl.click_current_position(button=self.click_button)

        def do_shake():
            if self.mouse_shake and self.shake_max > 0:
                shake_offset = random.randint(self.shake_min, self.shake_max)
                shake_angle = random.uniform(0, 2 * math.pi)
                return int(shake_offset * math.cos(shake_angle)), int(shake_offset * math.sin(shake_angle))
            return 0, 0

        if self.click_inside:
            click_method = send_hold if self.hold_duration > 0 else send_click
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
                if self.hold_duration > 0:
                    time.sleep(0.05)
                click_method()

            timer.restart()
            current_delay = self.delay
            if self.random_delay and self.delay_max > 0:
                delay_offset = random.randint(self.delay_min, self.delay_max)
                if random.randint(0, 1) == 0:
                    current_delay = max(0, self.delay - delay_offset)
                else:
                    current_delay = self.delay + delay_offset
            while timer.elapsed() < current_delay:
                if not self.running:
                    return

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

        self.click_thread = None
        self.click_count = 0
        self.capturing_hotkey = False
        self.current_hotkey = 'F8'

        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        self.load_config()

        self.ui.pushButton_setHotkey.setEnabled(True)
        self.ui.pushButton_setHotkey.pressed.connect(self.start_hotkey_capture)

        self.ui.pushButton_pickLocation.pressed.connect(self.pick_location)
        self.ui.pushButton_start.pressed.connect(self.start_clicker)
        self.ui.pushButton_stop.pressed.connect(self.stop_clicker)

        self.hotkey_listener = GlobalHotkeyListener(self.current_hotkey)
        self.hotkey_listener.hotkey_signal.connect(self.on_hotkey_pressed)
        self.hotkey_listener.hotkey_released_signal.connect(self.on_hotkey_released)
        self.hotkey_listener.start()

        self.update_hotkey_display()

    def get_config(self):
        return {
            "hotkey": self.current_hotkey,
            "hotkey_mode": "trigger" if self.ui.radioButton_trigger.isChecked() else "toggle",
            "delay_mins": self.ui.spinBox_mins.value(),
            "delay_secs": self.ui.spinBox_secs.value(),
            "delay_ms": self.ui.spinBox_miliseconds.value(),
            "click_button": self.ui.comboBox_clickButton.currentIndex(),
            "click_type": self.ui.comboBox_clickType.currentIndex(),
            "clicker_type": "inside" if self.ui.radioButton_insideClicker.isChecked() else "normal",
            "cursor_pos": "custom" if self.ui.radioButton_customLocation.isChecked() else "current",
            "x": self.ui.spinBox_x.value(),
            "y": self.ui.spinBox_y.value(),
            "hwnd": self.ui.spinBox_hwnd.value(),
            "repeat_enabled": self.ui.radioButton_repeat.isChecked(),
            "repeat_count": self.ui.spinBox_repeat.value(),
            "hold_enabled": self.ui.checkBox_hold.isChecked(),
            "hold_ms": self.ui.spinBox_hold.value(),
            "shake_enabled": self.ui.checkBox_shake.isChecked(),
            "shake_min": self.ui.spinBox_shakeMin.value(),
            "shake_max": self.ui.spinBox_shakeMax.value(),
            "random_delay_enabled": self.ui.checkBox_randomDelay.isChecked(),
            "delay_min": self.ui.spinBox_delayMin.value(),
            "delay_max": self.ui.spinBox_delayMax.value(),
        }

    def apply_config(self, cfg):
        if "hotkey" in cfg:
            self.current_hotkey = cfg["hotkey"]
        if "hotkey_mode" in cfg:
            if cfg["hotkey_mode"] == "trigger":
                self.ui.radioButton_trigger.setChecked(True)
            else:
                self.ui.radioButton_toggle.setChecked(True)
        if "delay_mins" in cfg:
            self.ui.spinBox_mins.setValue(cfg["delay_mins"])
        if "delay_secs" in cfg:
            self.ui.spinBox_secs.setValue(cfg["delay_secs"])
        if "delay_ms" in cfg:
            self.ui.spinBox_miliseconds.setValue(cfg["delay_ms"])
        if "click_button" in cfg:
            self.ui.comboBox_clickButton.setCurrentIndex(cfg["click_button"])
        if "click_type" in cfg:
            self.ui.comboBox_clickType.setCurrentIndex(cfg["click_type"])
        if "clicker_type" in cfg:
            if cfg["clicker_type"] == "inside":
                self.ui.radioButton_insideClicker.setChecked(True)
            else:
                self.ui.radioButton_normalClicker.setChecked(True)
        if "cursor_pos" in cfg:
            if cfg["cursor_pos"] == "custom":
                self.ui.radioButton_customLocation.setChecked(True)
            else:
                self.ui.radioButton_currentLocation.setChecked(True)
        if "x" in cfg:
            self.ui.spinBox_x.setValue(cfg["x"])
        if "y" in cfg:
            self.ui.spinBox_y.setValue(cfg["y"])
        if "hwnd" in cfg:
            self.ui.spinBox_hwnd.setValue(cfg["hwnd"])
        if "repeat_enabled" in cfg:
            self.ui.radioButton_repeat.setChecked(cfg["repeat_enabled"])
        if "repeat_count" in cfg:
            self.ui.spinBox_repeat.setValue(cfg["repeat_count"])
        if "hold_enabled" in cfg:
            self.ui.checkBox_hold.setChecked(cfg["hold_enabled"])
        if "hold_ms" in cfg:
            self.ui.spinBox_hold.setValue(cfg["hold_ms"])
        if "shake_enabled" in cfg:
            self.ui.checkBox_shake.setChecked(cfg["shake_enabled"])
        if "shake_min" in cfg:
            self.ui.spinBox_shakeMin.setValue(cfg["shake_min"])
        if "shake_max" in cfg:
            self.ui.spinBox_shakeMax.setValue(cfg["shake_max"])
        if "random_delay_enabled" in cfg:
            self.ui.checkBox_randomDelay.setChecked(cfg["random_delay_enabled"])
        if "delay_min" in cfg:
            self.ui.spinBox_delayMin.setValue(cfg["delay_min"])
        if "delay_max" in cfg:
            self.ui.spinBox_delayMax.setValue(cfg["delay_max"])

    def save_config(self):
        try:
            cfg = self.get_config()
            with open(self.config_path, "w") as f:
                json.dump(cfg, f, indent=2)
        except Exception:
            pass

    def load_config(self):
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, "r") as f:
                    cfg = json.load(f)
                self.apply_config(cfg)
        except Exception:
            pass

    def closeEvent(self, event):
        self.save_config()
        keyboard.unhook_all()
        if self.hotkey_listener:
            self.hotkey_listener.stop_listener()
            self.hotkey_listener.wait(500)
        if self.click_thread and self.click_thread.running:
            self.click_thread.stop()
            self.click_thread.wait(500)
        event.accept()

    def update_hotkey_display(self):
        self.ui.pushButton_start.setText(f"Start ({self.current_hotkey})")
        self.ui.pushButton_stop.setText(f"Stop ({self.current_hotkey})")
        self.ui.pushButton_setHotkey.setText(f"Set Hotkey ({self.current_hotkey})")

    def start_hotkey_capture(self):
        if self.capturing_hotkey:
            return
        self.capturing_hotkey = True
        self.ui.pushButton_setHotkey.setEnabled(False)
        self.ui.pushButton_setHotkey.setText("Press a key...")

        self.capture_thread = HotkeyCaptureThread()
        self.capture_thread.key_captured.connect(self.set_new_hotkey)
        self.capture_thread.start()

    def set_new_hotkey(self, key):
        self.capturing_hotkey = False
        self.current_hotkey = key.upper()
        self.hotkey_listener.set_hotkey(self.current_hotkey)
        self.update_hotkey_display()
        self.ui.pushButton_setHotkey.setEnabled(True)

    def on_hotkey_pressed(self):
        if self.ui.radioButton_trigger.isChecked():
            if not (self.click_thread and self.click_thread.running):
                self.start_clicker()
        else:
            if self.ui.pushButton_start.isEnabled():
                self.start_clicker()
            else:
                self.stop_clicker()

    def on_hotkey_released(self):
        if self.ui.radioButton_trigger.isChecked():
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
        hold_duration = self.ui.spinBox_hold.value() if self.ui.checkBox_hold.isChecked() else 0

        mouse_shake = self.ui.checkBox_shake.isChecked()
        shake_min = self.ui.spinBox_shakeMin.value()
        shake_max = self.ui.spinBox_shakeMax.value()
        random_delay = self.ui.checkBox_randomDelay.isChecked()
        delay_min = self.ui.spinBox_delayMin.value()
        delay_max = self.ui.spinBox_delayMax.value()

        if custom_location or click_inside:
            x = self.ui.spinBox_x.value()
            y = self.ui.spinBox_y.value()
            hwnd = self.ui.spinBox_hwnd.value()
        else:
            x = y = hwnd = None

        self.click_thread = ClickThread(
            repeat, is_repeat, delay, click_inside, click_button,
            click_type, x, y, hwnd, custom_location, hold_duration,
            mouse_shake, shake_min, shake_max,
            random_delay, delay_min, delay_max
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