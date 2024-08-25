from selenium import webdriver

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Open GitHub
driver.get("https://www.github.com")

# Find and click on the "Sign in" button
sign_in_button = driver.find_element("link text", "Sign in")
sign_in_button.click()

# Verify that the new page's URL is correct
current_url = driver.current_url
expected_url = "https://github.com/login"
assert current_url == expected_url, f"URL mismatch! Expected: {expected_url}, but got: {current_url}"

# Print confirmation
print("URL verification passed!")

# Wait for 10 seconds before closing the browser
driver.implicitly_wait(10)

# Close the browser
driver.quit()
