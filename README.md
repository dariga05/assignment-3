# 1. Selenium Automation - YouTube Search and Video Click Automation

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


#2. Selenium Automation - ActionChains and Keyboard Events#
This repository contains an automation script using Selenium WebDriver that demonstrates a variety of user actions, including mouse hover, drag and drop, right-click, and keyboard events.

Description
The script automates the process of:

Mouse Hover: Hovering over an image to reveal hidden elements.
Drag and Drop: Dragging an element from one location to another.
Right-Click: Right-clicking to open a context menu and handle the alert.
Keyboard Events: Simulating the pressing of the SHIFT key for uppercase text.
Keyboard Shortcuts: Using CTRL+A to select all text and CTRL+C to copy selected text.

## Code
```python
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

!Video Demonstration!
Click here to watch the video demonstration of the task
https://github.com/user-attachments/assets/0794ad10-acbc-4778-8415-79a4bd89d309






!3. Selenium Automation - Select Menu Interaction!
This repository contains an automation script using Selenium WebDriver that interacts with a dropdown menu and performs various selection actions such as single select, multi-select, and deselect options.

Description
The script automates the following actions:

Single Select: Select an option from a single-select dropdown by visible text.
Multi-Select: Select options from a multi-select dropdown by index and value, and then deselect one of the options.
View Selected Options: Display currently selected options in the multi-select dropdown.
Error Handling: Handles any unexpected errors during the execution.

Code

"from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Edge()

try:
    
    driver.get('https://demoqa.com/select-menu')
    driver.implicitly_wait(10)
    driver.maximize_window()

    time.sleep(2)

    # Single Select Dropdown
    dropdown_single = driver.find_element(By.ID, 'oldSelectMenu')
    select_single = Select(dropdown_single)
    select_single.select_by_visible_text('Black')
    print("Single select: Selected 'Black' by visible text")

    time.sleep(2)

    # Multi-Select Dropdown
    dropdown_multi = driver.find_element(By.ID, 'cars')
    select_multi = Select(dropdown_multi)

    select_multi.select_by_index(1)  # Selecting 'Saab'
    time.sleep(1)
    select_multi.select_by_value('audi')
    print("Multi-select: Selected options by index and value")

    time.sleep(2)

    # Display currently selected options
    selected_options = select_multi.all_selected_options
    print("Currently selected options:")
    for option in selected_options:
        print(f"- {option.text}")

    time.sleep(2)

    # Deselect option
    select_multi.deselect_by_index(1)
    print("Multi-select: Deselected option at index 1")

    time.sleep(2)

    # Display remaining selected options
    remaining_options = select_multi.all_selected_options
    print("Final selected options:")
    for option in remaining_options:
        print(f"Still selected: {option.text}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
   
    driver.quit()
    print("Browser closed.")"

!Video Demonstration!
Click here to watch the video demonstration of the task

https://github.com/user-attachments/assets/8ac8d1aa-f587-42fc-b190-6994694fd886




