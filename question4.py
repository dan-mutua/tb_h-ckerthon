from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def googleSearch():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://google.com")
        
        time.sleep(3)
        
        search_box = driver.find_element(By.CLASS_NAME, "gLFyf")
        
        search_box.send_keys("Test Automation")
        search_box.send_keys(Keys.ENTER)
        
        time.sleep(3)

        assert.
    finally:
        driver.quit()


if __name__ == "__main__":
    googleSearch()
        
  