#!/usr/bin/python3
# coding=utf-8
import sys
import tkinter

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
