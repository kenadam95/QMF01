import selenium, requests, time
import openpyxl
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open cophieu68
index = webdriver.Chrome()
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
portfolio = ['CEO','CLG','D11','D2D','DIG','DLG','DLR','DRH','DTA','DXG','FLC','HAG','HDC','HDG','HQC','IDI','IDJ','IDV','IJC','ITA','ITC','KAC','KBC','KDH','LCG','LEC','LGL','LHG','NBB','NDN','NHA','NLG','NTB','NTL','NVL','NVT','OGC','PDR','PFL','PPI','PVL','QCG','RCD','RCL','REE','SC5','SCR','SDI','SDU','SGR','SHN','SJS','SZL','TDC','TDH','TIG','TKC','UDC','UIC','VCR','VHM','VIC','VNI','VPH','VRE']
numlist = len(portfolio)
for i in range(numlist):
	print("Downloading",portfolio[i],'\n')
	index.get('https://www.cophieu68.vn/export/excelfull.php?id='+portfolio[i])
	sleep(3)