from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By
import time

import pandas as pd
import openpyxl







def take_data(info):

    


    PATH= '/usr/lib/chromium-browser/chromedriver'
    link = f'https://api.mercadolibre.com/items/{info}?include_attributes=all'
    print(link)

    s= Service(PATH)
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Habilitar el modo sin cabeza
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Crear una instancia del controlador de Chrome con las opciones configuradas
    driver = webdriver.Chrome(options=chrome_options,service=s)
    
    driver.set_window_size(1366,768)

    driver.get(link)


    frame = driver. find_element(By.CSS_SELECTOR,'span.collapsible')

    tag = driver. find_elements(By.CSS_SELECTOR,'span.s2')[3]
    ActionChains(driver).scroll_to_element(tag).perform()

    try:
        wait = WebDriverWait(driver, 8)
        element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/categories/"]')))
    
        category_id = element.text.replace('"','')

    except:
        category_id= None
    print(category_id)

    driver.quit()
    return category_id