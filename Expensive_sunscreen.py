"""
Find the most expensive sunscreen and add it to the cart.
SCOPE:
1) Launch Firefox Driver
2) Navigate to Highest prized Sunscreen 
3) Add that sunscreen to the cart
4) Open the cart
5) Check if the exact same sunscreen is added
6) Print the result
7) Close the browser

"""

from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the Sunscreen page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if the control lands on the right web page 
if browser.title!="The best moisturizers in the world!":
    print("page found")
    
    exit()
else:
    print("Page not found")

# Creating a list with prizes of all the Sunscreens
sunscreen_prices=list()
prices_box=browser.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices_box:
    price=int(i.text.strip("Price: Rs. "))
    sunscreen_prices.append(price)
print("The prizes of the moisturizers are ",sunscreen_prices)

# Finding the sunscreen with the highest prize
highest_price=max(sunscreen_prices)
print("The highest prize is",highest_price)

# Adding to cart the sunscreen with highest prize
add_button=browser.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(highest_price))
add_button.click()

# Clicking on cart button to check if the correct sunscreen is added
add_to_cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_button.click()

time.sleep(3)

# Check if the final cart total is equal to the highest prize and print pass or fail

final_price=int(browser.find_element_by_xpath('//div[@class="row justify-content-center top-space-50"]//td[2]').text)
print("Prize in cart is ",final_price)
if final_price==highest_price:
    print("Pass")
else:
    print("Fail")

    
browser.close()
