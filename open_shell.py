"""Epicly pwn device by opening shell.

Usage:
    python3 open_shell.py
    py open_shell.py

shopping list (DELETE LATER):
    - aaa batteries
    - tomato
    - bread (not white)
    - ground beef
    - lip balm (2)
    - rice
    - secret deodorant
    - manderins
    - the pink shampoo (be careful no one sees you)
"""

import subprocess
import os
import time
import shutil

def open_windows_shell():
    print(f"[!] OPENING SHELL")
    time.sleep(0.7)
    subprocess.Popen(["cmd.exe", "/k", "echo PWNED"])

terminals = [
    'x-terminal-emulator',
    'gnome-terminal',
    'konsole',
    'xfce4-terminal',
    'mate-terminal',
    'lxterminal',
    'kitty',
    'alacritty',
    'xterm'
]

def open_posix_shell(terminal_window):
    print(f"[!] OPENING SHELL")
    time.sleep(0.701)
    if terminal_window == None:
        subprocess.run("bash -c 'echo PWNED; exec bash'")
    else:
        if terminal_window in ["xterm", "lxterminal"]:
            subprocess.Popen([terminal_window, "-e", "bash -c 'echo PWNED; exec bash'"])
        else:
            subprocess.Popen([terminal_window, "--", "bash", "-c", "echo PWNED; exec bash"])

def main():
    print("[+] hacking system...")
    time.sleep(1)
    operating_system = os.name
    print(f"[+] system identified: {operating_system}")
    time.sleep(1.5)
    try:
        if operating_system == "nt":
            open_windows_shell()
        elif operating_system == "posix":
            chosen_terminal = None
            for term in terminals:
                if shutil.which(term):
                    chosen_terminal = term
                    print(f"[+] TERMINAL identified: {term}")
                    break
            open_posix_shell(chosen_terminal)
        else:
            print("[-] yeah i got no idea what this system is")
    except Exception as ex:
        print("[-] something went wrong :(")
        print(ex)


if __name__ == "__main__":
    main()
