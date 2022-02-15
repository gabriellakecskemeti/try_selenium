import time

import pytest as pytest

from selenium.webdriver.support.expected_conditions import presence_of_element_located

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="module")
def chrome_driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    settings = webdriver.ChromeOptions()
    settings.add_argument("--incognito")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=settings)
    print(f"driver:{driver.name}")
    yield driver

    driver.quit()


def test_using_chrome_driver(chrome_driver):
    url = "https://www.gutekueche.at/"
    print(chrome_driver.name)
    chrome_driver.get(url)

    try:
        # Wait for the cookie banner to appear and click the accept button
        expectation = presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        print(expectation)
        # Try all 500 milliseconds if expectation is fulfilled, timeout after 10 seconds
        element = WebDriverWait(chrome_driver, 10).until(expectation)
        element.click()

    finally:

        search_element = chrome_driver.find_element(By.CSS_SELECTOR, "input[type=search]")
        search_text = "Fenchel"
        search_element.send_keys(search_text)

        submit = chrome_driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
        submit.click()

        result_is_present = presence_of_element_located((By.CSS_SELECTOR, "#main h1"))
        # Try all 500 milliseconds if expectation is fulfilled, timeout after 10 seconds
        result_header_element = WebDriverWait(chrome_driver, 10).until(result_is_present)
        print(result_header_element.text)
        assert result_header_element.text == f'SUCHERGEBNIS FÜR "{search_text.upper()}"'
    # time.sleep(10)
    # driver.quit()


test_using_chrome_driver(chrome_driver)
