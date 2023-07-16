# Booking.com Web Scraper

This program is a web scraper built with Python and Selenium that allows you to search for hotels on Booking.com, apply various filtrations such as star ratings, and display the results in a formatted table. It provides an easy way to automate the process of finding and comparing hotel deals on Booking.com.

The program interacts with the Booking.com website, accepting cookies, changing the currency to Euro, and prompting the user for the desired destination, check-in/check-out dates, and the number of people. It then performs a search, applies user-specified star rating filtrations, and sorts the results by the lowest price and best reviews.

The results are displayed in the command-line interface using the prettytable library, showing the hotel names, prices, and ratings. The program offers a convenient way to gather essential information about hotels in a user-friendly format.

-----------------------------------------------------------------------------------------------------------------

The Booking class is a subclass of webdriver.Chrome, which means it inherits all the properties and methods of the webdriver.Chrome class. It is used to create an instance of a Chrome WebDriver, which is a tool provided by Selenium for controlling a Chrome browser.

```python
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"D:/SeleniumDrivers", teardown=False):  #Constructor, change your path of the ChromeDriver
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)     #To instantiate the Chrome class
        self.implicitly_wait(15)
        self.maximize_window()
```

## In the __init__ method, the class constructor, several actions are performed:

-The driver_path argument specifies the path to the ChromeDriver executable. If no path is provided, it defaults to "D:/SeleniumDrivers".

-The teardown argument determines whether to quit the WebDriver when the context manager exits. If teardown is True, the WebDriver will be closed; otherwise, it will remain open.

-The environment variable PATH is updated to include the driver_path, ensuring that the ChromeDriver can be found by the system.

-An instance of webdriver.ChromeOptions is created, allowing for customization of Chrome's behavior.

-The experimental option 'excludeSwitches' with the value ['enable-logging'] is added to the options. This option disables logging, which can be useful to avoid cluttering the output.

-The superclass constructor (super()) is called to instantiate the webdriver.Chrome class with the provided options.

-An implicit wait of 15 seconds is set, which instructs the WebDriver to wait up to 15 seconds when attempting to find an element before raising a NoSuchElementException.

-The window is maximized, ensuring that the web page takes up the entire browser window.

 

## Besides the element identification methods used in the previous exercises,in this code you will also find:

-```find_element_by_xpath```: This method is used to locate elements on the web page by using XPath expressions.

```python
#Here I am using x_path because the button for EUR currency doesn't have unique attributes

currency_change = self.find_element_by_xpath(f'//button[.//span[contains(text(), "{currency}")]]')
currency_change.click()
        
#In this XPath expression, '//button' selects any button element in the document.
#The inner predicate '[.//span[contains(text(), "Euro")]]' filters the selection to only buttons that contain a 'span' element with the text "Euro", ensuring that the button specifically representing the Euro currency is targeted
```

```python
wait = WebDriverWait(self, 10)
first_result = wait.until(
       EC.visibility_of_element_located((By.XPATH, f'//div[contains(div/div, "{place_to_go}")]//button'))
        )
first_result.click()

#In this code, the XPath expression '//div[contains(div/div, "{place_to_go}")]//button' is used to locate the button element within the parent div.
#The expression div/div selects the nested <div> element that contains the text "Greece".
#Then, the //button part selects the button element within that context.
```

```python
# Here I used XPath because the class attribute of the button I wanted to press is not a unique value as it is used mainly for css styling.
# In the code below, the XPath expression selects the <input> tag with the specified id="group_adults".
# Then, using the following-sibling axis, it navigates to the adjacent <div> sibling, and within that <div>, it finds the <button> element.

     while True:
        decrease_adults_element=self.find_element_by_xpath('//input[@id="group_adults"]/following-sibling::div/button[@class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 cd7aa7c891"]')
        decrease_adults_element.click()
```

## Another new feature I used is the ```get_attribute``` method that retrieves the value of a specified attribute of an element, such as innerHTML to get the inner HTML text. This is used in order to create the table with the informations of the hotels from the first page.

```python
class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_css_selector(
            'div[data-testid="property-card"]'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            #Pulling the hotel name
            hotel_name = deal_box.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()  #Get the innerHTML text from an element

            hotel_price = deal_box.find_element_by_css_selector(
                'span[data-testid="price-and-discounted-price"]'
            ).get_attribute('innerHTML').strip().split('&nbsp;')[-1]

            try:
                hotel_rating = deal_box.find_element_by_css_selector(
                    'div[class="b5cd09854e f0d4d6a2f5 e46e88563a"]'
                ).get_attribute('innerHTML').strip()
            except:
                print("This hotel does not have a rating! ")

            collection.append(
                [hotel_name, hotel_price, hotel_rating]
            )

        return collection
```

Another smart idea when you want to find nested elements , instead of using the xpath, you can iterate over the child elements of an identified parent element:

```python
	def apply_star_rating(self, *star_values): # The syntax '*star_value' allows the method to accept multiple star values as input.
        star_filtration_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        for star_value in star_values:
            star_elements = star_filtration_box.find_elements_by_css_selector(
                f'div[data-filters-item="class:class={star_value}"]'
            )
            for star_element in star_elements:
                star_checkbox = star_element.find_element_by_css_selector('input[type="checkbox"]')
                if not star_checkbox.is_selected():
                    star_checkbox.click()
        #In the code above, the 'apply_star_rating' method selects the checkbox for the given star_values rating. It locates the parent div element with the attribute 'data-filters-group="class"' and finds the desired star elements using the attribute 'data-filters-item="class:class={star_value}"'.
        #Then, it locates the checkbox within each star element and checks if it's already selected before clicking on it.
```


Finally, in order to have a better perspective on what the code does, here is the run.py:

```python
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.implicitly_wait(3)
        bot.accept_cookie()
        bot.change_currency(currency='Euro')
        bot.close_popUp()
        bot.select_place_to_go(input("Where do you want to go ? "))
        bot.select_dates(check_in_date=input("What is the check in date ? (Ex: 2023-07-14) "),
                         check_out_date=input("What is the check out date ? (Ex: 2023-07-14) "))
        bot.select_adults(int(input("How many people ? ")))
        bot.click_search()
        bot.apply_filtrations()  #Modify in booking.py
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
```


The bot's performance may not always meet 100% expectations due to the inherent challenges of timing and synchronization in web automation and the presence of asynchronous behavior on websites. These factors can occasionally lead to unexpected behavior or issues during bot execution.
