import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

# Check if the title of the page is proper
if(driver.title=="LinkedIn Login, Sign in | LinkedIn"):
    print ("Success:  launched successfully")
else:
    print ("Failure:  Title is incorrect")    

# Find the name field using xpath with id
name = driver.find_element_by_xpath("//input[@id='username']")
# KEY POINT: Send text to an element using send_keys method
name.send_keys('Mahima')



# Sleep is one way to wait for things to load
# Future tutorials cover explicit, implicit and ajax waits
time.sleep(3)

# Close the browser window
driver.close() 
        