
def test_language_switch(setup, base_url):
    page = setup
    page.goto(f"{base_url}/#/")
    language_button = page.wait_for_selector("xpath=//*[text()=' language ']")
    language_button.click()

    deutsch_option = page.wait_for_selector("xpath=//*[text()=' Deutsch ']")
    deutsch_option.click()

    alle_produkte_element = page.wait_for_selector("xpath=//div[text()='Alle Produkte']")
    assert alle_produkte_element is not None, "'Alle Produkte' is not present"

    sidenav_button = page.wait_for_selector("xpath=//button[contains(@aria-label , 'Sidenav')]")
    sidenav_button.click()

    kundenfeedback_element = page.wait_for_selector("xpath=//*[text() = ' Kundenfeedback ']")
    assert kundenfeedback_element is not None, "'Kundenfeedback' is not present"
