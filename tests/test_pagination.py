def test_pagination(setup, base_url):

    page = setup
    page.goto(f"{base_url}/#/")

    # Scenario 1
    elements = page.wait_for_selector(".mat-grid-tile.ng-star-inserted", state='visible', timeout=10000)
    count = len(page.query_selector_all(".mat-grid-tile.ng-star-inserted"))
    print(f"Count of Items with filter of 12 is : {count}")
    assert count == 12

    # Scenario 2
    page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    
    me_want_it_button = page.wait_for_selector("xpath=//*[text()='Me want it!']", timeout=10000)
    me_want_it_button.click()

    filter_12_button = page.wait_for_selector("xpath=//*[text()='12']", timeout=10000)
    filter_12_button.click()

    filter_24_button = page.wait_for_selector("xpath=//*[text()=' 24 ']", timeout=10000)
    filter_24_button.click()

    elements = page.wait_for_selector(".mat-grid-tile.ng-star-inserted", state='visible', timeout=10000)
    count = len(page.query_selector_all(".mat-grid-tile.ng-star-inserted"))
    print(f"Count of Items with filter of 24 is : {count}")
    assert count == 24

    # Scenario 3
    page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
    
    filter_24_button = page.wait_for_selector("xpath=//*[text()='24']", timeout=10000)
    filter_24_button.click()

    filter_36_button = page.wait_for_selector("xpath=//*[text()=' 36 ']", timeout=10000)
    filter_36_button.click()

    elements = page.wait_for_selector(".mat-grid-tile.ng-star-inserted", state='visible', timeout=10000)
    count = len(page.query_selector_all(".mat-grid-tile.ng-star-inserted"))
    print(f"Count of Items with filter of 36 is : {count}")
    assert count == 35
