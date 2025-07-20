import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

def startTesting():
    driver.get('https://courses-admin.neu.edu.vn')
    driver.maximize_window()
    driver.implicitly_wait(20)

def tapOutside():
    actions.move_by_offset(0, 0).perform()  # Move to a neutral position to tap outside
    driver.implicitly_wait(10)

    time.sleep(0.5)

def ensureVisible(element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def clickId(id):
    element = driver.find_element(By.ID, id)
    ensureVisible(element)
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def clickClass(className, index=0, last=True):
    element = driver.find_elements(By.CLASS_NAME, className)
    element = element[index] if last is False else element[-1]
    ensureVisible(element)
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def clickXPath(xpath):
    element = driver.find_element(By.XPATH, xpath)
    ensureVisible(element)
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def clickText(element, text, index=0, last=False):
    text = text.replace('"', '')
    element = driver.find_elements(By.XPATH, f"//{element}[contains(text(), '{text}')]")
    element = element[index] if last is False else element[-1]
    ensureVisible(element)
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def clickTextFieldCondition(element, field, text, index=0):
    text = text.replace('"', '')
    element = driver.find_elements(By.XPATH, f"//{element}[@{field}='{text}']")[index]
    ensureVisible(element)
    driver.execute_script("arguments[0].click();", element)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def inputText(placeholder, text, index=0):
    placeholder = placeholder.replace('"', '')
    text = text.replace('"', '')

    inputElement = driver.find_elements(By.XPATH, f"//input[@placeholder='{placeholder}']")[index]

    ensureVisible(inputElement)
    inputElement.send_keys(text)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def inputTextById(inputId, text, index=0):
    inputElement = driver.find_elements(By.ID, inputId)[index]
    ensureVisible(inputElement)
    inputElement.send_keys(text)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def inputTextByClass(className, text):
    inputElement = driver.find_element(By.CLASS_NAME, className)
    ensureVisible(inputElement)
    inputElement.send_keys(text)
    driver.implicitly_wait(10)

    time.sleep(0.5)

def expandDropdownById(id, index=0):
    dropdown = driver.find_elements(By.ID, id)[index]
    ensureVisible(dropdown)
    dropdown.click()
    driver.implicitly_wait(10)

    time.sleep(0.5)