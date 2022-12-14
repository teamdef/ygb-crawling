import openpyxl
import os
import sys
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#엑셀에서 데이터 추출(형식 : ㅇㅇ동 ㅁㅁ식당)
filename = '관악구레스토랑.xlsx'
restaurant_file = openpyxl.load_workbook(filename)
restaurants = restaurant_file.worksheets[0]
data = []

for restaurant in restaurants.iter_rows(min_row=3):
    address = restaurant[16].value
    if address is not None:
        data.append([
            restaurant[16].value.split('(')[1].split(')')[0],
            restaurant[18].value
        ])

print(data[0])

json_data = {}
file_path = "./restaurants.json"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('크롬드라이버 경로',options=options)

for i in data:
    keyword = i[0] + ' ' + i[1]
    print(keyword, end=" ")
    try:
        content = {}
        kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"
        driver.get(kakao_map_search_url)
        driver.implicitly_wait(time_to_wait=3)

        newlink = driver.find_element(by='xpath',value = '//*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]').send_keys(Keys.ENTER)
        driver.switch_to.window(driver.window_handles[-1])

        rateNum = driver.find_element(by='xpath',value = '//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[1]/span[1]').text

        Timelist = driver.find_element(by=By.CLASS_NAME, value = 'list_operation')
        periodTime = Timelist.find_elements(by=By.CLASS_NAME, value = 'txt_operation')
        detailTime = Timelist.find_elements(by=By.CLASS_NAME, value = 'time_operation')

        menus_dic = {}
        menulist = driver.find_element(by=By.CLASS_NAME, value = 'list_menu')
        menus = menulist.find_elements(by=By.CLASS_NAME, value = 'loss_word')
        menus_price = menulist.find_elements(by=By.CLASS_NAME, value = 'price_menu')
        for a,b in zip(menus,menus_price):
            menus_dic[a.text] = b.text

        print("평점 " + rateNum)
        content["평점"] = rateNum

        if detailTime:
            time = []
            for i in periodTime:
                time.append(i.text)
                print(i.text)
            content["영업 시간"] = time
        else:
            print("시간 정보 없음")
            content["영업 시간"] = "시간 정보 없음"

        for i in menus_dic:
            print("key: {}, value: {}".format(i, menus_dic[i]))
        content["메뉴"] = menus_dic

        json_data[keyword] = list(content.items())
        driver.close()
        driver.switch_to.window(driver.window_handles[0]);

    except Exception as e1:
        print("정보 없음")
        driver.switch_to.window(driver.window_handles[0]);
        pass

    print('\n')

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(json_data, file, indent=4)
driver.close()