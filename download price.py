import sys 
import selenium, time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


path = "D:\\Coding\\QMF01\\FR-Vietnam"

with open(path, 'wb') as f:
    f.write(r.content)
#install Chrome Driver
index = webdriver.Chrome(ChromeDriverManager().install())

index.get('https://www.cophieu68.vn/export/excelfull.php?id=^vnindex')
#open login page and wait 5s
login = index.find_element_by_link_text("Đăng nhập")
login.click()
for i in reversed(range(2)):
	print("|",end = " "),
	sleep(1)


#typing and submit account and wait 10s
print ("Typing...\n")
username = index.find_element_by_css_selector('#div_form_login > div > form > table > tbody > tr:nth-child(4) > td > input')
username.send_keys('buihuunam95@gmail.com')
password = index.find_element_by_css_selector('#div_form_login > div > form > table > tbody > tr:nth-child(5) > td > input')
password.send_keys('kyxqwr')
password.submit()

for i in reversed(range(2)):
	print("|",end = " "),
	sleep(1)
print("Here we go!\n")

#download
portfolio = ["HPG","NKG","HSG"]
numlist = len(portfolio)
for i in range(numlist):
	print("Downloading",portfolio[i],'\n')
	index.get('https://www.cophieu68.vn/export/reportfinance.php?id='+portfolio[i])

