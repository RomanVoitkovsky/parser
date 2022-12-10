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
for i in range(1, 2 + 1):
    print('Parsing page # ' + str(i) + ' of ' + str(2))
    adpageurl = 'https://100realty.ua/realty_search/apartment/sale/cur_3' + '?page=' + str(i)
    adpage = adpageurl
    driver.get(adpage)
    a_elements = driver.find_elements(By.CLASS_NAME, "image-field__link")
    for href in a_elements:
        driver.get(href.get_attribute('href'))
        findphone = driver.find_elements(By.CLASS_NAME, "object-contacts-one-phone")
        for phone in findphone:
            driver.find_element(By.LINK_TEXT, "Показать телефон").click()
            print(phone.text)
            current_url = driver.current_url
            print(current_url)
