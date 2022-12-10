from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Дрова #
path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=ChromeService(path))

# URL #
url_list = "https://100realty.ua/realty_search/apartment/sale/cur_3"

# Пагинация #
for i in range(1, 50 + 1):
    adpageurl = 'https://100realty.ua/realty_search/apartment/sale/cur_3' + '?page=' + str(i)
    adpage = adpageurl
    driver.get(adpage)
    a_elements = driver.find_elements(By.CLASS_NAME, "image-field__link")
    for href in a_elements:
        print(href.get_attribute('href'))

