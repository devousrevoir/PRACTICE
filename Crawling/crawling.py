from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests
import re
import pandas as pd
import numpy as np
import os
import pandas as pd

from selenium.webdriver.common.keys import Keys

import warnings
warnings.filterwarnings('ignore')

name=['LG 에어로타워']
category=['별점']

#LG 에어로타워 후기
ns_address="https://search.shopping.naver.com/catalog/30128278618?cat_id=50002543&frm=NVSCPRO&query=%EC%97%90%EC%96%B4%EB%A1%9C%ED%83%80%EC%9B%8C&NaPm=ct%3Dl0ksn0vc%7Cci%3D5bbd25c0299ce5dbcb72ff2b1d41488ebd6d52ce%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D87194ce8ced4cb2b52968022b8eb9db67602d12e"


#xpath
#shoppingmall_review ="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/ul"
#shoppingmall_review = "/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[2]/ul/li[5]/a/strong"
shoppingmall_review = "/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul/li[4]/a"

header = {'User-Agent': ''}
d = webdriver.Chrome('chromedriver.exe') # webdriver = chrome
d.implicitly_wait(1) #隐形等待， 加载完后进入， 没加载完报错超市
d.get(ns_address)
req = requests.get(ns_address,verify=False)
html = req.text 
soup = BeautifulSoup(html, "html.parser")
sleep(2)

#쇼핑몰 리뷰 보기
d.find_element("xpath",shoppingmall_review).click()
sleep(2)

# element = d.find_element("xpath",shoppingmall_review)
# d.execute_script("arguments[0].click();", element)
# sleep(2)



test_Text = d.find_element("xpath",shoppingmall_review).text
print(test_Text)

df = pd.DataFrame()

test_Text = d.find_element("xpath", '/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[6]/div[2]/div[2]/div/ul').text
df = test_Text
print(df)

# 데이터프레임으로 만들기
a = df.split('\n')
b = pd.DataFrame(a, columns=['이름']).set_index('이름')

b.to_csv('./b.csv', encoding='utf-8-sig')