from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('window-size=720,1080')
    # service = Service(executable_path='/home/eugeny/Downloads/chromedriver')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


