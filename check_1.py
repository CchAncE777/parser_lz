import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://belavia.by/account/#/account')

time.sleep(5)

acc_login = driver.find_element(By.XPATH, '//*[@id="mui-3"]')
acc_login.clear()
acc_login.send_keys('Почта')
time.sleep(5)

button = driver.find_element(By.CSS_SELECTOR, '#root > div.loginWrapper-3gPwb > div > form > div > div.button_wrapper-2wxuz.button_wrapper-3pJMZ > button')
button.click()
time.sleep(50)

# driver_mail = webdriver.Chrome()
# driver_mail.get('https://app.tuta.com/login')
# time.sleep(5)

# acc_mail_login = driver_mail.find_element(By.CSS_SELECTOR, 'input[type="email"]')
# acc_mail_login.clear()
# acc_mail_login.send_keys('login')
# time.sleep(2)

# acc_mail_password = driver_mail.find_element(By.CSS_SELECTOR, 'input[type="password"]')
# acc_mail_password.clear()
# acc_mail_password.send_keys('password')
# time.sleep(2)

# button_mail = driver_mail.find_element(By.XPATH, '//*[@id="login-view"]/div[2]/div/div[1]/div[1]/form/div[4]/button')
# button_mail.click()
# time.sleep(5)

# first_message = driver_mail.find_element(By.CSS_SELECTOR, '#mail > div > div.flex.col.flex-grow > div > div:nth-child(1) > div.list-column.flex.col.fill-absolute > div.flex-grow.rel > div > div > div > div.rel.flex-grow > div > ul > li:nth-child(14)')
# first_message.click()
# time.sleep(2)

# our_code = (driver_mail.find_element(By.XPATH, '//*[@id="shadow-mail-body"]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/p')).text
# driver_mail.close()

# acc_accept = driver.find_element(By.XPATH, '//*[@id="mui-6"]')
# acc_accept.clear()
# acc_accept.send_keys(our_code)
# time.sleep(2)

# button = driver.find_element(By.CSS_SELECTOR, '//*[@id="root"]/div[2]/div/form/div/div[2]/button')
# button.click()
# time.sleep(5)

button_find_road = driver.find_element(By.XPATH, "//button[contains(text(), 'Искать рейсы')]")
button_find_road.click()
time.sleep(8)

our_place_shipments_input = driver.find_element(By.XPATH, "//input[@placeholder='Откуда']")
our_place_shipments_input.click()
time.sleep(2)

our_place_shipments = driver.find_element(By.CSS_SELECTOR, 'input[data-city="Минск"]')
our_place_shipments.click()
time.sleep(2)

our_place_arrival_input = driver.find_element(By.XPATH, "//input[@placeholder='Куда']")
our_place_arrival_input.click()
time.sleep(1000)

our_place_arrival = driver.find_element(By.CSS_SELECTOR, 'input[data-city="Пекин"]')


driver.quit()



#66 дней