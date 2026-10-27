from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Parser_Belavia:
    def __init__(self, link):
        self._link = link
        self._driver = webdriver.Chrome()
        self._driver.get(self._link)
        self._wait = WebDriverWait(self._driver, 10)

    def accept_cookie(self):
        accept_cookie_button = self._wait.until(
                EC.element_to_be_clickable((By.ID, "submit_personal"))
                )
        accept_cookie_button.click()

    def click_next_day(self):
        next_day_button = self._wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-week-calendar-day-index='4']"
                )))
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_day_button)
        actions = ActionChains(self._driver)
        actions.move_to_element(next_day_button).click().perform()

    def get_info(self):
        elements = self._driver.find_elements(By.CSS_SELECTOR, '[data-test-id="flight"]')
        for element in elements:
            yield element.text.split('\n')

    def one_road(self, ticket):
        return { 
            'Дата вылета': ticket[0],
            'Компания': ticket[1],
            'Время вылета': ticket[2],
            'Время полета': ticket[3],
            'Время прилета': ticket[4],
            'Город вылета': ticket[5],
            'Город прилета': ticket[7],
            'Цена': ticket[10] + ' ' + ticket[11] + 'бел. рублей'
        }

    def two_roads(self, ticket):
        return { 
            'Дата вылета': ticket[0],
            'Компания': ticket[1] + ' + ' + ticket[11],
            'Время вылета': ticket[2],
            'Время полета': ticket[3] + ' + ' + ticket[12],
            'Время прилета': ticket[14],
            'Город вылета': ticket[5],
            'Город прилета': ticket[17],
            'Цена': ticket[-4] + ' ' + ticket[-3] + 'бел. рублей'
        }