from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def test_chrome_url_verify():

    driver = webdriver.Chrome()
    driver.get('https://app.vwo.com')
    assert driver.current_url == 'https://app.vwo.com/#/login'
    # open chrome in incognito mode
    # assert True ==False

    # stop python interpreter for 10 sec
    # time.sleep(10)
    driver.quit()