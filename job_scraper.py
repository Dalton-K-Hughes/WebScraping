import time

from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()  # Optional argument, if not specified will search path.
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.get('https://www.indeed.com/')
time.sleep(2) # Let the user actually see something!

try:
    job_searchbox = WebDriverWait(browser, 500).until(EC.presence_of_element_located(
        By.XPATH, "//input[@name='q']")).send_keys('it')
except NoSuchElementException:
    browser.quit()
finally:
    job_searchbox = browser.find_element(By.XPATH, "//input[@name='q']").send_keys('it')

# job_searchbox = browser.find_element(By.NAME, 'q')
# job_searchbox.send_keys('it')

try:
    location_searchbox = WebDriverWait(browser, 500).until(EC.presence_of_element_located(
        By.XPATH, "//input[@name='l']"))
    location_searchbox.send_keys(Keys.CONTROL + 'a')
    time.sleep(1)
    location_searchbox.send_keys(Keys.DELETE)
    time.sleep(1)
    location_searchbox.send_keys('Savannah, GA')
except NoSuchElementException:
    browser.quit()
finally:
    location_searchbox = browser.find_element(By.NAME, 'l')
    location_searchbox.send_keys(Keys.CONTROL + 'a')
    time.sleep(1)
    location_searchbox.send_keys(Keys.DELETE)
    time.sleep(1)
    location_searchbox.send_keys('Savannah, GA')

# location_searchbox = browser.find_element(By.NAME, 'l')
# location_searchbox.send_keys(Keys.CONTROL + 'a')
# time.sleep(1)
# location_searchbox.send_keys(Keys.DELETE)
# time.sleep(1)
# location_searchbox.send_keys('Savannah, GA')
# time.sleep(1)
try:
    submit_btn = WebDriverWait(browser, 500).until(EC.presence_of_element_located(
        By.XPATH, "//button[@type='submit']"
    ))
    submit_btn.click()
except NoSuchElementException:
    browser.quit()
finally:
    submit_btn = browser.find_element(By.CLASS_NAME, 'yosegi-InlineWhatWhere-primaryButton').click()

time.sleep(5)

# job_cards = browser.find_elements(By.CLASS_NAME, 'css-1ac2h1w eu4oa1w0')
# for job_card in job_cards:
#     print(job_card)

# browser.quit()