import pyautogui
import time

# 1. 화면 크기 출력
print(pyautogui.size())

# 2. 마우스 위치 출력
time.sleep(7)
print(pyautogui.position())

# 3. 마우스 이동
# 한번에 이동
# pyautogui.moveTo(300, 200)

# a초 만큼 이동
# pyautogui.moveTo(1791, 22, 2)

# 4, 마우스 클릭
# pyautogui.click()
# pyautogui.doubleClick()
# pyautogui.click(button='right')
# pyautogui.click(click=3, interval=1) #3번 클릭 1초마다

# 5. 마우스 드래그
# 1452,74 -> 2089,70
# pyautogui.moveTo(2089,70,2)
# pyautogui.dragTo(1830,69,2)
