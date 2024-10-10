from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Set up the WebDriver (Chrome)
driver = webdriver.Chrome()

# Open Google
driver.get("http://www.google.com")

# Find the search box
search_box = driver.find_element("name", "q")

# Enter search term and submit
search_box.send_keys("Automation Testing")
search_box.send_keys(Keys.RETURN)

# Print the title of the results page
print(driver.title)

# Close the browser
driver.quit()
