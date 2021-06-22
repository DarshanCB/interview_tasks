# This is a sample Python script
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
import requests
import random
import json
import time

URL = "https://www.d3a.io/login"
result_str = ''.join(random.choice('abcdefgh12345') for i in range(5))
project_name = "Test" + result_str
description = "Add some description" + result_str


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def url_ok(url):
    r = requests.head(url)
    return r.status_code == 200

def getwebdriver(URL):
    try:
        url_ok(URL)
    except requests.exceptions.ConnectionError:
        print(f"URL {URL} not reachable")
    driver =  webdriver.Chrome(executable_path= ChromeDriverManager().install())
    driver.get(URL)
    driver.maximize_window()
    delay = 3
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"
    return driver

def loginpage():
    """Login page validation in order to fill in the email and passowrd"""
    driver = getwebdriver(URL)
    assert driver.find_element_by_tag_name('h2').text == 'Login'
    driver.find_element_by_id("email").send_keys("darshancbeceng@gmail.com")
    driver.find_element_by_id("password").send_keys("**qwER1234##")
    driver.find_element_by_xpath("//button[span[text() = 'Login']]").click()
    try:
        assert driver.find_element_by_tag_name('h1').text == 'Home'
        print("Home page is loaded successfully")
    except NoSuchElementException as e:
        print(e.msg)
        pass
    try:
        assert driver.find_element_by_xpath("//*[contains(@class,'icon-projects ')]").click()
        time.sleep()
        print("Home page is loaded successfully")
    except NoSuchElementException as e:
        print(e.msg)


def newproject():
    """New project is created in order to list the project in new project region"""
    driver = getwebdriver(URL)
    assert driver.find_element_by_tag_name('h2').text == 'Login'
    driver.find_element_by_id("email").send_keys("darshancbeceng@gmail.com")
    driver.find_element_by_id("password").send_keys("**qwER1234##")
    driver.find_element_by_xpath("//button[span[text() = 'Login']]").click()
    delay = 10
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        print
        "Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"
    try:
        assert driver.find_element_by_tag_name('h1').text == 'Home'
        print
        "Home page is loaded successfully"
    except NoSuchElementException as e:
        print('No Such Element has occurred')
        pass
    driver.find_element_by_xpath("//*[contains(@class,'icon-projects ')]").click()
    driver.find_element_by_xpath("//button[span[text() = 'new project']]").click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        print
        "New Project Page is ready!"
    except TimeoutException:
        print
        "Loading took too much time!"
        pass
    try:
        time.sleep(10)
        assert driver.find_element_by_xpath("//div[@class='library-name-modal__container']/h3[text()='New Project']").text == 'New Project'
        print
        "New project window is visible"
        pass
    except NoSuchElementException as e:
        print('New Project is not visible')
        pass
    driver.find_element_by_xpath("//*[@id='input-field-name']").send_keys(project_name)
    driver.find_element_by_xpath("//*[@id='textarea-field-nameTextArea']").send_keys(description)
    driver.find_element_by_xpath("//button[span[text() = 'Add']]").click()
    #Validation of project creation
    driver.refresh()
    time.sleep(5)
    try:
        assert driver.find_element_by_xpath("//span[text() = '" + project_name + "']").text == project_name
        print("Project is created Successfully")
    except NoSuchElementException as e:
        print('Project is not created')
        pass
    try:
        assert driver.find_element_by_xpath("//p[text() ='" + description + "']").text == description
        print("Description of the project is listed")
    except NoSuchElementException as e:
        print('Discription is not found')
        pass
    simvalidation(driver)


def simvalidation(driver):
    """Created projects need to be validated accordingly and create a new simulation"""
    driver.refresh()
    time.sleep(5)
    try:
        assert driver.find_element_by_xpath("//span[text() = '" + project_name + "']").text == project_name
        print("Project is created Successfully")
    except NoSuchElementException as e:
        print('Project is not created')
        pass
    try:
        assert driver.find_element_by_xpath("//p[text() ='" + description + "']").text == description
        print("Description of the project is listed")
    except NoSuchElementException as e:
        print('Discription is not found')
        pass
    driver.find_element_by_xpath("//span[text() = '" + project_name + "']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//span[text() = 'new simulation']").click()
    try:
        assert driver.find_element_by_tag_name('h1').text == 'New Simulation'
        print("New simulation page is loaded successfully")
    except NoSuchElementException as e:
        print(e.msg)
        pass
    time.sleep(5)
    driver.find_element_by_id("input-field-name").clear()
    driver.find_element_by_id("input-field-name").send_keys(project_name)
    try:
        assert driver.find_element_by_xpath("//span[text() = 'Description']").text == "Description"
        print("Description is found")
    except NoSuchElementException as e:
        print(e.msg)
        pass
    driver.find_element_by_id("textarea-field-description").send_keys(description)
    checkprj = driver.find_element_by_xpath("//select[@name='projectUUID']").text
    try:
        assert checkprj == project_name
    except Exception:
        print("Project not found in simulation")
    driver.find_element_by_xpath("//button[span[text() = 'Next']]").click()
    time.sleep(5)
    try:
        assert driver.find_element_by_tag_name('h1').text == 'Modelling'
        print("Modelling page is loaded successfully")
    except NoSuchElementException as e:
        print(e.msg)
        pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    newproject()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
