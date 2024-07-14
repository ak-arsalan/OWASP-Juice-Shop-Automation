from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sql_injection(driver, base_url, sql_email, password):
    
    driver.get(f"{base_url}/#/login") 
    dismiss_buttons = driver.find_elements(By.XPATH, "//*[text()='Dismiss']")
    if dismiss_buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']"))
        ).click()

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys(sql_email)
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.ID, "loginButton")
    assert login_button.is_enabled(), "Login button should be enabled"

    login_button.click()
    
    successfully_login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = ' Your Basket']")))
    assert successfully_login is not None, "'Cart' is not present"
