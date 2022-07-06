from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Firefox(executable_path="C:\\Users\\AllOneNeon\\Python\\Testovoe_A1\\geckodriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.a1.by/ru/c/shop")

buttons = driver.find_element(By.XPATH, '/html/body/main/div[10]/div[2]/div/button').click()
buttons = driver.find_elements(By.XPATH, '//*[@id="promo-product-button_0"]')
button = random.choice(buttons)
button.click()

driver.find_element(By.XPATH, '//*[@id="CURRENT_CONTRACT"]/div[1]/div[1]/div/label/span[1]/span[1]/span').click()
driver.find_element(By.XPATH, '//*[@id="select2-priceBlock_selector_CURRENT_CONTRACT-results"]/li[3]').click()

title = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[2]/div/div/div/div/span[2]/h1').text
price = driver.find_element(By.XPATH, '//*[@id="CURRENT_CONTRACT"]/div[1]/div[1]/div/label/span[1]/span[1]/span/span[1]').text

driver.find_element(By.XPATH, '//*[@id="CURRENT_CONTRACT"]/div[1]/div[2]/div[3]/form/div[2]/div/button').click()

print(f"Выбран {title}, вариант оплаты: {price}.")
driver.quit()