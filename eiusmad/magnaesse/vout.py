from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Go to the Google homepage
driver.get("https://www.example.com Find the search box
search_box = driver.find_element_by_name("q")

# Type "Selenium" into the search box
search_box.send_keys("Selenium")

# Submit the search query
search_box.submit()

# Get the search results
results = driver.find_elements_by_class_name("g")

# Print the titles of the first 10 search results
for result in results[:10]:
    print(result.text)

# Close the browser window
driver.close()
