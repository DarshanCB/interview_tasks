from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, SessionNotCreatedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver
import requests

URL = "https://www.d3a.io/login"

def url_ok(url):
    r = requests.head(url)
    return r.status_code == 200

class LoginPage(unittest.TestCase):
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
        self.driver = LoginPage.ApplicationStart()
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
            print('No Such Element has occurred')
            pass


if __name__ == "__main__":
    unittest.main()