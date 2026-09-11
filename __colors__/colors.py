import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

# Foreground colors
fc = Fore.RESET          # Clear/Reset
fg = Fore.GREEN          # Green (Success)
fr = Fore.RED            # Red (Error)
fb = Fore.BLUE           # Blue (Info)
fy = Fore.YELLOW         # Yellow (Warning)
fm = Fore.MAGENTA        # Magenta

# Styles
sd = Style.DIM           # Dim
sb = Style.BRIGHT        # Bold
