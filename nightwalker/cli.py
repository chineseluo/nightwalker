#!/user/bin/env python
# -*- coding: utf-8 -*-

"""
------------------------------------
@Project : nightwalker
@Time    : 2020/10/13 14:01
@Auth    : chineseluo
@Email   : 848257135@qq.com
@File    : cli.py
@IDE     : PyCharm
------------------------------------
"""
import os
import sys
import argparse
from nightwalker import __version__, __description__


def main():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("-v", "-V", "--version", "--Version", dest="version", action="store_true", help="show version")
    nw_argv = sys.argv
    print(nw_argv)
    print(len(nw_argv))
    if len(nw_argv) == 1:
        print("ni")
    elif len(nw_argv) == 2:
        if nw_argv[1] in ["-V", "-v", "--Version", "--version"]:
            print(f"The Night Walker version is {__version__}")
        elif nw_argv[1] in ["-h", "-H", "--help", "--Help"]:
            print("help")
        elif nw_argv[1] == "startproject":
            print("start create project")
        else:
            print("please input again")
        sys.exit(0)


if __name__ == "__main__":
    main()
