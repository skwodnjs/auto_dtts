import time
import win32gui

from click_example import move_mouse, left_click

# 특정 창의 핸들 가져오기 (창 제목을 알고 있을 때)
hwnd = win32gui.FindWindow(None, "NoxPlayer")

# 창이 존재하지 않으면 hwnd는 0이 됩니다. 이를 체크해야 합니다.
if hwnd == 0:
    print("창을 찾을 수 없습니다.")
else:
    print(f"창의 핸들: {hwnd}")

if hwnd != 0:
    # 창의 위치와 크기 가져오기
    rect = win32gui.GetWindowRect(hwnd)

    # 창의 크기 계산
    current_width = rect[2] - rect[0]
    current_height = rect[3] - rect[1]

    print(current_width, current_height)

    # 창 맨 앞으로 가져오고 위치 변경하기
    win32gui.SetForegroundWindow(hwnd)
    win32gui.MoveWindow(hwnd, -1920, 0, 640, 1136, True)
    time.sleep(0.05)

    # 창의 중앙 좌표 계산
    rect = win32gui.GetWindowRect(hwnd)
    x1, y1, x2, y2 = rect  # x1, y1은 좌상단, x2, y2는 우하단 좌표
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    # 중앙으로 마우스 이동 후 클릭
    move_mouse(center_x, center_y)
    for i in range(1):
        left_click()
        time.sleep(0.75)
