import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to Linkedin page
driver.get("https://in.linkedin.com")

signin_button = driver.find_element_by_xpath("//a [@class='nav__button-secondary']")  
signin_button.click()
# Wait for the new page to load
time.sleep(3)
# Verify the heading of the page 

    if driver.title("LinkedIn Login, Sign in | LinkedIn"):
        print("success")
    #This pattern of catching all exceptions is ok when you are starting out
    else:
        print("not successful")

# Close the browser   
driver.close()
        

