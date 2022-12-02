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

# 웹페이지 해당 주소 이동
driver.implicitly_wait(3) # 웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window() # 화면을 최대화
driver.get("https://www.naver.com/")

# 검색어 입력창
search = driver.find_element(By. CSS_SELECTOR, "#query")
search.click()
search.send_keys("제주도 표선 해수욕장 호텔")
search_btn = driver.find_element(By.CSS_SELECTOR, "#search_btn > span.ico_search_submit")
search_btn.click()
time.sleep(3)

# 숙소 더보기
more = driver.find_element(By.CSS_SELECTOR,"#loc-main-section-root > section > div > div.api_more_wrap > a")
more.click()
time.sleep(3)

# 검색어 입력창
accname_xpath = driver.find_element(By.XPATH, '//*[@id="_pcmap_list_scroll_container"]/ul/li[1]/div[2]/a[1]/div/div/span[1]')
accname = accname_xpath.text
