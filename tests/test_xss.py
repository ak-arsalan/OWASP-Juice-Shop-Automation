from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_sql_injection(driver):
    driver.get("http://localhost:3000/#/login") 

    email_input = driver.find_element(By.ID, "email")
    password_input = driver.find_element(By.ID, "password")

    email_input.send_keys("<script>alert('XSS')</script>")
    password_input.send_keys("admin")
    
    login_button = driver.find_element(By.ID, "loginButton")
    assert login_button.is_enabled(), "Login button should be enabled"

    login_button.click()
    
    solved_challenge_message = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[text() = 'You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.)']")))
    assert solved_challenge_message is not None, "'Solved_Challenge_Message' is not present"