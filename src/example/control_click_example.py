import time

import win32con
import win32gui
import win32api
import win32ui


def click1(hWnd, x, y):
    lParam = win32api.MAKELONG(x, y)

    win = win32ui.CreateWindowFromHandle(hWnd)
    win.PostMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win.PostMessage(win32con.WM_LBUTTONUP, None, lParam)


hwnd = win32gui.FindWindow(None, "NoxPlayer")

if hwnd != 0:
    # 창의 위치와 크기 가져오기
    rect = win32gui.GetWindowRect(hwnd)

    # 창의 크기 계산
    current_width = rect[2] - rect[0]
    current_height = rect[3] - rect[1]

    # 화면의 중앙을 클릭
    for i in range(10):
        click1(hwnd, current_width // 2, current_height // 2)
        time.sleep(0.75)
