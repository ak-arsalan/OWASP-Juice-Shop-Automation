import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:3000"

@pytest.fixture(scope="module")
def driver(base_url):

    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(base_url)

    dismiss_buttons = driver.find_elements(By.XPATH, "//*[text()='Dismiss']")
    if dismiss_buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[text()='Dismiss']"))
        ).click()

    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def invalid_email():
    return os.getenv("INVALID_EMAIL")

@pytest.fixture(scope="session")
def invalid_password():
    return os.getenv("INVALID_PASSWORD")

@pytest.fixture(scope="session")
def email():
    return os.getenv("EMAIL")

@pytest.fixture(scope="session")
def password():
    return os.getenv("PASSWORD")

@pytest.fixture(scope="session")
def sql_email():
    return os.getenv("SQL_EMAIL")

@pytest.fixture(scope="session")
def xss_script():
    return os.getenv("XSS_SCRIPT")