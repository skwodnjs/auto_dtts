import time

import cv2
import numpy as np
import win32api
import win32con
import win32gui
import win32ui
from PIL import ImageGrab
from functools import partial


def capture_window(hWnd):
    # 창 맨 앞으로 가져오고 크기 및 위치 변경하기
    win32gui.SetForegroundWindow(hWnd)
    win32gui.MoveWindow(hWnd, -1920, 0, 620, 1000, True)

    # 창의 위치 가져오기
    rect = win32gui.GetWindowRect(hWnd)
    left, top, right, bottom = rect

    # 화면 캡쳐
    ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    screen_bgr = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screen_bgr


def find_and_click(hWnd, templatePath):
    # 화면 캡쳐하기
    screen = capture_window(hWnd)

    # 찾고자 하는 이미지를 불러오기
    template = cv2.imread(templatePath, cv2.IMREAD_COLOR)
    h, w, _ = template.shape

    # 이미지 찾기
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7  # Similarity threshold
    box_loc = np.where(result >= threshold)

    # 찾았는지 확인하기
    temp_x, temp_y = 0, 0
    for box in zip(*box_loc[::-1]):
        startX, startY = box
        endX, endY = startX + w, startY + h
        cv2.rectangle(screen, (startX, startY), (endX, endY), (0, 0, 255), 1)

        x = (startX + endX) // 2 - 1920
        y = (startY + endY) // 2

        if abs(temp_x - x) < 5 and abs(temp_y - y) < 5:
            temp_x, temp_y = x, y
            continue

        print(x, y)

        lParam = win32api.MAKELONG(x + 1920, y)
        win = win32ui.CreateWindowFromHandle(hWnd)
        win.PostMessage(win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        time.sleep(0.025)
        win.PostMessage(win32con.WM_LBUTTONUP, None, lParam)
        time.sleep(0.025)

        temp_x, temp_y = x, y

    cv2.imwrite('result.png', screen)


# Find the window handle for the target application
hwnd = win32gui.FindWindow(None, "NoxPlayer")  # Change "NoxPlayer" to your window title

if hwnd == 0:
    print("Window not found")
else:
    # Path to the template image
    template_path = '../../../birds/blue_gem.png'
    for i in range(20):
        find_and_click(hwnd, template_path)
        time.sleep(1)
