import time
import os
from random import randint, choice
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re

# PROXIES = ['<50.96.204.48>:<18351>', '<207.55.243.42>:<64403>', '<194.36.98.231>:<80>', '<192.64.115.90>:<25462>', '<50.251.146.121>:<5678>']

options = webdriver.ChromeOptions()  # Optional argument, if not specified will search path.
options.add_experimental_option('detach', True)
# options.add_argument('--proxy-server=%s' % choice(PROXIES))
browser = webdriver.Chrome(options=options)
# browser.get('https://www.indeed.com/')
html_file = 'indeed.html'
abs_path = os.path.abspath(html_file)
file_url = f'file://{abs_path}'
browser.get(file_url)
time.sleep(randint(2, 4)) # Let the user actually see something!

# Get the list of the page btns at the buttom of the page and click the btn to go to the next page
page_btns = browser.find_elements(By.XPATH, '//ul[contains(@class, "css-1g90gv6")]//li[contains(@class, "css-227srf")]')
time.sleep(3)
page_btns[-1].click()


# Trying to find a way to to select all the filter options for the page
ul = browser.find_element(By.XPATH, '//div[@id="MosaicProviderRichSearchDaemon"]')
filter_options = ul.find_elements(By.XPATH, './/div//div//div//ul[@class="eu4oa1w0"]')
for filter in filter_options:
    try:
        button = filter.find_element(By.TAG_NAME, 'button').click()
    except ElementNotInteractableException:
        continue
    time.sleep(1)
# try:
#     job_searchbox = browser.find_element(By.XPATH, "//input[@name='q']")
#     job_searchbox.send_keys('it')
# except NoSuchElementException:
#     job_searchbox = WebDriverWait(browser, randint(5, 10)).until(EC.presence_of_element_located(
#         By.XPATH, "//input[@name='q']"))
#     job_searchbox.send_keys('it')
    
# try:
#     location_searchbox = browser.find_element(By.NAME, 'l')
#     location_searchbox.send_keys(Keys.CONTROL + 'a')
#     time.sleep(randint(1, 3))
#     location_searchbox.send_keys(Keys.DELETE)
#     time.sleep(randint(1, 2))
#     location_searchbox.send_keys('Savannah, GA')
# except NoSuchElementException:
#     location_searchbox = WebDriverWait(browser, randint(4, 10)).until(EC.presence_of_element_located(
#         By.XPATH, "//input[@name='l']"))
#     location_searchbox.send_keys(Keys.CONTROL + 'a')
#     time.sleep(randint(1, 3))
#     location_searchbox.send_keys(Keys.DELETE)
#     time.sleep(randint(1, 4))
#     location_searchbox.send_keys('Savannah, GA')
#     time.sleep(randint(1, 2))
    
# try:
#     submit_btn = browser.find_element(By.XPATH, "//button[@type='submit']").click()
# except NoSuchElementException:
#     submit_btn = WebDriverWait(browser, 500).until(EC.presence_of_element_located(
#         By.XPATH, "//button[@type='submit']"))
#     submit_btn.click()
    
# time.sleep(randint(1, 2))
# job_cards = browser.find_elements(By.CLASS_NAME, 'css-1ac2h1w')
# print(f'Num jobcards: {len(job_cards)}')
# for job_card in job_cards:
#     try:
#         title = job_card.find_element(By.XPATH, './/span[starts-with(@id, "jobTitle-")]')
#         company = job_card.find_element(By.XPATH, './/span[@data-testid="company-name"]')
#         location = job_card.find_element(By.XPATH, './/div[@data-testid="text-location"]')
#         print(title.text)
#         print(company.text)
#         print(location.text)
#         print()
#     except NoSuchElementException:
#         continue
    
time.sleep(5)

browser.quit()