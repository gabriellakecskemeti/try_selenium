import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

driver_path = "C:/Users/compi_000/.wdm/drivers/chromedriver/win32/98.0.4758.80/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
option = webdriver.ChromeOptions()
option.binary_location = brave_path

service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.utils import ChromeType

# browser = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser = webdriver.Chrome(service=service, options=option)

# Navigate browser to given URL
url = "https://www.python.org/"
browser.get(url)
# Wait for 5 seconds
time.sleep(5)
# Close all opened browser windows and terminate the driver
browser.quit()


