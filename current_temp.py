"""
Selenium script that performs common actions like: 
click button, get text from box

SCOPE:
1) Launch Firefox driver
2) Navigate to weathershopper Tutorial page
3) check for the temperature display box
4) convert the current temperature into integer
5) print the current temperature
6) compare the current temperature with fixed temperature values for further navigation
7) Click the approtiate button after checking the conditions
8) Close the browser
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver= webdriver.Firefox()

# KEY POINT: The driver.get method will navigate to a page given by the URL
driver.get('https://weathershopper.pythonanywhere.com')


#Find the current temperature box using xpath and retrive the value from the box
current_temperature= driver.find_element_by_xpath("//span[@ id='temperature']")  
celsius=current_temperature.text.split(' ')


#Convert the retrived temperature into integer and print the temperature
temperature_corrected= int(celsius[0])
print(temperature_corrected)

#Check for the conditions using if loop , if the temperature is less than 19 then click the moisturizers button and verify using the heading of the moisturizer page 
if (temperature_corrected<19):
    moisturizer_button = driver.find_element_by_xpath("//a[@ href='/moisturizer'] ")
    moisturizer_button.click()
    if driver.find_element_by_xpath("//h2['Moisturizers']"):
        print("the test was successful and tracked the moisturizers page")
    else:
        print("the test failed to track the moisturizers page")


#Check for the condition, if the temperature is more than 34 then click the sunscreens button and verify using the heading of the sunscreen page 
elif temperature_corrected >34:
    sunscreen_button=driver.find_element_by_xpath("//a[@ href='/sunscreen']  ")
    sunscreen_button.click()
    if driver.find_element_by_xpath("//h2['Sunscreens']"):
        print("the test was successful and tracked the sunscreens page") 
    else:
        print("the test failed to track the sunscreens page")


#pause the script for 3 secs
time.sleep(3)

#close the browser
driver.close()