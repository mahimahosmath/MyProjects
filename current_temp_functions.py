"""
Selenium script that performs common actions like: 
click button, get text from box

SCOPE:
1) Launch Firefox driver
2) Navigate to weathershopper Tutorial page
3) check for the temperature display box
4) convert the current temperature into integer
5) print the current temperature
6) write a function to verify if the control has landed on the correct page
7) compare the current temperature with fixed temperature values for further navigation
8) Click the approtiate button after checking the conditions and maake a function call to verify
9) close the browser
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


#function to verify the operation
def check_title(type_title,title):
   
    if type_title==title:
        print("successfully land on %s page"%type_title)
    else:
        print("unsuccessful")
    

#Check for the conditions using if loop , if the temperature is less than 19 then click the moisturizers button and verify by making a function call 
if (temperature_corrected<19):
    moisturizer_button = driver.find_element_by_xpath("//a[@ href='/moisturizer'] ")
    moisturizer_button.click()
    title= 'Moisturizers'
    type_title_moisturizers=driver.find_element_by_xpath("//h2['Moisturizers']").text
    check_title(type_title_moisturizers,title)


#Check for the conditions using if loop , if the temperature is greater than 34 then click the moisturizers button and verify by making a function call 
elif temperature_corrected >34:
    sunscreen_button=driver.find_element_by_xpath("//a[@ href='/sunscreen']  ")
    sunscreen_button.click()
    title= 'Sunscreens'
    type_title_sunscreens=driver.find_element_by_xpath("//h2['Sunscreens']").text
    check_title(type_title_sunscreens,title)


#pause for 3 secs
time.sleep(3)

#close the browser
driver.close()





