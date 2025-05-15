from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

try:
    driver.get("http://<PRIVATE_IP_OR_DNS>")
    time.sleep(2)
    page_source = driver.page_source

    assert "Twinkle Twinkle Little Star" in page_source
    assert "How I wonder what you are" in page_source
    print("TEST PASSED: Expected content found.")
except AssertionError:
    print("TEST FAILED: Expected content not found.")
    exit(1)
finally:
    driver.quit()

