#!/usr/bin/python3
# coding=utf-8
import os
import sys
import tkinter

test_env = os.path.expanduser("~/Envs/test/Lib/site-packages")

if os.path.exists(test_env):
    sys.path.insert(0, test_env)

import dandan


name = 'Reaper'
root = tkinter.Tk(baseName=name)


def setup():
    pass


def main():
    root.title(name)

    # show on top
    root.call('wm', 'attributes', '.', '-topmost', True)

    root.mainloop()


if __name__ == '__main__':
    main()
