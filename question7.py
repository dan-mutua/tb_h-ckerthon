from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

product_url = "https://www.amazon.com/SteelSeries-Aerox-Wireless-Lightweight-Ultra-lightweight-Resistant/dp/B09VP2NV53/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&dib=eyJ2IjoiMSJ9.9XfPEvr2PmqaFuBd8WdE3Yy8PiQFA-ET5_XBco_SUAobUPXFWOcF76X039y7CXgL3FvYwOQ5lEygYimagdKXgip8exkF3kQ9aW6qq_lZuIjJtYaf2TaUHrUQkjxx3vc7-fklw_Od8T2GLwicac5qe6iGHaJCSRPqR0vqpoXYgDmodYMVlBokyP8wVCXH7ZPxDWmQjynU4g8UqYqte2dB1dImb02Q-ZH13Oc14NRPOxM.6iWD8G1hj4633eP1NE8p89euQbHvBdRSvslOKWq1KMA&dib_tag=se&keywords=gaming+mouse&pd_rd_r=58efcb50-cc98-461a-8b37-10b479494ba3&pd_rd_w=hnxpk&pd_rd_wg=L9jfm&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=WFZK1GBDKH70VT8KT69R&qid=1723285745&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

def main(driver, wait):
  
    try:
        driver.get(product_url)

        try:
            cookie = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='accept-cookie-button']")))
            cookie.click()
        except (NoSuchElementException, TimeoutException):
            pass  

        add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart-button")))
        add_to_cart.click()

        wait.until(EC.presence_of_element_located((By.ID, "hlb-view-cart")))

        checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#hlb-view-cart-btn")))
        checkout.click()

        print("Successfully added item to cart and proceeded to checkout (simulated).")
        return True

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error encountered: {e}")
        return False

if __name__ == "__main__":
    driver = webdriver.Chrome("C:\Users\danmu\Downloads\chromedriver-win64")
    driver.implicitly_wait(10)  

    wait = WebDriverWait(driver, 10)

    success = main(driver, wait)

    if not success:
        print("Something went wrong.")

    driver.quit()