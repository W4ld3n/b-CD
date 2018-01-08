#!/usr/bin/python
# -*- coding: utf-8 -*-
import curses
import linecache
from curses.textpad import Textbox, rectangle


class GUI:
    stdscr=""
    commandWin=""
    statusBox = ""
    songWin = ""
    volumeWin = ""
    barcodeWin = ""

    def __init__(self):
        self.stdscr = curses.initscr()
        # No display of pressed keys
        curses.noecho()
        # No line-buffer
        curses.cbreak()

        #Non-blocking input
        self.stdscr.nodelay(1)
        self.stdscr.box()

        # Escape-Sequence activation
        self.stdscr.keypad(1)
        curses.start_color()

        # Colors
        #Foreground Text, Background
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        # Windows and background color
        self.stdscr.bkgd(curses.color_pair(1))
        self.stdscr.refresh()


    def init(self):
        self.initStatusBox()
        self.initSongWin()
        self.initVolumeWin()
        self.initBarcodeWin()
        self.initCommandWin(self.stdscr)
        self.commandWin.nodelay(1)

    def close(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def initCommandWin(self,stdscr):
        stdscr.addstr(0, 0, "What to do next?: (hit Ctrl-G to send)")
        editwin = curses.newwin(1,30, 2,1)
        rectangle(stdscr, 1,0, 1+1+1, 1+30+1)
        stdscr.refresh()
        self.commandWin = editwin

    def initSongWin(self):
        self.songWin = curses.newwin(1,500, 5,1)
        self.songWin.bkgd(curses.color_pair(2))
        self.songWin.addstr(0, 0, "Song: ")
        self.songWin.refresh()

    def updateSong(self,song):
        self.songWin.clear()
        self.songWin.addstr(0, 0, "Song: " + song)
        self.songWin.refresh()

    def initStatusBox(self):
        self.statusBox = curses.newwin(1,50, 6,1)
        self.statusBox.bkgd(curses.color_pair(2))
        self.statusBox.addstr(0, 0, "Status: ")
        self.statusBox.refresh()

    def updateStatus(self,state):
        self.statusBox.clear()
        self.statusBox.addstr(0, 0, "Status: " + state)
        self.statusBox.refresh()

    def initBarcodeWin(self):
        self.barcodeWin = curses.newwin(1,50, 4,1)
        self.barcodeWin.bkgd(curses.color_pair(2))
        self.barcodeWin.addstr(0, 0, "BARCODE: ")
        self.barcodeWin.refresh()

    def updateBarcode(self,code):
        self.barcodeWin.clear()
        self.barcodeWin.addstr(0, 0, "BARCODE: " + code)
        self.barcodeWin.refresh()

    def initVolumeWin(self):
        self.volumeWin = curses.newwin(1,50, 7,1)
        self.volumeWin.bkgd(curses.color_pair(2))
        self.volumeWin.addstr(0, 0, "Volume: ")
        self.volumeWin.refresh()

    def updateVolume(self,volume):
        self.volumeWin.clear()
        self.volumeWin.addstr(0, 0, "Volume: " + volume)
        self.volumeWin.refresh()

    def inputCommand(self):
        box = Textbox(self.commandWin)

        # Let the user edit until Ctrl-G is struck.
        box.edit()

        # Get resulting contents
        message = box.gather()
        self.commandWin.clear()
        return message

    def getKey(self):
        return self.stdscr.getkey()
