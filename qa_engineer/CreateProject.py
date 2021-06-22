from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, SessionNotCreatedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
import random
import requests
import time

URL = "https://www.d3a.io/login"
result_str = ''.join(random.choice('abcdefgh12345') for i in range(5))
project_name = "Test" + result_str
description = "Add some description" + result_str

def url_ok(url):
    r = requests.head(url)
    return r.status_code == 200

class CreateProject(unittest.TestCase):
    def ApplicationStart(self):
        try:
            url_ok(URL)
        except requests.exceptions.ConnectionError:
            print(f"URL {URL} not reachable")
        self.driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
        self.driver.get(URL)
        self.driver.maximize_window()
        delay = 3
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        return self.driver

    def LoginApp(self):
        self.driver = CreateProject.ApplicationStart()
        assert self.driver.find_element_by_tag_name('h2').text == 'Login'
        self.driver.find_element_by_id("email").send_keys("darshancbeceng@gmail.com")
        self.driver.find_element_by_id("password").send_keys("**qwER1234##")
        self.driver.find_element_by_xpath("//button[span[text() = 'Login']]").click()
        try:
            assert self.driver.find_element_by_tag_name('h1').text == 'Home'
            print("Home page is loaded successfully")
        except NoSuchElementException as e:
            print('No Such Element has occurred')
            pass
        try:
            assert self.driver.find_element_by_xpath('').text == 'Home'
            print("Home page is loaded successfully")
        except NoSuchElementException as e:
            print(e.msg)
            pass
        return self.driver

    def projectcreate(self):
        self.driver = CreateProject.LoginApp()
        try:
            assert self.driver.find_element_by_tag_name('h2').text == 'Login'
        except NoSuchElementException as e:
            print(e.msg)
        self.driver.find_element_by_id("email").send_keys("darshancbeceng@gmail.com")
        self.driver.find_element_by_id("password").send_keys("**qwER1234##")
        self.driver.find_element_by_xpath("//button[span[text() = 'Login']]").click()
        delay = 10
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        try:
            assert self.driver.find_element_by_tag_name('h1').text == 'Home'
            print("Home page is loaded successfully")
        except NoSuchElementException as e:
            print('No Such Element has occurred')
            pass
        self.driver.find_element_by_xpath("//*[contains(@class,'icon-projects ')]").click()
        self.driver.find_element_by_xpath("//button[span[text() = 'new project']]").click()
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
            print("New Project Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
        try:
            time.sleep(10)
            assert self.driver.find_element_by_xpath(
                "//div[@class='library-name-modal__container']/h3[text()='New Project']").text == 'New Project'
            print("New project window is visible")
        except NoSuchElementException as e:
            print('New Project is not visible')
            pass
        self.driver.find_element_by_xpath("//*[@id='input-field-name']").send_keys(project_name)
        self.driver.find_element_by_xpath("//*[@id='textarea-field-nameTextArea']").send_keys(description)
        self.driver.find_element_by_xpath("//button[span[text() = 'Add']]").click()
        # Validation of project creation
        self.driver.refresh()
        time.sleep(5)
        try:
            assert self.driver.find_element_by_xpath("//span[text() = '" + project_name + "']").text == project_name
            print("Project is created Successfully")
        except NoSuchElementException as e:
            print('Project is not created')
            pass
        try:
            assert self.driver.find_element_by_xpath("//p[text() ='" + description + "']").text == description
            print("Description of the project is listed")
        except NoSuchElementException as e:
            print('Discription is not found')


if __name__ == "__main__":
    unittest.main()