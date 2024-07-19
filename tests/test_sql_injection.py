def test_sql_injection(setup, base_url, sql_email, password):
    page = setup
    page.goto(f"{base_url}/#/login")

    email_input = page.locator("#email")
    password_input = page.locator("#password")

    email_input.fill(sql_email)
    password_input.fill(password)

    login_button = page.wait_for_selector("#loginButton")
    assert login_button.is_enabled(), "Login button should be enabled"

    login_button.click()

    your_basket_span = page.wait_for_selector("xpath=//span[text()=' Your Basket']", timeout=10000)
    assert your_basket_span.is_visible(), "'Your Basket' span is not visible"
