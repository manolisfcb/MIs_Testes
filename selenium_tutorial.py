# Tutorial selenium #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads

import selenium

from selenium import webdriver

path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get('https://techwithtim.net')

print(driver.title)
