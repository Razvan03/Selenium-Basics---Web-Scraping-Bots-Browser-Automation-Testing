# Sending Keys & CSS Selector

## Sending Keys in Selenium:

The send_keys() method is used to simulate keyboard input in Selenium. It allows you to send keys, including special keys and combinations, to interact with web elements like text fields. For numeric input, you can use Keys.NUMPAD1 and Keys.NUMPAD5 or directly input the numbers, such as TextBoxB.send_keys(15).

```python
TextBoxA.send_keys(Keys.NUMPAD1, Keys.NUMPAD5) 
TextBoxB.send_keys(15) 
```

## CSS Selector in Selenium:

CSS Selector is a powerful way to locate web elements based on their CSS properties. In Selenium, find_element_by_css_selector() is used to locate elements using CSS selectors. For instance, driver.find_element_by_css_selector('button[onclick="return calculateTotal()"]') finds a button element with a specific onclick attribute value. CSS selectors provide flexibility for selecting elements by class names, IDs, attributes, and more.

```python
btnSum = driver.find_element_by_css_selector('button[onclick="return calculateTotal()"]')
```

For testing purpose I created basic [website](https://github.com/Razvan03/Selenium-Basics---Web-Scraping-Bots-Browser-Automation-Testing/tree/main/Selenium_BasicForm) using ASP.NET Web Application(.NET Framework).

## Entire Code:

```python
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
```
# Demo:

![](https://github.com/Razvan03/Selenium-Basics---Web-Scraping-Bots-Browser-Automation-Testing/blob/main/Basic_Form_Test_2/Gif2.gif)
