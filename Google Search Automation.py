import selenium
from selenium inport webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome("C:\\Users\\shubh\\Desktop\\Python\\chromedriver.exe")

driver.set_page_load_timeout(0)
diver.get("http://www.google.com")
driver.find_element_by _id("fakebox-input").send_keys("Python Programming")
driver.find_element_by_id("fakebox-cursor").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()
