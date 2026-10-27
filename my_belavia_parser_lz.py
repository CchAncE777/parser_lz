import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Belavia_parser:

    def __init__(self, link_parser, link_email):
        self._link_parser = link_parser
        self._link_email = link_email
        self._driver = webdriver.Chrome()
        self._wait_driver = WebDriverWait(self._driver, 30)

    def get_our_tickets(self):
        pass

    def registrations_on_Belavia_with_mail(self):
        driver = self._driver
        driver.get(self._link_parser)

        acc_login = self._wait_driver(EC.visibility_of_element_located(
                                      By.XPATH, '//*[@id="mui-3"]'
                                      ))
        acc_login.clear()
        acc_login.send_keys('Почта')

        button = self._wait_driver(EC.element_to_be_clickable(
                                   By.CSS_SELECTOR, '#root > div.loginWrapper-3gPwb > div > form > div > div.button_wrapper-2wxuz.button_wrapper-3pJMZ > button'
                                   ))
        button.click()

    def get_our_code_registrations(self):
        driver_mail = self._driver
        driver_mail.get(self._link_email)
        time.sleep(5)

        acc_mail_login = driver_mail.find_element(By.CSS_SELECTOR, 'input[type="email"]')
        acc_mail_login.clear()
        acc_mail_login.send_keys('login')
        time.sleep(2)

        acc_mail_password = driver_mail.find_element(By.CSS_SELECTOR, 'input[type="password"]')
        acc_mail_password.clear()
        acc_mail_password.send_keys('password')
        time.sleep(2)

        button_mail = driver_mail.find_element(By.XPATH, '//*[@id="login-view"]/div[2]/div/div[1]/div[1]/form/div[4]/button')
        button_mail.click()
        time.sleep(5)

        first_message = driver_mail.find_element(By.CSS_SELECTOR, '#mail > div > div.flex.col.flex-grow > div > div:nth-child(1) > div.list-column.flex.col.fill-absolute > div.flex-grow.rel > div > div > div > div.rel.flex-grow > div > ul > li:nth-child(14)')
        first_message.click()
        time.sleep(2)

        our_code = (driver_mail.find_element(By.XPATH, '//*[@id="shadow-mail-body"]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[1]/td/table/tbody/tr[6]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td/p')).text
        driver_mail.close()
        return our_code
