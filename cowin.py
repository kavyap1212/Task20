from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

# Open the desired webpage
driver.get('https://www.cowin.gov.in/')

# Wait for the page to load
time.sleep(8)

# Find and click on the "FAQ" and "Partners" anchor tags
faq_link = driver.find_element(By.XPATH, "//a[@href='/faq']")
partners_link = driver.find_element(By.XPATH, "//a[@href='/our-partner']")

# Open the links in new windows
faq_link.send_keys(Keys.CONTROL + Keys.ENTER)
partners_link.send_keys(Keys.CONTROL + Keys.ENTER)

# Wait for the new windows to open
time.sleep(5)

# Get the window handles
windows = driver.window_handles

# Display the window handles
print("Window handles:", windows)

# Switch to the first new window (FAQ) and close it
driver.switch_to.window(windows[1])
print("Switched to FAQ window with handle:", windows[1])
driver.close()

# Switch to the second new window (Partners) and close it
driver.switch_to.window(windows[2])
print("Switched to Partners window with handle:", windows[2])
driver.close()

# Switch back to the main window (home page)
driver.switch_to.window(windows[0])
print("Switched back to home window with handle:", windows[0])

# Close the WebDriver
driver.quit()