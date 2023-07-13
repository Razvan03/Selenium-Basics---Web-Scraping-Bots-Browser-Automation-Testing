import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #Pentru a folosi control keys

os.environ['PATH'] += r"D:/SeleniumDrivers"  #Adding Chrome_Web_Driver to path
driver = webdriver.Chrome()

driver.get("https://localhost:44308/BasicForm")
driver.implicitly_wait(5)

try:
    ok_button = driver.find_element_by_id('popupButton')  #Apasa butonul ok din pop-up la startarea site-ului
    ok_button.click()
except:
    print('Ex')

TextBoxA = driver.find_element_by_id('TextBoxA')
TextBoxB = driver.find_element_by_id('TextBoxB')

TextBoxA.send_keys(Keys.NUMPAD1, Keys.NUMPAD5) #Scrie valoare data in textbox folosind numpad keys
TextBoxB.send_keys(15) #Scrie valoarea data in textbox

# Folosim css_selector pentru a filtra elementele dupa un atribut
# De exemplu toate butoanele care au atributul onclick = 'return calculateTotal()'
btnSum = driver.find_element_by_css_selector('button[onclick="return calculateTotal()"]')
btnSum.click()

TextBoxMessage = driver.find_element_by_id('TextBoxMessage')
TextBoxMessage.send_keys("Test")
btnText = driver.find_element_by_css_selector('button[onclick="return showMessage()"]')
btnText.click()