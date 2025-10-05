from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from bs4 import BeautifulSoup as bs
import requests
import time
import pandas as pd
import numpy as np

options = Options()
options.add_argument("--disable-notifications")  # 關閉通知請求
# 可加其他選項：不顯示警告、視窗最大化
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-notifications")
options.add_argument("--disable-blink-features=IndexedDB")

service = Service('D:\Code\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://lvr.land.moi.gov.tw/jsp/index.jsp")

driver.execute_script("window.indexDbDelAll = function() {};")
driver.execute_script("window.onerror = function() { return true; }")

# 點擊「買賣查詢」
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "pills-sale-tab"))).click()

# 選縣市
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "p_city")))
Select(driver.find_element(By.ID, "p_city")).select_by_visible_text("基隆市")

# 等區域載入
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "p_town"), "七堵區")
)
Select(driver.find_element(By.ID, "p_town")).select_by_visible_text("七堵區")

# 年月選擇
Select(driver.find_element(By.ID, "p_startY")).select_by_visible_text("113")
Select(driver.find_element(By.ID, "p_startM")).select_by_visible_text("4")
Select(driver.find_element(By.ID, "p_endY")).select_by_visible_text("114")
Select(driver.find_element(By.ID, "p_endM")).select_by_visible_text("4")

# 點擊前 JS log
print("查詢前 JS log：")
for log in driver.get_log('browser'):
    print(log['level'], log['message'])

# 點擊搜尋
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, '搜尋'))
).click()

# 點擊後等待片刻
time.sleep(2)

# 點擊後 JS log
print("查詢後 JS log：")
for log in driver.get_log('browser'):
    print(log['level'], log['message'])