"""
References:
  https://itnext.io/overwrite-previously-printed-lines-4218a9563527
  colorama module
"""

class Graphics:
    LINE_UP = '\033[1A'  # move cursor up one line
    LINE_CLEAR = '\x1b[2K'  # clear the current line that the cursor is on

    class Fore:
        BLACK = '\x1b[30m'
        BLUE = '\x1b[34m'
        CYAN = '\x1b[36m'
        GREEN = '\x1b[32m'
        LIGHTBLACK_EX = '\x1b[90m'
        LIGHTBLUE_EX = '\x1b[94m'
        LIGHTCYAN_EX = '\x1b[96m'
        LIGHTGREEN_EX = '\x1b[92m'
        LIGHTMAGENTA_EX = '\x1b[95m'
        LIGHTRED_EX = '\x1b[91m'
        LIGHTWHITE_EX = '\x1b[97m'
        LIGHTYELLOW_EX = '\x1b[93m'
        MAGENTA = '\x1b[35m'
        RED = '\x1b[31m'
        RESET = '\x1b[39m'
        WHITE = '\x1b[37m'
        YELLOW = '\x1b[33m'

    class Back:
        BLACK = '\x1b[40m'
        BLUE = '\x1b[44m'
        CYAN = '\x1b[46m'
        GREEN = '\x1b[42m'
        LIGHTBLACK_EX = '\x1b[100m'
        LIGHTBLUE_EX = '\x1b[104m'
        LIGHTCYAN_EX = '\x1b[106m'
        LIGHTGREEN_EX = '\x1b[102m'
        LIGHTMAGENTA_EX = '\x1b[105m'
        LIGHTRED_EX = '\x1b[101m'
        LIGHTWHITE_EX = '\x1b[107m'
        LIGHTYELLOW_EX = '\x1b[103m'
        MAGENTA = '\x1b[45m'
        RED = '\x1b[41m'
        RESET = '\x1b[49m'
        WHITE = '\x1b[47m'
        YELLOW = '\x1b[43m'

    class Decor:
        BRIGHT = '\x1b[1m'
        DIM = '\x1b[2m'
        NORMAL = '\x1b[22m'
        RESET_ALL = '\x1b[0m'

    def clear_line(n: int = 1) -> None:
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        for _ in range(n):
            print(LINE_UP, end=LINE_CLEAR)
