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
from fake_useragent import UserAgent

# Class used to create a object to represent a Indeed Web Scrapper with Google Chrome's webdriver
class Indeed_Scrapper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_argument('--incognito')
        
        # Disable Selenium detection
        options.add_argument('--disable-blink-features=AutomationControlled')
        
        # Create randomized user agent
        user_agent = UserAgent()
        user_agent = user_agent.random
        options.add_argument(f'user-agent={user_agent}')
        
        self.browser = webdriver.Chrome(options=options)
        self.browser.get('https://www.indeed.com/')
        
    #TODO: Create a function to login into the site so i can automatically apply for jobs     
    def login(self):
        pass
    
    #TODO: Create a function to get all the filter options of the website relavent to improving job matches
    def get_filter_options(self):
        pass

            
    # Get the searchbox for using keywords of specific job terms
    def get_searchbox(self):
        try:
            searchbox = self.browser.find_element(By.XPATH, '//input[@name="q"]')
            return searchbox
        except NoSuchElementException:
            searchbox = WebDriverWait(self.browser, randint(5, 10)).until(EC.presence_of_element_located(By.XPATH, "//input[@name='q']"))
            return searchbox
    
    # Get the searchbox for searching for specific locations
    def get_locationbox(self):
        try:
            searchbox = self.browser.find_element(By.XPATH, '//input[@name="l"]')
            return searchbox
        except NoSuchElementException:
            searchbox = WebDriverWait(self.browser, randint(5, 10)).until(EC.presence_of_element_located(By.XPATH, '//input[@name="l"]'))
            return searchbox
    
    # Get the submot button of the webpage when submitting a job search    
    def get_submit_button(self):
        try:
            submit_btn = self.browser.find_element(By.XPATH, '//button[@type="submit"]')
            return submit_btn
        except NoSuchElementException:
            submit_btn = WebDriverWait(self.browser, randint(5, 10)).until(EC.presence_of_element_located(By.XPATH, '//button[@type="submit"]'))
            return submit_btn
        
    # Get all the job cards on a page of the site
    def get_job_cards(self):
        try:
            job_cards = self.browser.find_elements(By.CLASS_NAME, 'css-1ac2h1w')
            return job_cards
        except NoSuchElementException:
            job_cards = WebDriverWait(self.browser, randint(5, 10)).until(EC.presence_of_all_elements_located(By.CLASS_NAME, 'css-1ac2h1w'))
            return job_cards
    
    # Get the next page button of the site 
    def get_next_btn(self):
        try:
            page_btns = self.browser.find_elements(By.XPATH, '//ul[contains(@class, "css-1g90gv6")]//li[contains(@class, "css-227srf")]')
            return page_btns[-1]
        except NoSuchElementException:
            page_btns = WebDriverWait(self.browser, randint(5, 10)).until(EC.presence_of_all_elements_located(By.XPATH, '//ul[contains(@class, "css-1g90gv6")]//li[contains(@class, "css-227srf")]'))
            return page_btns[-1]