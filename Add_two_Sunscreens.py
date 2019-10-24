"""
 Add two sunscreens in the cart according to the conditions.
 SCOPE:
 1) Launch Firefox Driver
 2) Add sunscreens to the cart accroding to the following conditions
     (a) First, select the least expensive sunscreen that is SPF-50
     (b)  For your second sunscreen, select the least expensive sunscreen that is SPF-30.
 3) Make a list of products to be added
 4) Click on the cart
 5) Check if all the sunscreens are added by compareing list of products in the cart againist list of products to be added
 6) Close the browser
"""

from selenium import webdriver
import time

# Creating an instence of thw web browser and navigating to the Shopping page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if the right web page has been loaded
if browser.title!="The best moisturizers in the world!":
    print("Error in loading page")
    browser.close()
    exit()
else:
    print("\n Page loaded")

print("_"*50)

# List of all sunscreens
list_sunscreens=browser.find_elements_by_xpath('//div[@class="text-center col-4"]')

# List of products on which we clicked add
products_added=[]

# Finding sunscreens with SPF-50 and thier prices 
print("\n Products with SPF-50 are :\n")
spf50_list=[]
for i in list_sunscreens:
    try:
        current_element=i.find_element_by_xpath('.//p[contains(text(),"SPF-50")]')
        price_element=i.find_element_by_xpath('.//p[contains(text(),"Price")]').text
        price=int(price_element.strip("Price : Rs. "))
        print("     ",current_element.text,"    ",price)
        spf50_list.append([i,price])
    except Exception as e:
        continue

# Finding sunscreen with minimum price that has SPF-50
first_min_price=1000
for i,j in spf50_list:
    if j<first_min_price:
        first_min_price=j
        first_product=i
print("\n Product with spf 50  and minimum price is \n ",first_product.find_element_by_xpath('.//p[contains(text(),"SPF-50")]').text, "\n and cost ",first_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)
products_added.append(first_product.find_element_by_xpath('.//p[contains(text(),"SPF-50")]').text)

# Adding first element to the cart
first_product_add=first_product.find_element_by_xpath('.//button[text()="Add"]')
first_product_add.click()


print("_"*50)


# Finding sunscreens with SPF-30 and thier prices 
print("\nProducts with SPF-30 are :\n")
spf30_list=[]
for i in list_sunscreens:
    try:
        current_element=i.find_element_by_xpath('.//p[contains(text(),"SPF-30")]')
        price_element=i.find_element_by_xpath('.//p[contains(text(),"Price")]').text
        price=int(price_element.strip("Price : Rs. "))
        print("     ",current_element.text,"    ",price)
        spf30_list.append([i,price])
    except Exception as e:
        continue

# Finding sunscreen with minimum price that has SPF-30
second_min_price=1000
for i,j in spf30_list:
    if j<second_min_price:
        second_min_price=j
        second_product=i
print("\nProduct with SPF-30  and minimum price is\n ",second_product.find_element_by_xpath('.//p[contains(text(),"SPF-30")]').text, "\n and cost ",second_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)

# Adding second product to the cart
products_added.append(second_product.find_element_by_xpath('.//p[contains(text(),"SPF-30")]').text)
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