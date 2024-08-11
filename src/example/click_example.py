import time
import win32api
import win32con


# 좌표로 마우스 이동
def move_mouse(x, y):
    win32api.SetCursorPos((x, y))


# 왼쪽 마우스 클릭
def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)  # 클릭 지속 시간
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# 오른쪽 마우스 클릭
def right_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.05)  # 클릭 지속 시간
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


if __name__ == "__main__":
    # 예제: 특정 좌표로 이동 후 클릭
    move_mouse(100, 200)
    left_click()
    move_mouse(-300, 300)
    right_click()
