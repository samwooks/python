'''
centerwin.py is a code snipplet to center a windows gui. default mode is set to 'zoomed', meaning full window.
Upon minimizing the window, the window will be centered with WxH 300x300 pixels.
'''

from tkinter import *
import tkinter as tk


#create main window called root
root = Tk()
root.state('zoomed')


win_width = 300
win_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coord = (screen_width/2) - (win_width/2)
y_coord = (screen_height/2) - (win_height/2)

root.geometry("%dx%d+%d+%d" % (win_width, win_height, x_coord, y_coord))

root.minsize(win_width, win_height)

mainloop()
