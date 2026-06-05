import ctypes

# Define constants
INPUT_MOUSE = 0

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000

MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040

# Define structures
class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]

class _INPUT_UNION(ctypes.Union):
    _fields_ = [("mi", MOUSEINPUT)]

class INPUT(ctypes.Structure):
    _anonymous_ = ("union",)
    _fields_ = [("type", ctypes.c_ulong), ("union", _INPUT_UNION)]

# Main class
class MouseController:
    def __init__(self):
        self.screen_width = ctypes.windll.user32.GetSystemMetrics(0)
        self.screen_height = ctypes.windll.user32.GetSystemMetrics(1)

    def _get_button_flags(self, button: str):
        button = button.lower()
        if button == "left":
            return MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
        elif button == "right":
            return MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP
        elif button == "middle":
            return MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP
        else:
            raise ValueError("Unsupported mouse button. Use 'left', 'right', or 'middle'.")

    def _create_mouse_input(self, x, y, flags):
        abs_x = int(x * 65536 / self.screen_width)
        abs_y = int(y * 65536 / self.screen_height)

        mi = MOUSEINPUT(
            dx=abs_x,
            dy=abs_y,
            mouseData=0,
            dwFlags=flags,
            time=0,
            dwExtraInfo=None
        )
        return INPUT(type=INPUT_MOUSE, mi=mi)

    def _create_click_input(self, flags):
        mi = MOUSEINPUT(
            dx=0,
            dy=0,
            mouseData=0,
            dwFlags=flags,
            time=0,
            dwExtraInfo=None
        )
        return INPUT(type=INPUT_MOUSE, mi=mi)

    def click(self, x, y, button='left', hold=False, hold_duration=0):
        down_flag, up_flag = self._get_button_flags(button)
        inputs = [
            self._create_mouse_input(x, y, MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE),
            self._create_mouse_input(x, y, down_flag),
        ]
        for i in inputs:
            ctypes.windll.user32.SendInput(1, ctypes.byref(i), ctypes.sizeof(INPUT))

        if hold:
            ctypes.windll.kernel32.Sleep(int(hold_duration))

        up_input = self._create_mouse_input(x, y, up_flag)
        ctypes.windll.user32.SendInput(1, ctypes.byref(up_input), ctypes.sizeof(INPUT))

    def click_current_position(self, button='left', hold=False, hold_duration=0):
        down_flag, up_flag = self._get_button_flags(button)
        down_input = self._create_click_input(down_flag)
        ctypes.windll.user32.SendInput(1, ctypes.byref(down_input), ctypes.sizeof(INPUT))

        if hold:
            ctypes.windll.kernel32.Sleep(int(hold_duration))

        up_input = self._create_click_input(up_flag)
        ctypes.windll.user32.SendInput(1, ctypes.byref(up_input), ctypes.sizeof(INPUT))

# Example usage
if __name__ == "__main__":
    mouse = MouseController()
    # Examples:
    mouse.click_current_position(button="right")
    # mouse.click(300, 500, button="middle")
