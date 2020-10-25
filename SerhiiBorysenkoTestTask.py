from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
# 1)Open "https://hotline.ua/" in Chrome
driver.get("https://hotline.ua/")
time.sleep(2)
# 2)Enter "iPhone7" in search field
driver.find_element_by_xpath('//input[@id="searchbox"]').send_keys(["iPhone 7"])
time.sleep(2)
# 3)Click on search button
driver.find_element_by_css_selector("#doSearch").click()
time.sleep(2)
# 4)Click on first link
driver.find_element_by_css_selector('li:nth-child(1) div.item-info p a').click()
time.sleep(3)
driver.quit()