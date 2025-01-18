# Selenium Automation - YouTube Search and Video Click Automation

This repository contains an automation script using **Selenium** to search for a "makeup tutorial" on **YouTube**, click on the first video, and handle potential errors during the process.

## Description
The script automates the process of:
1. Searching for a "makeup tutorial" on YouTube.
2. Clicking on the first video in the search results.
3. Handling potential errors such as `ElementClickInterceptedException` if the video is blocked by another element.

## Code
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.youtube.com")

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("makeup tutorial")
search_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 15)
results_container = wait.until(EC.visibility_of_element_located((By.ID, "contents")))

fluent_wait = WebDriverWait(driver, 30, poll_frequency=1)
first_video = fluent_wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, "ytd-video-renderer"))

driver.execute_script("arguments[0].scrollIntoView(true);", first_video)

try:
    driver.execute_script("arguments[0].click();", first_video)
    print("Video opened successfully.")
except ElementClickInterceptedException:
    print("Unable to click on the video, it may be blocked by another element.")

time.sleep(15)

driver.quit()


!Video Demonstration!
Click here to watch the video demonstration of the task
https://github.com/user-attachments/assets/434c5fc6-c348-4a08-b836-cdedac86fbea


