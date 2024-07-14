from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(driver, base_url):
    driver.get(f"{base_url}/#/login")
    assert driver.title == "OWASP Juice Shop"

    dismiss_buttons = driver.find_elements(By.XPATH, "//*[text()='Dismiss']")
    if dismiss_buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']"))
        ).click()

    login_heading_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = 'Login']")))
    assert login_heading_element is not None, "'Login heading' is not present"

def test_initial_state_login_button_disabled(driver, base_url):
    driver.get(f"{base_url}/#/login")  

    dismiss_buttons = driver.find_elements(By.XPATH, "//*[text()='Dismiss']")
    if dismiss_buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']"))
        ).click()

    login_button = driver.find_element(By.ID, "loginButton")
    assert not login_button.is_enabled(), "Login button should be disabled initially"

def test_empty_fields_button_disabled(driver, base_url):
    driver.get(f"{base_url}/#/login")

    dismiss_buttons = driver.find_elements(By.XPATH, "//*[text()='Dismiss']")
    if dismiss_buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']"))
        ).click()

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("")
    password_input.send_keys("")

    login_button = driver.find_element(By.ID, "loginButton")
    assert not login_button.is_enabled(), "Login button should be disabled with empty fields"

def test_invalid_credentials(driver, base_url, invalid_email, invalid_password):
    driver.get(f"{base_url}/#/login") 

    dismiss_buttons = driver.find_elements(By.XPATH, "//*[text()='Dismiss']")
    if dismiss_buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']"))
        ).click()

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys(invalid_email)
    password_input.send_keys(invalid_password)

    login_button = driver.find_element(By.ID, "loginButton")

    assert login_button.is_enabled(), "Login button should be enabled with incorrect credentials"
    login_button.click()

    error_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = 'Invalid email or password.']")))
    assert error_message is not None, "'Error validation' is not present"

def test_valid_credentials_successful_login(driver, base_url, email, password):
    driver.refresh()
    driver.get(f"{base_url}/#/login") 

    dismiss_buttons = driver.find_elements(By.XPATH, "//*[text()='Dismiss']")
    if dismiss_buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']"))
        ).click()

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys(email)
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.ID, "loginButton")
    assert login_button.is_enabled(), "Login button should be enabled with correct credentials"

    login_button.click()
    
    successfully_login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = ' Your Basket']")))
    assert successfully_login is not None, "'Cart' is not present"

