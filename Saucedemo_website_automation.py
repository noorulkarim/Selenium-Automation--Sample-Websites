# Name:Noor ul karim


# Selenium Python Task:
# 1. Go to URL: https://www.saucedemo.com/
# 2. Log in with standard_user
# 3. Verify login is successful
# 4. Add a product to the cart
# 5. Go to cart and checkout
# 6. Enter name & postal code
# 7. Finish the purchase
# 8. Verify that the purchase is successful
# 8. Go back to homepage
# 9. Log out
# 10. Verify user is logged out successfully

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()

# 1. Go to URL: https://www.saucedemo.com/
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(1)

# 2. Log in with standard_user
username = driver.find_element("id", "user-name").send_keys("standard_user")
password = driver.find_element("id", "password").send_keys("secret_sauce")
time.sleep(1)
loginbutton = driver.find_element("id", "login-button").click()
time.sleep(2)

# 3. Verify login is successful
burgermenu = driver.find_element("id", "react-burger-menu-btn").click()
time.sleep(1)

if driver.find_element("id", "logout_sidebar_link").text.lower() == "logout":
    print("Login Successful!")
else:
    print("Login not Successful")
menu_close = driver.find_element("id", "react-burger-cross-btn").click()
time.sleep(1)

# 4. Add a product to the cart
add_to_cart_product = driver.find_element(
    "id", "add-to-cart-sauce-labs-bike-light"
).click()
time.sleep(1)

# 5. Go to cart and checkout
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
time.sleep(2)
checkout = driver.find_element("id", "checkout").click()
time.sleep(2)


# 6. Enter name & postal code
firstname = driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("John")
lastname = driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("Doe")
zipcode = driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("11417")
time.sleep(1)

# 7. Finish the purchase
continue_button = driver.find_element(By.ID, "continue").click()
time.sleep(2)
finish_button = driver.find_element(By.ID, "finish").click()
time.sleep(2)

# 8. Verify that the purchase is successful
if (
    driver.find_element(By.CLASS_NAME, "complete-header").text
).lower() == "thank you for your order!":
    print("Check 1: Purchase Successful!")
else:
    print("Check 1:Purchase not successful")

# Check if the shopping cart badge exists
try:
    shopping_cart_badge = driver.find_element(
        By.XPATH, "//span[@class='shopping-cart-badge']"
    )
    print("Check 2:Shopping cart badge exists.")
except NoSuchElementException:
    print("Check 2:Shopping cart badge does not exist.")

# 8. Go back to homepage
back_to_home = driver.find_element(By.ID, "back-to-products").click()
time.sleep(2)

# 9. Log out
burgermenu = driver.find_element("id", "react-burger-menu-btn").click()
time.sleep(2)
logoutbutton = driver.find_element("id", "logout_sidebar_link").click()
time.sleep(2)

# 10. Verify user is logged out successfully
if driver.find_element("id", "login-button").get_attribute("value").lower() == "login":
    print("Logout Successful!")
else:
    print("Logout Unsuccessful")

driver.close()
