from dotenv import load_dotenv
import os
import pytest
from selenium import webdriver

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:3000"

@pytest.fixture(scope="module")
def driver(base_url):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
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