import time

from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()  # Optional argument, if not specified will search path.

browser.get('http://www.bandcamp.com/')

time.sleep(2) # Let the user actually see something!

radio = browser.find_element(By.CLASS_NAME, 'menubar-bcweekly-shows-link').click()

time.sleep(2)
play_btn = browser.find_element(By.CLASS_NAME, 'play-btn').click()
time.sleep(10)

# search_box = browser.find_element(By.NAME, 'q')

# search_box.send_keys('The Devil Wears Prada')

# search_box.submit()

# time.sleep(5) # Let the user actually see something!

# browser.quit()