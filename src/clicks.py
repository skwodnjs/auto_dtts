import time

import win32con
import win32api
import win32gui
import win32ui


def click(x, y, hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()
    lParam = win32api.MAKELONG(x, y)

    win = win32ui.CreateWindowFromHandle(hWnd)
    win.PostMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    time.sleep(0.05)
    win.PostMessage(win32con.WM_LBUTTONUP, None, lParam)


def click_center(hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()

    rect = win32gui.GetWindowRect(hWnd)

    current_width = rect[2] - rect[0]
    current_height = rect[3] - rect[1]

    click(current_width // 2, current_height // 2, hWnd)


def _get_nox():
    hWnd = win32gui.FindWindow(None, "NoxPlayer")
    if hWnd == 0:
        hWnd = win32gui.FindWindow(None, "녹스 플레이어")
    return hWnd


def click_cave(hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()
    if hWnd != 0:
        click(470, 285, hWnd)


def click_park(hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()
    if hWnd != 0:
        click(470, 375, hWnd)


def click_prize(hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()
    if hWnd != 0:
        click(470, 725, hWnd)


def click_hard_mode(hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()
    if hWnd != 0:
        click(80, 285, hWnd)


def click_back(hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()
    if hWnd != 0:
        click(60, 165, hWnd)


def click_back_park(hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()
    if hWnd != 0:
        click(70, 215, hWnd)


def click_explore_the_cave(hWnd=None):
    if hWnd is None:
        hWnd = _get_nox()
    if hWnd != 0:
        click(280, 770, hWnd)
