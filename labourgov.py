import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Create a folder to save photos
photos_folder = 'photo_gallery'
if not os.path.exists(photos_folder):
    os.makedirs(photos_folder)

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()

# Open the desired webpage
driver.get('https://labour.gov.in/')

# Wait for the page to load completely
time.sleep(5)


#1. Downloading the Monthly Progress Report

# Hover over the "Documents" dropdown menu
documents_menu = driver.find_element(By.XPATH, '//a[text()="Documents"]')
ActionChains(driver).move_to_element(documents_menu).perform()

# Wait for the dropdown menu to be displayed
time.sleep(2)

# Click on "Monthly Progress Report"
monthly_progress_report = driver.find_element(By.XPATH, '//a[text()="Monthly Progress Report"]')
monthly_progress_report.click()

# Wait for the Monthly Progress Report page to load
time.sleep(5)

# Find and download one of the Monthly Progress Reports
# Assuming there is a link to a PDF or other document format
# This xpath may need to be adjusted based on the actual page structure
report_link = driver.find_element(By.XPATH, '(//a[contains(text(), "Download")])[1]')
report_url = report_link.get_attribute('href')

# Download the report
response = requests.get(report_url)
with open("Monthly_Progress_Report.pdf", "wb") as file:
    file.write(response.content)

# 2. Download 10 photos from the "Photo Gallery" submenu under the "Media" menu
media_menu = driver.find_element(By.LINK_TEXT, 'Media')
ActionChains(driver).move_to_element(media_menu).perform()
time.sleep(2)
photo_gallery = driver.find_element(By.LINK_TEXT, 'Photo Gallery')
photo_gallery.click()
time.sleep(5)

# Find the first 10 image elements
#images = driver.find_elements(By.XPATH, '//img[@type="foaf:Image"]')[:10]
images = driver.find_elements(By.TAG_NAME, 'img')[:10]
# Download each image
for i, img in enumerate(images):
    src = img.get_attribute('src')
    img_data = requests.get(src).content
    with open(f'{photos_folder}/image_{i+1}.jpg', 'wb') as handler:
        handler.write(img_data)

# Close the WebDriver
driver.quit()