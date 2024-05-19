import sys
from threading import Thread
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
import win32api, win32con
import mouse


sys.setrecursionlimit(15000)
import pyperclip as pc

f = open("keyss.txt", "r")
x = 0


def confirm(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    mouse.click('left')

def loop1():
 while True:
    time.sleep(5)
    confirm(1020, 523)



def enter(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    mouse.click('left')


def loop2():
 while True:
    time.sleep(8)
    enter(1020, 630)



def entry(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    mouse.click('left')


def loop3():
 while True:
    time.sleep(6)
    entry(1020, 670)



def pidoras(x, f = open("keyss.txt", "r")):
    for line in f:
        time.sleep(4)
        print(line.split()[0])
        x += 1
        text_to_copy = line.split()[0]

        # Copy text to the clipboard
        pc.copy(text_to_copy)

        # Retrieve the copied text from the clipboard
        pasted_text = pc.paste()

        # Print the N0OA5-7J8CO-ZC5BF text and its data type
        print("Pasted Text:", pasted_text)
        keyboard.press(Key.ctrl)
        keyboard.press('v')
        keyboard.pressed('v')
        keyboard.pressed(Key.ctrl)
        return pidoras(x+1, f)

def loop4():
 while True:
  pidoras(x, open("keyss.txt", "r"))
  time.sleep(1)

Thread(target = loop4).start()
Thread(target = loop2).start()
Thread(target = loop1).start()
Thread(target = loop3).start()

if(input("")) == 'yes':
       f.close()

