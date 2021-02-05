import time
import random

from selenium import webdriver


executable_path=r'C:/Users/Karolina/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path)

driver.get('http://localhost:8080/');
driver.maximize_window()
time.sleep(3)

products_site = driver.find_element_by_class_name("category")
products_site.click()

# Add products from first category
category_1 =  driver.find_elements_by_css_selector("div.block-categories.hidden-sm-down > ul > li:nth-child(2) > ul > li:nth-child(1)")
time.sleep(2)
driver.find_element_by_css_selector("div.products.row > div:nth-child(1)").click()

quantity = driver.find_element_by_id("quantity_wanted")
quantity.clear()
quantity.send_keys(random.randint(1, 3))

driver.find_element_by_class_name("add-to-cart").click()
time.sleep(2)

continue_shopping = driver.find_element_by_css_selector("div.cart-content-btn button")
continue_shopping.click()

# second product
driver.execute_script("window.history.go(-1)")
time.sleep(2)
driver.find_element_by_css_selector("div.products.row > div:nth-child(2)").click()
time.sleep(2)
quantity = driver.find_element_by_id("quantity_wanted")
quantity.clear()
quantity.send_keys(random.randint(1, 3))

driver.find_element_by_class_name("add-to-cart").click()

time.sleep(2)

continue_shopping = driver.find_element_by_css_selector("div.cart-content-btn button")
continue_shopping.click()
# product
driver.execute_script("window.history.go(-1)")
driver.find_element_by_css_selector("div.products.row > div:nth-child(3)").click()

quantity = driver.find_element_by_id("quantity_wanted")
quantity.clear()
quantity.send_keys(random.randint(1, 3))

driver.find_element_by_class_name("add-to-cart").click()
time.sleep(5)
continue_shopping = driver.find_element_by_css_selector("div.cart-content-btn button")
continue_shopping.click()

# cat 2
products_site = driver.find_element_by_class_name("category")
products_site.click()

category_2 =  driver.find_element_by_css_selector("div.block-categories.hidden-sm-down > ul > li:nth-child(2) > ul > li:nth-child(2)").click()

# Add products from second category
driver.find_element_by_css_selector("div.products.row > div:nth-child(1)").click()

quantity = driver.find_element_by_id("quantity_wanted")
quantity.clear()
quantity.send_keys(random.randint(1, 3))

driver.find_element_by_class_name("add-to-cart").click()

time.sleep(5)

continue_shopping = driver.find_element_by_css_selector("div.cart-content-btn button")
continue_shopping.click()
# second
driver.execute_script("window.history.go(-1)")
driver.find_element_by_css_selector("div.products.row > div:nth-child(2)").click()

quantity = driver.find_element_by_id("quantity_wanted")
quantity.clear()
quantity.send_keys(random.randint(1, 3))

driver.find_element_by_class_name("add-to-cart").click()
time.sleep(5)
continue_shopping = driver.find_element_by_css_selector("div.cart-content-btn button")
continue_shopping.click()


# go to shoping card and remove one product
driver.find_element_by_class_name("blockcart").click()
driver.find_element_by_class_name("remove-from-cart").click()

driver.find_element_by_class_name("checkout").click()

# personal info
driver.find_elements_by_class_name("radio-inline")[1].click()
driver.find_element_by_name("firstname").send_keys("Karolina")
driver.find_element_by_name("lastname").send_keys("Jed")
driver.find_element_by_name("email").send_keys("karolinaJ"+str(random.randint(1, 100))+"@gmail.com")
driver.find_element_by_name("password").send_keys("TestTest")
driver.find_element_by_name("customer_privacy").click()
driver.find_element_by_name("newsletter").click()
driver.find_element_by_name("psgdpr").click()


driver.find_element_by_class_name("continue").click()

#adress form
time.sleep(3)
driver.find_element_by_name("address1").send_keys("Główna 33")
driver.find_element_by_name("postcode").send_keys("80-228")
driver.find_element_by_name("city").send_keys("Gdańsk")
driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
time.sleep(3)
driver.find_element_by_name("phone").send_keys("123456789")

driver.find_element_by_xpath("//*[@id='delivery-address']/div/footer/button").click()

# shipping form
time.sleep(3)
driver.find_element_by_xpath("//*[@id='delivery_option_7']").click()
driver.find_element_by_xpath("//*[@id='js-delivery']/button").click()

# payment
time.sleep(3)
driver.find_element_by_id("payment-option-1").click()
driver.find_element_by_xpath("//*[@id='conditions_to_approve[terms-and-conditions]']").click()
driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
time.sleep(3)

# confirmation
driver.find_element_by_xpath("//*[@id='payment-confirmation']/div[1]/button").click()


#go to account and check shipping status
driver.find_element_by_class_name("account").click()
time.sleep(2)
driver.find_element_by_id("history-link").click()
time.sleep(2)
driver.find_element_by_css_selector("td.text-sm-center.order-actions > a:nth-child(1)").click()


time.sleep(5)
driver.quit()