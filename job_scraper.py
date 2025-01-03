import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()  # Optional argument, if not specified will search path.

browser.get('https://www.indeed.com')
time.sleep(2) # Let the user actually see something!

job_searchbox = browser.find_element(By.NAME, 'q')
job_searchbox.send_keys('it')

location_searchbox = browser.find_element(By.NAME, 'l')
location_searchbox.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
location_searchbox.send_keys(Keys.DELETE)
time.sleep(1)
location_searchbox.send_keys('Savannah, GA')
time.sleep(1)
submit_btn = browser.find_element(By.CLASS_NAME, 'yosegi-InlineWhatWhere-primaryButton').click()

time.sleep(10)

# search_box = browser.find_element(By.NAME, 'q')

# search_box.send_keys('The Devil Wears Prada')

# search_box.submit()

# time.sleep(5) # Let the user actually see something!

# browser.quit()