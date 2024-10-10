from selenium import webdriver

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Open a simple website with a button
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

# Find the "Show Message" button by its CSS selector and click it
show_message_button = driver.find_element("css selector", "button[onclick='showInput();']")
show_message_button.click()

# Verify that the button was clicked successfully
output_text = driver.find_element("id", "display").text
assert output_text != "", "Button click failed!"

# Print the output text to confirm the button click
print("Output text:", output_text)

# Wait for 10 seconds before closing the browser
driver.implicitly_wait(10)

# Close the browser
driver.quit()
