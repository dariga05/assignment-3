from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
import time


driver = webdriver.Chrome()


driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()


actions = ActionChains(driver)

# 1: Mouse Hover to reveal hidden elements
print("Performing mouse hover...")
driver.get('https://the-internet.herokuapp.com/hovers')
hover_element = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/img')
actions.move_to_element(hover_element).perform()
time.sleep(2)  
print("Mouse hover completed.")

# 2: Drag and Drop
print("Performing drag and drop...")
driver.get('https://the-internet.herokuapp.com/drag_and_drop')
source_element = driver.find_element(By.ID, 'column-a')
target_element = driver.find_element(By.ID, 'column-b')
actions.drag_and_drop(source_element, target_element).perform()
time.sleep(2)  
print("Drag and drop completed.")

# 3: Right-click (context click) to open a context menu and handle the alert
print("Performing right-click...")
driver.get('https://the-internet.herokuapp.com/context_menu')
right_click_element = driver.find_element(By.ID, 'hot-spot')
actions.context_click(right_click_element).perform()
time.sleep(2) 

# Handle the alert
try:
    alert = driver.switch_to.alert
    alert.accept()
    print("Alert accepted.")
except UnexpectedAlertPresentException:
    print("No alert present")

# 4: Use keyboard events like pressing SHIFT while entering text
print("Performing keyboard events...")
driver.get('https://the-internet.herokuapp.com/key_presses')
input_element = driver.find_element(By.ID, 'target')
actions.click(input_element).key_down(Keys.SHIFT).send_keys('text in uppercase').key_up(Keys.SHIFT).perform()
time.sleep(2)  
print("Keyboard events completed.")

# 5: Perform shortcuts like CTRL+A and CTRL+C
print("Performing keyboard shortcuts...")
actions.click(input_element).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()  # Select all text
time.sleep(1)
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()  # Copy selected text
time.sleep(2)  
print("Keyboard shortcuts completed.")

# Close the browser
driver.quit()
print("Browser closed.")
