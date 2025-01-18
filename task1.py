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
    print("Видео открылось.")
except ElementClickInterceptedException:
    print("Не удалось кликнуть на видео, возможно оно заблокировано другим элементом.")


time.sleep(15)


driver.quit()
