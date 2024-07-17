from playwright.sync_api import expect

def test_login(setup, base_url):
    page = setup
    page.goto(f"{base_url}/#/login")
    expect(page).to_have_title("OWASP Juice Shop")

    login_heading_element = page.locator("h1", has_text="Login")
    expect(login_heading_element).to_be_visible()
    assert login_heading_element.inner_text() == "Login", "'Login' heading text is incorrect"

def test_initial_state_login_button_disabled(setup, base_url):
    page = setup
    page.goto(f"{base_url}/#/login")

    login_button = page.locator("xpath=//button[@disabled = 'true']")
    assert login_button.is_visible(), "Login button should be disabled initially"

def test_empty_fields_button_disabled(setup, base_url):
    page = setup
    page.goto(f"{base_url}/#/login")

    email_input = page.locator("#email")
    password_input = page.locator("#password")

    email_input.fill("")
    password_input.fill("")

    login_button = page.locator("xpath=//button[@disabled = 'true']")
    assert login_button.is_visible(), "Login button should be disabled initially"

def test_invalid_credentials(setup, base_url, invalid_email, invalid_password):
    page = setup
    page.goto(f"{base_url}/#/login")

    email_input = page.locator("#email")
    password_input = page.locator("#password")

    email_input.fill(invalid_email)
    password_input.fill(invalid_password)

    login_button = page.wait_for_selector("#loginButton")
    assert login_button.is_enabled(), "Login button should be enabled"

    login_button.click()

    error_message = page.wait_for_selector("xpath=//div[@class='error ng-star-inserted' and text()='Invalid email or password.']", timeout=10000)
    assert error_message.is_visible(), "Error message 'Invalid email or password.' is not visible"

def test_valid_credentials_successful_login(setup, base_url, email, password):
    page = setup
    page.goto(f"{base_url}/#/login")

    email_input = page.locator("#email")
    password_input = page.locator("#password")

    email_input.fill(email)
    password_input.fill(password)

    login_button = page.wait_for_selector("#loginButton")
    assert login_button.is_enabled(), "Login button should be enabled"

    login_button.click()

    your_basket_span = page.wait_for_selector("xpath=//span[text()=' Your Basket']", timeout=10000)
    assert your_basket_span.is_visible(), "'Your Basket' span is not visible"
