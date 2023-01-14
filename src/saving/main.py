'''
IchiiDev, 2023
Project Name: snipets-manager
File Name: main.py
License: MIT
'''

import os
from os import path
import shutil

HOME = os.environ.get("HOME")

def clean_snippets_dir():
    for file in os.listdir(f"{HOME}/.snippets"):
        os.remove(f"{HOME}/.snippets/{file}")

def clean_out_dir():
    for file in os.listdir("./out"):
        os.remove(f"./out/{file}")
    os.rmdir("./out")

def copy_files():
    for archive in os.listdir("./out"):
        shutil.copyfile(f"./out/{archive}", f"{HOME}/.snippets/{archive}")

def save_snippet(dir):
    elements = []
    for file in os.listdir(f"./snippets/{dir}"):
        elements.append(f"./snippets/{dir}/{file}")
    os.system(f"tar -czf ./out/{dir}.tar.gz {' '.join(elements)}")
    print(f"-> Created archive for {dir}.")

if __name__ == "__main__":
    clean_snippets_dir()
    if not path.exists(f"{HOME}/.snippets"):
        print("No snippets directory found... Please run 'make install' first")
        exit(1)
    print("Snippets directory found, loading snippets...")
    os.mkdir("./out")
    for dir in os.listdir(f"./snippets"):
        save_snippet(dir)
    copy_files()
    clean_out_dir()
    print("Snippets saved !")
