#!/usr/bin/env python3
'''
IchiiDev, 2023
Project Name: snippets-manager
File Name: snippets.py
License: MIT
'''

import os
from os import path
import shutil
import argparse

HOME = os.environ.get("HOME")

def init_config():
    parser = argparse.ArgumentParser(description="Snippets manager")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("snippet", help="Snippet name", type=str, nargs="?")
    group.add_argument("-l", "--list", help="List all snippets", action="store_true")
    return parser

def list_snippets():
    print("Listing snippets...\nAvailable snippets:")
    for snippet in os.listdir(f"{HOME}/.snippets"):
        snippet = snippet.replace(".tar.gz", "")
        print(f"- {snippet}")

def copy_snippet(snippet):
    if not path.exists(f"{HOME}/.snippets/{snippet}.tar.gz"):
        print(f"Snippet {snippet} doesn't exists")
        return
    os.system(f"tar -xf {HOME}/.snippets/{snippet}.tar.gz")

if __name__ == "__main__":
    parser = init_config()
    args = parser.parse_args()
    if args.list:
        list_snippets()
    elif args.snippet:
        copy_snippet(args.snippet)
    else:
        parser.print_help()
