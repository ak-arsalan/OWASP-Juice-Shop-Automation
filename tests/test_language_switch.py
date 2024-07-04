from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_language_switch(driver):
    
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']")))
    driver.find_element(By.XPATH, "//*[text()='Dismiss']").click()

    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()=' language ']")))
    driver.find_element(By.XPATH, "//*[text()=' language ']").click()

    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()=' Deutsch ']")))
    driver.find_element(By.XPATH, "//*[text()=' Deutsch ']").click()

    alle_produkte_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[text()='Alle Produkte']")))
    assert alle_produkte_element is not None, "'Alle Produkte' is not present"

    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label , 'Sidenav')]")))
    driver.find_element(By.XPATH, "//button[contains(@aria-label , 'Sidenav')]").click()

    sidenav_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = ' Kundenfeedback ']")))
    assert sidenav_element is not None, "'Alle Produkte' is not present"