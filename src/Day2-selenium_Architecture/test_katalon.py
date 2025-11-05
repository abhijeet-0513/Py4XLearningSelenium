from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
def test_katalon_login():
    driver = webdriver.Chrome()
    driver.get('https://katalon-demo-cura.herokuapp.com')

    # find element by locator
    make_appointment_element=driver.find_element(By.ID, 'btn-make-appointment')
    make_appointment_element.click()
    assert driver.current_url == 'https://katalon-demo-cura.herokuapp.com/profile.php#login'

