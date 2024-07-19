def test_sql_injection(setup, base_url, xss_script, password):
    page = setup
    page.goto(f"{base_url}/#/login")

    email_input = page.locator("#email")
    password_input = page.locator("#password")

    email_input.fill(xss_script)
    password_input.fill(password)

    login_button = page.wait_for_selector("#loginButton")
    assert login_button.is_enabled(), "Login button should be enabled"

    login_button.click()

    try:
        solved_challenge_message = page.wait_for_selector("xpath=//*[text()='You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.)']", timeout=10000)
        if solved_challenge_message:
            print("'Solved_Challenge_Message' is present")
            assert solved_challenge_message is not None, "'Solved_Challenge_Message' is not present"
        else:
            print("'Solved_Challenge_Message' is not present")
    except Exception as e:
        print("'Solved_Challenge_Message' is not present")