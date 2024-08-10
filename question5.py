from ssl import Options
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.common.exceptions import NoSuchElementException



username = "admin"
password = "admin2020"

options = Options()


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("app_id")

try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    username.send_keys(username)

    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "pass"))
    )
    password.send_keys(password)

    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "login"))
    )
    login_button.click()

   
    try:
        my_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "homepage"))
        )
        print("Login successful!")
    except TimeoutException:
        print("Failed to find verification element on homepage")

        time.sleep(3)


    settings_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "settings"))
    )
    settings_button.click()

    

except NoSuchElementException as e:
    print(f"Error: {e}. Element not found.")
except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    driver.quit()
