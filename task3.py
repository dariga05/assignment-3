from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Edge()

try:
    
    driver.get('https://demoqa.com/select-menu')
    driver.implicitly_wait(10)
    driver.maximize_window()

    
    time.sleep(2)

   
    dropdown_single = driver.find_element(By.ID, 'oldSelectMenu')
    select_single = Select(dropdown_single)
    select_single.select_by_visible_text('Black')
    print("Single select: Selected 'Black' by visible text")

    
    time.sleep(2)

    
    dropdown_multi = driver.find_element(By.ID, 'cars')
    select_multi = Select(dropdown_multi)

   
    select_multi.select_by_index(1)  # Selecting 'Saab'
    time.sleep(1)
    select_multi.select_by_value('audi')
    print("Multi-select: Selected options by index and value")

   
    time.sleep(2)

    
    selected_options = select_multi.all_selected_options
    print("Currently selected options:")
    for option in selected_options:
        print(f"- {option.text}")

    
    time.sleep(2)

    
    select_multi.deselect_by_index(1)
    print("Multi-select: Deselected option at index 1")

    
    time.sleep(2)

    
    remaining_options = select_multi.all_selected_options
    print("Final selected options:")
    for option in remaining_options:
        print(f"Still selected: {option.text}")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
   
    driver.quit()
    print("Browser closed.")
