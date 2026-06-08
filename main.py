# ASTRA - Algorithmic Simulation for Trading Risk Analysis main.py
# This is the main entry point for the ASTRA application. It displays a welcome banner and a menu of options for users to navigate through the various features of the application.

import time
import pyfiglet
import shutil
from rich import print
from rich.console import Console

# Display the welcome banner
ascii_banner = pyfiglet.figlet_format("ASTRA", font="colossal")
terminal_size = shutil.get_terminal_size(fallback=(80, 24))
centered_banner = "\n".join(line.center(terminal_size.columns) for line in ascii_banner.splitlines())

print(f"[bold blue]{centered_banner}[/bold blue]")

time.sleep(2)

# Display the menu options
menu = [
    ("1", "Dashboard"),
    ("2", "Strategy Library"),
    ("3", "Backtesting"),
    ("4", "Scanner"),
    ("5", "Market Data"),
    ("6", "Diagnostics"),
    ("7", "Settings"),
    ("8", "Help"),
    ("0", "Exit"),
]

console = Console()

console.print("[bold white]═══ MENU ═══[/bold white]")

for number, option in menu:
    color = "red" if number == "0" else "cyan"
    console.print(f"[bold {color}][{number}][/bold {color}] {option}")

input("Press Enter to continue...")