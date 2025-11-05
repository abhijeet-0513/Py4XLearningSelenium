from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(chrome_options)
    driver.get('https://app.vwo.com')
    # open chrome in incognito mode
    assert True ==False

    # stop python interpreter for 10 sec
    # time.sleep(10)