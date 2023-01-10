from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

import namegenerator

username = 'Admin'
password = 'admin123'
delay = 500
name = namegenerator.gen()

class Scenario:
    def __init__(self):    
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

    def login(self):
        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located(
            (By.XPATH, '//input[@name="username"]'))).send_keys(username)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def add(self):
        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located(
            (By.XPATH, '//span[text()="Admin"]'))).click()

        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"Job")]'))).click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Pay Grades")]').click()

        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Add")]'))).click()

        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input'))).send_keys(name)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Add")]'))).click()

        WebDriverWait(self.driver, delay).until(ec.presence_of_element_located(
            (By.XPATH, '//div[contains(text(),"-- Select --")]'))).click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"ALL - Albanian Lek"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div/div[2]/input').send_keys(1000)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[2]/div/div[2]/div/div[2]/input').send_keys(10000)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/form/div[3]/button[2]').click()

    def check(self):
        xpath_found_row = '//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "Ukraine Hryvnia")]'
        found_row = WebDriverWait(self.driver, delay).until(ec.presence_of_element_located(
            (By.XPATH, xpath_found_row)))

        found_row.find_element(By.XPATH, '//div[contains(., "Ukraine Hryvnia")]')
        found_row.find_element(By.XPATH, '//div[contains(., "1000")]')
        found_row.find_element(By.XPATH, '//div[contains(., "10000")]')

    def remove(self):
        xpath_delete = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{name}"' \
                       ', "Ukraine Hryvnia")]//i[@class="oxd-icon bi-trash"]'
        found_row = self.driver.find_element(By.XPATH, xpath_delete)
        found_row.find_element(By.XPATH, '//i[@class="oxd-icon bi-trash"]').click()
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()

        self.driver.close()
        
def main():
    test = Scenario()
    test.login()
    test.add()
    test.check()
    test.remove()


if __name__ == "__main__":
    main()
