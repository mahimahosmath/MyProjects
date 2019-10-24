"""
 Check cart deatils
 SCOPE:
 
 1) Launch Firefox Driver
 2) Find the value of temperature displayed and to click the appropriate button
    (a) If temperature is less than 19 moisturizer button is selected.
    (b) If temperature is more than 34 sunscreen button is selected.
 3) Once the button is selected the program checks wether the webbrowser is redirected to the appropriate page
 4) (a) If on moisturizer page:Add moisterizers to the cart accroding to the following conditions
         - First, select the least expensive mositurizer that contains Aloe
         - For your second moisturizer, select the least expensive moisturizer that contains almond.
    (b) If on sunscreen page :Add sunscreens to the cart accroding to the following conditions
         - First, select the least expensive sunscreen that is SPF-50
         - For your second sunscreen, select the least expensive sunscreen that is SPF-30.
 5) List the products added
 6) Click on the cart
 7) Check the number products
 8) Check the total
 9) Close the browser
 """
from selenium import webdriver
import time

def get_cart_products():
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

    return cart_products


def moisterizers_add():
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

    return products_added

def sunscreens_add():
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

    return products_added

def check_temperature():
    # Finding the tag with tempature value , finding the content of the tag and extracting the values
    temperature_Box=browser.find_element_by_xpath('//span[@id="temperature"]').text.split(' ')

    # Finding the temperature from the list of extracted values
    temperature=int(temperature_Box[0])
    print("The temperature is",temperature)
    return temperature

def select_MorS(temperature):
    products=[]
    #If temperature is less than 19 Moisturizer button is clicked
    if temperature<19:
        button_Moisturizer=browser.find_element_by_xpath('//a[@href="/moisturizer"]')
        button_Moisturizer.click()

        #Cheacking if moisturizer button is clicked and if webbrowser is redirected to the correct page
        if browser.find_element_by_xpath('//h2["Moisturizers"]'):
            print("Temperature is less than 19 , hence moisturizers are selected")
        products=moisterizers_add()

    #If temperature is more than 34 Sunscreen button is clicked
    elif temperature>34:
        button_Sunscreen=browser.find_element_by_xpath('//a[@href="/sunscreen"]')
        button_Sunscreen.click()

        #Cheacking if moisturizer button is clicked and if webbrowser is redirected to the correct page
        if browser.find_element_by_xpath('//h2["sunscreens"]'):
            print("Temperature is greater than 34 , hence sunscreens are selected")
        products=sunscreens_add()
    
    return products


# Creating an instence of thw web browser and navigating to the Shopping page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/')

# Checking if the right web page has been loaded
if browser.title!="The best moisturizers in the world!":
    print("Error in loading page")
    browser.close()
    exit()
else:
    print("\n Page loaded")

# Finding Temperature
temperature=check_temperature()

# Selecting appropriate button, selecting appropriate products from selected page
products_added=select_MorS(temperature)

# Getting the products in cart
cart_products=get_cart_products()

# Amount of products in cart
print("\n No of products in the cart : ",len(cart_products))

# Checking if the right products are added
if products_added==cart_products:
    print("\n\n  Success : Correct products added")
else:
    print("Fail")

# Checking and printing total:
total=int(browser.find_element_by_xpath('//p[contains(text(),"Total")]').text.strip("Total: Rupees "))
print("Cart Totoal : ", total)

browser.close()