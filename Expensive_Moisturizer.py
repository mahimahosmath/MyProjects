"""
Find the most expensive moisturizer and add it to the cart.
SCOPE:
1) Launch Firefox Driver
2) Navigate to Highest prized Moisturizer 
3) Add that moisturizer to the cart
4) Open the cart
5) Check if the exact same moisturizer is added
6) Print the result
7) Close the browser

"""

from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the Moisturizer page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/moisturizer')

# Checking if the control lands on the right web page 
if browser.title!="The best moisturizers in the world!":
    print("page found")
    browser.close()
    exit()
else:
    print("Page not found")

# Creating a list with prizes of all moisturizers
moisturizer_prices=list()
prices_box=browser.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices_box:
    price=int(i.text.strip("Price: Rs. "))
    moisturizer_prices.append(price)
print("The prizes of the moisturizers are ",moisturizer_prices)

# Finding the moisturizer with the highest prize
highest_prize=max(moisturizer_prices)
print("The highest prize is",highest_prize)

# Adding to cart the moisturizer with max prize
add_button=browser.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(highest_prize))
add_button.click()

# Clicking on cart button to check if the correct moisturizer is added
add_to_cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_button.click()

time.sleep(3)

# Check if the final cart total is equal to the highest prize and print pass or fail

final_prize=int(browser.find_element_by_xpath('//div[@class="row justify-content-center top-space-50"]//td[2]').text)
print("Prize in cart is ",final_prize)
if final_prize==highest_prize:
    print("Pass")
else:
    print("Fail")

    
browser.close()


