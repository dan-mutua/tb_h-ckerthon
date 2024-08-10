from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def userLogIn():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("mysite.com")
        
        time.sleep(3)

        username_box = driver.find_element(By.ID, 'username')
        username_box.send_keys('admin')

        password_box = driver.find_element(By.ID, 'password')
        password_box.send_keys('admin2020')

        login = driver.find_element_by_id("login")
        login.click()

        time.sleep(3)
        assert 'Homepage' in driver.title



        
        
    finally:
        driver.quit()


if __name__ == "__main__":
    userLogIn()