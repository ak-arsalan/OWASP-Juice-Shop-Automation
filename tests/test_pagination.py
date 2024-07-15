from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pagination(driver):

    #Scenario 1

    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-grid-tile.ng-star-inserted")))
    count = len(elements)
    print(f"Count of Items with filter of 12 is : {count}")
    assert count == 12

    #Scenario 2
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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
    assert count == 24

    #Scenario 3
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = '24']")))
    driver.find_element(By.XPATH, "//*[text() = '24']").click()

    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text() = ' 36 ']")))
    driver.find_element(By.XPATH, "//*[text() = ' 36 ']").click()

    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "mat-grid-tile.ng-star-inserted")))

    count = len(elements)
    print(f"Count of Items with filter of 35 is : {count}")
    assert count == 35
