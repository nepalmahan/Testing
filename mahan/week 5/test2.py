from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box using its name attribute value
search_box = driver.find_element("name", "q")

# Type the search term
search_box.send_keys("Selenium Python")

# Press the Enter key to submit the search
search_box.send_keys(Keys.RETURN)

# Print the title of the results page
print("Title of the results page:", driver.title)

# Wait for 10 seconds before closing the browser
driver.implicitly_wait(10)

# Close the browser
driver.quit()
