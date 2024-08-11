import time

import win32api
import win32gui

hWnd = win32gui.FindWindow(None, "NoxPlayer")
if hWnd == 0:
    hWnd = win32gui.FindWindow(None, "녹스 플레이어")

if hWnd != 0:
    for i in range(10):
        x, y = win32api.GetCursorPos()
        print(x+1920, y)
        time.sleep(0.75)
