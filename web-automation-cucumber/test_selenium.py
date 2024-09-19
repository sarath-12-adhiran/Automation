from selenium import webdriver

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the first URL in the initial window
driver.get('https://google.com')

# Open a new window/tab with a different URL
driver.execute_script("window.open('https://amazon.com', '_blank');")

# Open another new window/tab with yet another URL
driver.execute_script("window.open('https://flipkart.com', '_blank');")

driver.execute_script("window.open('https://yahoo.com', '_blank');")

# Get all window handles
handles = driver.window_handles

# Print out all window handles
print("Window Handles:", handles)

# Switch to the first new window (second handle in the list)
driver.switch_to.window(handles[1])
print("One", driver.title)  # Should print the title of 'https://another-example.com'

# Perform actions in the new window
# For example, retrieve the title
print(driver.title)

# Switch to the third window (third handle in the list)
driver.switch_to.window(handles[2])
print("Two:", driver.title)  # Should print the title of 'https://yet-another-example.com'

# Switch to the third window (third handle in the list)
driver.switch_to.window(handles[2])
print("Two:", driver.title)  # Should print the title of 'https://yet-another-example.com'

# Switch back to the original window (first handle in the list)
driver.switch_to.window(handles[0])
print("Three:", driver.title)  # Should print the title of 'https://example.com'

# Quit the driver
driver.quit()
