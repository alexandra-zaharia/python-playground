from enum import Enum, auto

class Color(Enum):
    RED = 31
    GREEN = auto()
    YELLOW = auto()
    BLUE = auto()
    MAGENTA = auto()
    CYAN = auto()
    LIGHTRED = 91
    LIGHTGREEN = auto()
    LIGHTYELLOW = auto()
    LIGHTBLUE = auto()
    LIGHTMAGENTA = auto()
    LIGHTCYAN = auto()

    _START = '\u001b['
    _BOLD = ';1'
    _BLINK = ';5'
    _END = 'm'
    _RESET = '\u001b[0m'

    @staticmethod
    def colored(color, msg, bold=False, blink=False):
        if not(isinstance(color, Color)):
            raise TypeError(f'Unknown color {color}')

        fmt_msg = Color._START.value + str(color.value)

        if bold:
            fmt_msg += Color._BOLD.value
        if blink:
            fmt_msg += Color._BLINK.value

        return fmt_msg + Color._END.value + str(msg) + Color._RESET.value
