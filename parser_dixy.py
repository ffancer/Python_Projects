# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import chromedriver_binary
#
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get('https://dixy.ru/catalog/')
# time.sleep(2)
#
# def select_town():
#     search_button = browser.find_element(By.CLASS_NAME, 'current-city')
#     search_button.click()
#     time.sleep(1)
#     search_button.click()
#     time.sleep(3)
#     search_button2 = browser.find_element(By.XPATH, '/html/body/header/div/div/ul[1]/li[1]/div/div[3]/div/ul/li[4]/a')
#     search_button2.click()
#
#
# select_town()
# time.sleep(500)
# browser.close()


with open('dixy.html', encoding='utf-8') as file:
    src = file.read()

print(src)