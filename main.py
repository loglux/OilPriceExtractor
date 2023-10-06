from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options  # Import Options class


class OilPriceExtractor:
    def __init__(self, url, headless=True):
        self.url = url
        chrome_options = Options()  # Instantiate Options class
        if headless:
            chrome_options.add_argument("--headless")  # Add headless argument
        self.driver = webdriver.Chrome(options=chrome_options)

    def extract_prices(self):
        self.driver.get(self.url)
        prices = {}
        for i in range(1, len(Select(self.driver.find_element(By.ID, 'litres')).options)):  # Updated loop condition
            dropdown = Select(self.driver.find_element(By.ID, 'litres'))  # Re-locate dropdown on each iteration
            option_text = dropdown.options[i].text
            dropdown.select_by_visible_text(option_text)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.woocommerce-Price-amount.amount'))
            )
            price = self.driver.find_element(By.CSS_SELECTOR, '.woocommerce-Price-amount.amount').text
            prices[option_text] = price
        return prices

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    extractor = OilPriceExtractor('https://deandrews.co.uk/product/home-heating-oil/', headless=True)
    prices = extractor.extract_prices()
    extractor.close()
    for litres, price in prices.items():
        print(f'{litres} litres: {price}')
