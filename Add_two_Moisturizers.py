"""
 Add two moisturizers in the cart according to the conditions.
 SCOPE:
 1) Launch Firefox Driver
 2) Add moisterizers to the cart accroding to the following conditions
     (a) First, select the least expensive mositurizer that contains Aloe
     (b) For your second moisturizer, select the least expensive moisturizer that contains almond.
 3) Make a list of products to be added
 4) Click on the cart
 5) Check if all the moisturizers are added by compareing list of products in the cart againist list of products to be added
 6) Close the browser
 Author : Bilwa Gutthi
"""

from selenium import webdriver
import time

# Creating an instence of thw web browser and navigating to the Shopping page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/moisturizer')

# Checking if the right web page has been loaded
if browser.title!="The best moisturizers in the world!":
    print("Error in loading page")
    browser.close()
    exit()
else:
    print("\n Page loaded")

print("_"*50)

# List of all moisturizer
list_moisturizer=browser.find_elements_by_xpath('//div[@class="text-center col-4"]')

# List of products on which we clicked add
products_added=[]

# Products with aloe
print("\n Moisturizers with Aloe are :\n")
aloe_list=[]
for i in list_moisturizer:
    try:
        current_element=i.find_element_by_xpath('.//p[contains(text(),"Aloe")]')
        price_element=i.find_element_by_xpath('.//p[contains(text(),"Price")]').text
        price=int(price_element.strip("Price : Rs. "))
        print("     ",current_element.text,"    ",price)
        aloe_list.append([i,price])
    except Exception as e:
        continue

# Finding Aloe moisturizer with minimum price
first_min_price=1000
for i,j in aloe_list:
    if j<first_min_price:
        first_min_price=j
        first_product=i
print("\n Aloe moisturizer and minimum price is \n ",first_product.find_element_by_xpath('.//p[contains(text(),"Aloe")]').text, "\n and cost ",first_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)
products_added.append(first_product.find_element_by_xpath('.//p[contains(text(),"Aloe")]').text)

# Adding first element to the cart
first_product_add=first_product.find_element_by_xpath('.//button[text()="Add"]')
first_product_add.click()


print("_"*50)


# Finding moisturizers with almond and thier prices 
print("\nMoisturizerz with Almond are :\n")
almond_list=[]
for i in list_moisturizer:
    try:
        current_element=i.find_element_by_xpath('.//p[contains(text(),"Almond")]')
        price_element=i.find_element_by_xpath('.//p[contains(text(),"Price")]').text
        price=int(price_element.strip("Price : Rs. "))
        print("     ",current_element.text,"    ",price)
        almond_list.append([i,price])
    except Exception as e:
        continue

# Finding the least expensive moisturizer that contains almond
second_min_price=1000
for i,j in almond_list:
    if j<second_min_price:
        second_min_price=j
        second_product=i
print("\nMoisturizer with Almond and minimum price is\n ",second_product.find_element_by_xpath('.//p[contains(text(),"Almond")]').text, "\n and cost ",second_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)

# Adding second product to the cart
products_added.append(second_product.find_element_by_xpath('.//p[contains(text(),"Almond")]').text)
second_product_add=second_product.find_element_by_xpath('.//button[text()="Add"]')
second_product_add.click()
print("_"*50)


# Clicking on cart button to check if required sunscreens  are added
cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
cart_button.click()

# Finding products in the cart
cart_product_elements=browser.find_elements_by_xpath('//tbody/tr/td[1]')
cart_products=[]
for element in cart_product_elements:
    cart_products.append(element.text)
print("\n Products in the cart are :\n")
print("\n".join(cart_products))

# Checking if the right products are added
if products_added==cart_products:
    print("\n\n  Success : Correct products added")
else:
    print("Fail")

browser.close()
