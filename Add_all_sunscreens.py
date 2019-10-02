"""
Add all the sunscreens  to the cart.
SCOPE:
1) Launch Firefox Driver
2) Navigate to Sunscreen page 
3) Add all the sunscreens
4) Open the cart
5) Check if all the items are added by comparing the total price with the sum
6) Print the result
7) Close the browser

"""

from selenium import webdriver
import time

# Creating an instance of the web browser and navigating to the Moisturizer page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if the control lands on the right web page 
if browser.title!="The best moisturizers in the world!":
    print("page not found")
    browser.close()
    exit()
else:
    print("Page found")

# Creating a list with prices of all sunscreens
sunscreen_prices=list()
prices_box=browser.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices_box:
    price=int(i.text.strip("Price: Rs. "))
    sunscreen_prices.append(price)
print("The prices of the sunscreens are ",sunscreen_prices)


#Getting the sum of prices of all the elements in the list
total=0
for ele in range(0, len(sunscreen_prices)): 
    total = total + sunscreen_prices[ele] 
  
# printing the sum or total value
print("Sum of all elements in given list: ", total) 

#Clicking the add button for all the items on the page and printing the added items
add_buttons=browser.find_elements_by_xpath('//button[contains(text(),"Add")]')
items=0
for i in add_buttons:
    i.click()
    items+=1
    print("Added",items)
    

# Clicking on cart button
add_to_cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
add_to_cart_button.click()

#Checking if the final price in the cart matches the sum of the added items and printing the result
final_price=(browser.find_element_by_xpath('//p[@id="total"]').text)
final_price=int(final_price.strip("Total: Rupees "))
print("Price in cart is ",final_price)
if final_price==total:
    print("Pass")
else:
    print("Fail")

#pause for 3secs
time.sleep(3)

#close the browser    
browser.close()

