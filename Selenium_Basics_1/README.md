# Explicit vs Implicit

## Implicit Wait in Python Selenium:

Implicit wait is a global wait applied throughout the lifespan of the WebDriver object. By setting an implicit wait, the WebDriver will wait for a specified amount of time before throwing an exception if an element is not immediately available. It saves time and avoids using explicit waits at every step.

```python
driver.implicitly_wait(10)
```

## Explicit Wait in Python Selenium:

Explicit wait is a more specific wait applied to a particular condition or element. It allows you to define a certain condition and a maximum amount of time to wait for that condition to be met. It gives more control and flexibility to your test scripts by waiting for specific elements or conditions before proceeding further.

```python
WebDriverWait(driver, 30).until( 
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label') , # Element filtration
        'Complete!' # The expected text
    )
)
```

## Entire Code:

```python
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



os.environ['PATH'] += r"D:/SeleniumDrivers"  #Adding Chrome_Web_Driver to path
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(10) #asteapta ca site-ul sa incarce toate elementele folosite in taskuri
my_element = driver.find_element_by_id('downloadButton'); #gaseste elementul dupa id
my_element.click()

#Explicit wait (asteapta pana o conditie anume este indeplinita)
WebDriverWait(driver, 30).until(   # Returneaza true atunci cand gaseste elementul de tip text(div) dat prin class name , cu valoarea 'Complete!'
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label') , # Element filtration
        'Complete!' # The expected text
    )
)
```

![](https://github.com/Razvan03/Selenium-Basics---Web-Scraping-Bots-Browser-Automation-Testing/blob/main/Selenium_Basics_1/Gif1.gif)
