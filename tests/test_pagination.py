from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pagination(driver):
    #Scenario 1
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']")))
    driver.find_element(By.XPATH, "//*[text()='Dismiss']").click()

    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-grid-tile.ng-star-inserted")))
    count = len(elements)
    print(f"Count of Items with filter of 12 is : {count}")

    #Scenario 2
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = 'Me want it!']")))
    driver.find_element(By.XPATH, "//*[text() = 'Me want it!']").click()

    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = '12']")))
    driver.find_element(By.XPATH, "//*[text() = '12']").click()

    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = ' 24 ']")))
    driver.find_element(By.XPATH, "//*[text() = ' 24 ']").click()

    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-grid-tile.ng-star-inserted")))
    
    count = len(elements)
    print(f"Count of Items with filter of 24 is : {count}")

    #Scenario 3
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = '24']")))
    driver.find_element(By.XPATH, "//*[text() = '24']").click()

    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = ' 36 ']")))
    driver.find_element(By.XPATH, "//*[text() = ' 36 ']").click()

    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-grid-tile.ng-star-inserted")))

    count = len(elements)
    print(f"Count of Items with filter of 36 is : {count}")
    driver.quit()