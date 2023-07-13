# Selenium Basics-Web Scraping Bots, Browser-Automation, Testing

Selenium Basics is a comprehensive repository that showcases the versatile features of Selenium, an open-source framework renowned for its prowess in web scraping, browser automation, and testing. With a focus on these three key areas, this repository provides a solid foundation for leveraging Selenium's capabilities effectively.

In order to follow this tutorial you must install Python and Pycharm(the IDE) with the links below, then open cmd and type ``` pip install selenium ```. In order to use ChromeDriver you need to install the version compatible with the version of your Chrome. You can check the version of Chrome at ```chrome://version/``` and then pick the right version from the link below. 

🔗 Python Download: [https://www.python.org/downloads](https://www.python.org/downloads/)

🔗 Pycharm Download: [https://www.jetbrains.com/pycharm/dow...](https://www.jetbrains.com/pycharm/download/?section=windows) 

🔗 Chromedriver download website: [https://chromedriver.storage.googleap...](https://chromedriver.storage.googleapis.com/index.html)

Only the first digits before the first '.' need to match:
![Alt Text](https://github.com/Razvan03/Selenium-Basics---Web-Scraping-Bots-Browser-Automation-Testing/blob/main/ChromeVersion.png)
![Alt Text](https://github.com/Razvan03/Selenium-Basics---Web-Scraping-Bots-Browser-Automation-Testing/blob/main/ChromeDriver.png)


## Table of Contents

-Getting Started with the basics
-[Explicit vs Implicit](https://github.com/Razvan03/Selenium-Basics---Web-Scraping-Bots-Browser-Automation-Testing/tree/main/Selenium_Basics_1)
-[Sending Keys & CSS Selector](https://github.com/Razvan03/Selenium-Basics---Web-Scraping-Bots-Browser-Automation-Testing/tree/main/Basic_Form_Test_2)


## Getting Started with the basics

1. Import the necessary modules:

-os for managing the operating system functionalities.
-webdriver from Selenium for controlling the web browser.

```python
import os
from selenium import webdriver
```

2. Set the Chrome driver path:

-Use os.environ['PATH'] to access the system's environment variables.
-Append the path to the Chrome driver executable (D:/SeleniumDrivers) to the existing PATH variable.
-This step ensures that the system can locate the Chrome driver executable when initializing the web driver.

```python
os.environ['PATH'] += r"D:/SeleniumDrivers"  #Adding Chrome_Web_Driver to path
```

3. Initialize the Chrome web driver:

-Use webdriver.Chrome() to create an instance of the Chrome web driver.
-This will open a new Chrome browser window for automation.
```python
driver = webdriver.Chrome()
```

4. Navigate to the target website:

Use the get() method of the web driver to open the desired URL (https://site.html).
The web driver will load the webpage in the opened Chrome browser window.

```python
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
```

5. Find the element by ID:

Use the find_element_by_id() method of the web driver to locate the element with the specified ID (downloadButton) on the webpage.
This method returns a web element object representing the desired element on the page.

```python
my_element = driver.find_element_by_id('downloadButton'); 
```

6. Perform an action on the element:

In this case, call the click() method on the my_element object to simulate a click action on the identified element.
This will trigger the associated functionality or event on the webpage.

```python
my_element.click()
```


## Entire Code:
```python
import os
from selenium import webdriver

os.environ['PATH'] += r"D:/SeleniumDrivers"  #Don't forget to update the PATH with your PATH of ChromeDriver
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
my_element = driver.find_element_by_id('downloadButton'); #gaseste elementul dupa id
my_element.click()
```

## Congratulations! You just made your first Browser Automation! ^_^ 
