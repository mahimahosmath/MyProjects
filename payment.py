"""
Test to read the temperature and choose the products

1) Launch Chrome driver
2) Navigate to weathershopper page
3) Read the temperature
4) Click on the desired product depending on the temperature
5) Open the product list page
6) Close the driver
"""
import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to LinkedIn page
driver.get("https://weathershopper.pythonanywhere.com/")

#Check the title of the page
if(driver.title =="The best moisturizers in the world!"):
    print("Loaded page Successfully")
else:
    print("Error Loading Page")

# Get the temperature text input from web page 
temp  = driver.find_element_by_xpath("//span[@id='temperature']").text

# Filter out and read only the the digits form the string 
temp1 = int(''.join(filter(lambda i: i.isdigit(), temp)))

#Check the product heading
def check_page(product,page):
    if product == page:
        print("Correct Product Heading")
    else:
        print("Inncorrect Product Heading")

# Pause the script to wait for page elements to load
time.sleep(3)

# Condition to check weather to buy Moisturizers or Sunscreens depending on the temperature
# Buy a moisturizer if temperature is less than 19 degree celsius
# Buy a sunscreen if temperature is greather than 43 degree celsius
if temp1<19:
    product = 'Moisturizers'
    moist_button  = driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy moisturizers']") 
    moist_button.click()
    moist_page = driver.find_element_by_xpath("//h2").text
    check_page(product,moist_page)
    # Creating a list of all moisturizers
    list_moisturizer=driver.find_elements_by_xpath('//div[@class="text-center col-4"]')

    # A List of products which are added into the cart
    products_added=[]

    # The products containing Aloe
    print("\n Moisturizers containing Aloe are :\t")
    aloe_moist_list=[]
    for i in list_moisturizer:
        try:
            current_element=i.find_element_by_xpath('.//p[contains(text(),"Aloe")]')
            price_element=i.find_element_by_xpath('.//p[contains(text(),"Price")]').text
            price=int(price_element.strip("Price : Rs. "))
            print("     ",current_element.text,"  :  ",price)
            aloe_moist_list.append([i,price])
        except Exception as e:
            continue

    # Finding Aloe moisturizer with minimum price
    first_min_price=1000
    for i,j in aloe_moist_list:
        if j<first_min_price:
            first_min_price=j
            first_product=i
    print("Moisturizer containing Aloe added to cart : \n ",first_product.find_element_by_xpath('.//p[contains(text(),"Aloe")]').text, "\n and the ",first_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)
    products_added.append(first_product.find_element_by_xpath('.//p[contains(text(),"Aloe")]').text)

    # Adding the first product to the cart to the cart
    first_product_add=first_product.find_element_by_xpath('.//button[text()="Add"]')
    first_product_add.click()

    # Finding moisturizers with almond and thier prices 
    print("\nMoisturizers with Almond are :\n")
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
    print("\nMoisturizer containing Almond added to cart :\n ",second_product.find_element_by_xpath('.//p[contains(text(),"Almond")]').text, "\n and the ",second_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)

    # Adding second product to the cart
    products_added.append(second_product.find_element_by_xpath('.//p[contains(text(),"Almond")]').text)
    second_product_add=second_product.find_element_by_xpath('.//button[text()="Add"]')
    second_product_add.click()  

    # Clicking on cart button to check if the correct moisturizers are added    
    cart_button=driver.find_element_by_xpath('//button[@class="thin-text nav-link"]')
    cart_button.click()

    # Finding products in the cart
    cart_items=driver.find_elements_by_xpath('//tbody/tr/td[1]')
    cart_products=[]
    for element in cart_items:
        cart_products.append(element.text)
    print("\n Products in the cart are :\n")
    print("\n".join(cart_products))

    # Pause the script to wait for page elements to load
    time.sleep(3)

    # Checking if the products are addedcorrectly 
    if products_added==cart_products:
        print("\n\n  Successfully added the products")  
    else:
        print("Failed to add products")

    # Clicking on payment button   
    pay_button=driver.find_element_by_xpath('//button[@class="stripe-button-el"]')
    pay_button.click()

elif temp1>34:
    product = 'Sunscreens'
    sun_button  = driver.find_element_by_xpath("//button[@class='btn btn-primary' and text()='Buy sunscreens']") 
    sun_button.click()
    sun_page = driver.find_element_by_xpath("//h2").text
    check_page(product,sun_page)
    # List of all sunscreens
    list_sunscreens=driver.find_elements_by_xpath('//div[@class="text-center col-4"]')

    # List of products on which are  added to cart
    products_added=[]

    # Finding sunscreens with SPF-50 with their prices 
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

    # Finding sunscreen of least price that contains SPF-50 
    first_min_price=1000
    for i,j in spf50_list:
        if j<first_min_price:
            first_min_price=j
            first_product=i
    print("\n Product with spf 50 :\n ",first_product.find_element_by_xpath('.//p[contains(text(),"SPF-50")]').text, "\n and the ",first_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)
    products_added.append(first_product.find_element_by_xpath('.//p[contains(text(),"SPF-50")]').text)

    # Adding first product to the cart
    first_product_add=first_product.find_element_by_xpath('.//button[text()="Add"]')
    first_product_add.click()

    # Pause the script to wait for page elements to load
    time.sleep(3)

    # Finding sunscreens with SPF-30 with thier prices 
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

    # Finding sunscreen of least price that contains SPF-30
    second_min_price=1000
    for i,j in spf30_list:
        if j<second_min_price:
            second_min_price=j
            second_product=i
    print("\nProduct with SPF-30 :\n ",second_product.find_element_by_xpath('.//p[contains(text(),"SPF-30")]').text, "\n and the ",second_product.find_element_by_xpath('.//p[contains(text(),"Price")]').text)

    # Adding second product to the cart
    products_added.append(second_product.find_element_by_xpath('.//p[contains(text(),"SPF-30")]').text)
    second_product_add=second_product.find_element_by_xpath('.//button[text()="Add"]')
    second_product_add.click()

    # Clicking on cart button to check if required sunscreens  are added
    cart_button=driver.find_element_by_xpath('//button[@class="thin-text nav-link"]')
    cart_button.click()

    # Pause the script to wait for page elements to load
    time.sleep(3)

    # Finding products in the cart
    cart_items=driver.find_elements_by_xpath('//tbody/tr/td[1]')
    cart_products=[]
    for element in cart_items:
        cart_products.append(element.text)
    print("\n Products in the cart are :\n")
    print("\n".join(cart_products))

    # Checking if the right products are added
    if products_added==cart_products:
        print("\n  Successfully added the products")
    else:
        print("Failed to add products")

    # Clicking on payment button   
    pay_button=driver.find_element_by_xpath('//button[@class="stripe-button-el"]')
    pay_button.click()

# Pause the script to wait for page elements to load
time.sleep(3)

# Close the browser
driver.close()
