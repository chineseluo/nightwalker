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
import pytest
import argparse
from nightwalker import __version__, __description__


def init_scaffold_parser(subparsers):
    sub_scaffold_parser = subparsers.add_parser(
        "startproject", help="Create a new project with template structure."
    )
    sub_scaffold_parser.add_argument(
        "project_name", type=str, nargs="?", help="Specify new project name."
    )
    return sub_scaffold_parser


def main():
    # Generate subcommand object
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("-v", "-V", "--version", "--Version", dest="version", action="store_true", help="show version")
    subparsers = parser.add_subparsers(help="Night walker sub-command help")
    sub_scaffold_parser = init_scaffold_parser(subparsers)

    nw_argv = sys.argv
    print(nw_argv)
    if len(nw_argv) == 1:
        parser.print_help()
        sys.exit()
    elif len(nw_argv) == 2:
        if nw_argv[1] in ["-V", "-v", "--Version", "--version"]:
            print(f"The Night Walker version is {__version__}")
        elif nw_argv[1] in ["-h", "-H", "--help", "--Help"]:
            parser.print_help()
        elif nw_argv[1] == "startproject":
            sub_scaffold_parser.print_help()
        else:
            print("Please use nm - h to view help information")
        sys.exit(0)
    elif len(sys.argv) == 3 and sys.argv[1] == "startproject" and sys.argv[2] in ["-h", "-H", "--help", "--Help"]:
        pytest.main(["-h"])
        sys.exit(0)


if __name__ == "__main__":
    main()
