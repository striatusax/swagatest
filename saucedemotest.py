from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.saucedemo.com/')


#авторизация под standard_user
username = browser.find_element(By.XPATH, '//*[@id="user-name"]')  
username.send_keys('standard_user')

password = browser.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('secret_sauce')

loginbutton = browser.find_element(By.XPATH, '//*[@id="login-button"]')
loginbutton.click()

#выбот товара Sauce Labs Bolt T-Shirt
addtocartbutton = browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
addtocartbutton.click()

cartbutton = browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
cartbutton.click()

#проверка, что товар добавлен в корзину
get_source = browser.page_source
search_text = "Sauce Labs Bolt T-Shirt" in get_source
if search_text is False:
   print("ОШИБКА: товар не добавлен в корзину!")
else:
   print("Товар добавлен к корзину.")

checkoutbutton = cartbutton = browser.find_element(By.XPATH, '//*[@id="checkout"]')
cartbutton.click()

#ввод данных покупателя и завершение покупки
firstname = browser.find_element(By.XPATH, '//*[@id="first-name"]')  
firstname.send_keys('Max')

lastname = browser.find_element(By.XPATH, '//*[@id="last-name"]')  
lastname.send_keys('Joe')

postcode = browser.find_element(By.XPATH, '//*[@id="postal-code"]')  
postcode.send_keys('6548795')

cartconbutton = cartbutton = browser.find_element(By.XPATH, '//*[@id="continue"]')
cartconbutton.click()

finishbutton = cartbutton = browser.find_element(By.XPATH, '//*[@id="finish"]')
finishbutton.click()

#проверка, что покупка совершена успешно
get_source = browser.page_source
search_text = "Thank you for your order!" in get_source
if search_text is False:
   print("Ошибка: покупка не совершена!")
else:
   print("Покупка совершена успешно.")
