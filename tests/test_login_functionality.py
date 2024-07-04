from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):
    driver.get("http://localhost:3000/#/login")
    assert driver.title == "OWASP Juice Shop"

    login_heading_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = 'Login']")))
    assert login_heading_element is not None, "'Login heading' is not present"

def test_initial_state_login_button_disabled(driver):
    driver.get("http://localhost:3000/#/login")  
    login_button = driver.find_element(By.ID, "loginButton")
    assert not login_button.is_enabled(), "Login button should be disabled initially"

def test_empty_fields_button_disabled(driver):
    driver.get("http://localhost:3000/#/login")

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("")
    password_input.send_keys("")

    login_button = driver.find_element(By.ID, "loginButton")
    assert not login_button.is_enabled(), "Login button should be disabled with empty fields"

def test_invalid_credentials(driver):
    driver.get("http://localhost:3000/#/login") 

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("invalid@gmail.com")
    password_input.send_keys("wrongpassword")

    login_button = driver.find_element(By.ID, "loginButton")

    assert login_button.is_enabled(), "Login button should be enabled with incorrect credentials"
    login_button.click()

    error_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = 'Invalid email or password.']")))
    assert error_message is not None, "'Error validation' is not present"

def test_valid_credentials_successful_login(driver):
    driver.refresh()
    driver.get("http://localhost:3000/#/login") 

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("admin@juice-sh.op")
    password_input.send_keys("admin123")
    
    login_button = driver.find_element(By.ID, "loginButton")
    assert login_button.is_enabled(), "Login button should be enabled with correct credentials"

    login_button.click()
    
    successfully_login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = ' Your Basket']")))
    assert successfully_login is not None, "'Cart' is not present"

