import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

settings = webdriver.ChromeOptions()
settings.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=settings)

url = "file:///C:/Users/compi_000/PycharmProjects/try_selenium/example.html"
driver.get(url)


email_element = driver.find_element(By.CSS_SELECTOR, "input[type=email]")
email_element.send_keys("georg.mansky-kummert@fh-campuswien.ac.at")

select = Select(driver.find_element(By.ID, "title_field"))
select.select_by_value("mr")  # select mr
time.sleep(2)
select.select_by_index(2)  # select ms
time.sleep(2)
select.select_by_visible_text("Mister")

button_element = driver.find_element(By.ID, "button")
button_element.click()
button_element.click()
button_element.click()

time.sleep(1)

link_element1 = driver.find_element(By.ID, "python_link")
print(link_element1.get_attribute("href"))
link_element1.click()

time.sleep(5)

driver.quit()


