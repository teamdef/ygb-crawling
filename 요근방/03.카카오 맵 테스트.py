from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


#카카오 맵 이동
driver.implicitly_wait(5) # 웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window() # 화면을 최대화
driver.get("https://map.kakao.com/")

# 마우스 한번에 이동 및 클릭
pyautogui.moveTo(750, 335)
pyautogui.click()
time.sleep(2)

# 길찾기 클릭
roadsearch = driver.find_element(By. CSS_SELECTOR, "#search\.tab2 > a")
roadsearch.click()

# 마우스 한번에 이동 및 클릭
pyautogui.moveTo(750, 335)
pyautogui.click()
time.sleep(2)

# 길찾기 검색 클릭
pyautogui.moveTo(227, 485)
pyautogui.doubleClick()
time.sleep(2)

# 길찾기 검색
departsearch = driver.find_element(By. CSS_SELECTOR, "#info\.route\.waypointSuggest\.input0")
departsearch.click()
departsearch.send_keys("제주도 표선 해수욕장")
departsearch.send_keys(Keys.ENTER)

# 길찾기 검색 클릭
pyautogui.moveTo(208, 546)
pyautogui.doubleClick()
time.sleep(2)

# 길찾기 검색
arrivalsearch = driver.find_element(By. CSS_SELECTOR, "#info\.route\.waypointSuggest\.input0")
arrivalsearch.click()
