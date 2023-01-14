'''
IchiiDev, 2023
Project Name: snippets-manager
File Name: main.py
License: MIT
'''

import os
from os import path
from pick import pick
import shutil

HOME = os.environ.get("HOME")
DEFAULT_SNIPPETS_DIR = f"{HOME}/.snippets"
SHELLS = [f"{HOME}/.bashrc", f"{HOME}/.zshrc", f"{HOME}/.config/fish/config.fish"]

def init_config_dir(dir):
    if path.exists(dir):
        return False
    else:
        os.mkdir(dir)
        return True

def select_shell():
    title = "Please select your shell:"
    options = ["bash", "zsh", "fish"]
    option, index = pick(options, title, indicator="->")
    print(f"Loading config for {option}...")
    return SHELLS[index], option

def append_config(shell_path):
    with open(shell_path, "a") as f:
        if is_config_set(shell_path):
            return
        f.write(f"alias snippets='{HOME}/bin/snippets.py'\nPATH=$PATH:$HOME/bin")
        f.close()

def is_config_set(config_path):
    with open(config_path, "r") as f:
        for line in f:
            if "alias snippets" in line:
                return True
        return False

def copy_binaries():
    if not path.exists(f"{HOME}/bin"):
        os.mkdir(f"{HOME}/bin")
    if not path.exists(f"{HOME}/bin/snippets.py"):
        try:
            shutil.copy("./src/bin/snippets.py", f"{HOME}/bin/snippets.py")
        except PermissionError:
            print(f"Error copying binary to {HOME}/bin/snippets")
            exit(1)

if __name__ == "__main__":
    print("Initialising snippets directory...")
    created = init_config_dir(DEFAULT_SNIPPETS_DIR)
    if not created:
        print("Dir already exists... Aborting...")
        exit(1)
    print("Dir '~/.snippets' created")
    copy_binaries()
    print(f"Binaries copied to {HOME}/bin/snippets.py")
    shell_path, shell = select_shell()
    print(f"Adding executable to {shell_path}")
    append_config(shell_path)
    print("Alias added!")
    print("Reloading shell...")
    print("Installation complete!")
    os.system(shell)
