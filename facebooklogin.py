import random
import time
import pandas as pd
import json
import sys
import logging

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,ElementNotVisibleException,TimeoutException,ElementNotSelectableException
from pyvirtualdisplay import Display
from selenium.webdriver.common.action_chains import ActionChains

import re

def search(driver,keyword):
	p=dict()
	p['name']=''
	p['auto']=''
	driver.get('https://www.facebook.com/')
	time.sleep(10)
	Input=driver.find_element_by_id('email')
	Input.send_keys('')
	Input2=driver.find_element_by_id('pass')
	Input2.send_keys('')
	driver.find_element_by_id('u_0_5').click()
	time.sleep(40)
	driver.find_element_by_css_selector('.fbRemindersTitle').click()
	time.sleep(10)
	Input3=driver.find_element_by_id('u_1i_5')
	Input3.send_keys('Happy Birthday :)')
	Input3.send_keys(Keys.ENTER)     

def main():
	try:
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--no-sandbox')
		driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options = chrome_options)
		h=search(driver,row.Item)
			#file_write(header,data)
	#print h['auto']
		driver.close()
		driver.quit()
	except Exception as e:
		logging.exception("message")
		driver.quit()
if __name__ == "__main__":
	main()
