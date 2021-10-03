import selenium, time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import csv 



#open cophieu68
index = webdriver.Chrome(ChromeDriverManager().install())
index.get('https://www.cophieu68.vn/')

#wait for loading
for i in reversed(range(10)):
	print(i+1,end = " "),
	sleep(1)
print ("Go!!\n")

#open login page and wait 10s
login = index.find_element_by_link_text("Đăng nhập")
login.click()
for i in reversed(range(10)):
	print(i+1,end = " "),
	sleep(1)

#typing and submit account and wait 10s
print ("Typing...\n")
username = index.find_element_by_css_selector('#div_form_login > div > form > table > tbody > tr:nth-child(4) > td > input')
username.send_keys('buihuunam95@gmail.com')
password = index.find_element_by_css_selector('#div_form_login > div > form > table > tbody > tr:nth-child(5) > td > input')
password.send_keys('kyxqwr')
password.submit()
for i in reversed(range(10)):
	print(i+1,end = " "),
	sleep(1)
#Open data index and wait 10s
print ("Open data page..\n")

gate = "#navlist > li:nth-child(7) > a"
download = index.find_element_by_css_selector(gate)
download.click()

for i in reversed(range(10)):
	print(i+1,end = " "),
	sleep(1)
print("Here we go!\n")
print("Downloading...")

#download
portfolio = []

with open('HOSE.csv') as csvfile:    
	csvReader = csv.reader(csvfile)    
	for row in csvReader:        
		portfolio.append(row[0])

portfolio[0]="AAA"
numlist = len(portfolio)
for i in range(numlist):
	print("Downloading",portfolio[i],'\n')
	index.get('https://www.cophieu68.vn/export/reportfinance.php?id='+portfolio[i])
	sleep(3)