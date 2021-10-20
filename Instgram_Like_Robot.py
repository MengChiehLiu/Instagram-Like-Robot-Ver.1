"""
Instgram_Like_Robot (Ver.1)
Created by MJ. Liu
2021/10/21
"""

from selenium.webdriver.support import expected_conditions as EC  #pip install selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="chromedriver.exe")  #記得存在同個資料夾裡
url = 'https://www.instagram.com/'  

# ------ 前往該網址 ------
browser.get(url) 

# ------ 填入帳號與密碼 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))

# ------ 網頁元素定位 ------
username_input = browser.find_elements_by_name('username')[0]
password_input = browser.find_elements_by_name('password')[0]
#print("inputing username and password...")

# ------ 輸入帳號密碼 ------
username_input.send_keys("account")    #你的IG帳號
password_input.send_keys("password")   #你的IG密碼

# ------ 登入 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
'//*[@id="loginForm"]/div/div[3]/button/div')))
# ------ 網頁元素定位 ------
login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]
# ------ 點擊登入鍵 ------
login_click.click()

# ------ 不儲存登入資料 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

# ------網頁元素定位 ------
store_click = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]

# ------ 點擊不儲存鍵 ------
store_click.click()

# ------ 不開啟通知 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))

# ------ 網頁元素定位 ------                                                                                                    
notification_click = browser.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')[0]

# ------ 點擊不開啟通知 ------
notification_click.click()

#刷頁面
url_main_page = 'https://www.instagram.com/XXXXXXXXX/'   #你想洗讚的網頁(個人首頁)
browser.get(url_main_page)

for i in range(2):
    html = browser.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    time.sleep(2)

# 取得要按讚貼文網址
# 用find_elements_by_class_name找到放貼文地方
post = browser.find_elements_by_class_name('v1Nh3') # 最新貼文都套用v1Nh3這class
hashtag_url_list = [] # 等等放網址
for i in post:
    # 在每個post找到標籤a後取得herf(網址)屬性
    post_url = i.find_element_by_tag_name('a').get_attribute('href') 
    hashtag_url_list.append(post_url) # 放入網址

# 分別切換網頁去按讚
for url in hashtag_url_list:
    browser.get(url)
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "wpO6b ")))
    #browser.implicitly_wait(10) 

    # 找到按讚的按鈕
    like_button = browser.find_elements_by_class_name("wpO6b ")[1]
    t = like_button.find_element_by_class_name('_8-yf5').get_attribute('aria-label') # 選到文字讚的那個class

    # 檢驗是讚還是收回按 是讚就按下去
    if t == '讚':
        like_button.click() # 點讚
    time.sleep(1) # 停頓一下以免被抓

# 關閉瀏覽器
browser.close()
