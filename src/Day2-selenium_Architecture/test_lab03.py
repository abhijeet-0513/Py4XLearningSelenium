from selenium import webdriver

def test_vwo_login():
    driver = webdriver.Chrome()
    driver.get('https://app.vwo.com') # loads the webpage in current browser session
    title=driver.title
    page_source_data=driver.page_source
    url=driver.current_url
    print(title,url)
    # print(page_source_data)