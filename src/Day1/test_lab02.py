from selenium import webdriver
def test_open_vwo_login():
    driver = webdriver.Chrome()
    # POST request to create a new fresh copy of chrome
    # fresh - chrome(browser) - sessionId - 7474hf744-7384fud-3hfffe4849

    driver.get('https://app.vwo.com')
    # code -> HTTP request - chromeDriver(selenium Manager) -> chrome(sessionId)

    print(driver.title)
    assert driver.title == 'Login - VWO'
    driver.quit()