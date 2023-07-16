import booking.constants as const
import os
import time
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

    #Context Manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    def land_first_page(self):
        self.get(const.BASE_URL)

    def accept_cookie(self):
        accept=self.find_element_by_id('onetrust-accept-btn-handler')
        accept.click()

    # I ended up using implicit wait because it is faster (NOT RECOMMENDED)
    def close_popUp(self):
        try:
            close=self.find_element_by_css_selector(
                'button[aria-label="Dismiss sign-in info."]'
            )
            close.click()
        except:
            print('PopUp did not show')

    #In the code below, an instance of WebDriverWait is created with a timeout of 1 seconds
    #The 'EC.presence_of_element_located' condition is used to wait for the presence of the element specified by the CSS selector.
    # def close_popUp(self):
    #     try:
    #         wait = WebDriverWait(self, 1)
    #         close = wait.until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')))
    #         close.click()
    #     except TimeoutException:
    #         print('close_popUp skipped')

    def change_currency(self, currency=None):
        currency_element=self.find_element_by_css_selector(
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        #Here I am using x_path because the button for EUR currency doesn't have unique attributes
        currency_change = self.find_element_by_xpath(f'//button[.//span[contains(text(), "{currency}")]]')
        currency_change.click()
        #In this XPath expression, '//button' selects any button element in the document.
        #The inner predicate '[.//span[contains(text(), "Euro")]]' filters the selection to only buttons that contain a 'span' element with the text "Euro", ensuring that the button specifically representing the Euro currency is targeted

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_name('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        wait = WebDriverWait(self, 10)
        first_result = wait.until(
            EC.visibility_of_element_located((By.XPATH, f'//div[contains(div/div, "{place_to_go}")]//button'))
        )
        first_result.click()
        #In this code, the XPath expression '//div[contains(div/div, "{place_to_go}")]//button' is used to locate the button element within the parent div.
        #The expression div/div selects the nested <div> element that contains the text "Greece".
        #Then, the //button part selects the button element within that context.

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'span[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'span[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count):
        selection_element = self.find_element_by_css_selector(
            f'button[data-testid="occupancy-config"]'
        )
        selection_element.click()
        # Here I used XPath because the class attribute of the button I wanted to press is not a unique value as it is used mainly for css styling.
        # In the code below, the XPath expression selects the <input> tag with the specified id="group_adults".
        # Then, using the following-sibling axis, it navigates to the adjacent <div> sibling, and within that <div>, it finds the <button> element.
        while True:
            decrease_adults_element=self.find_element_by_xpath('//input[@id="group_adults"]/following-sibling::div/button[@class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 cd7aa7c891"]')
            decrease_adults_element.click()

            adults_value_element = self.find_element_by_css_selector(
                'input[id="group_adults"]'
            )
            adults_value = adults_value_element.get_attribute('value')
            # If the value of adults reaches 1, then we should get out of the while loop
            if int(adults_value) == 1:
                break

        increase_adults_element = self.find_element_by_xpath(
            '//input[@id="group_adults"]/following-sibling::div/button[@class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 d64a4ea64d"]')

        for i in range(count - 1):
            increase_adults_element.click()

    def click_search(self):
        search_button=self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        stars_input = input(
            "How many stars do you want the hotel to have? (If multiple values, separate them by space!) ")
        stars_list = stars_input.split()  # Split the input values by a space
        filtration.apply_star_rating(*stars_list)  # Pass the star values as separate arguments using the * operator
        time.sleep(3)  # Pause for 3 seconds
        filtration.sort_lowestPrice_bestReviews()
        time.sleep(3)

    #We search for the parent div that contains all the hotels div elements
    def report_results(self):
        hotel_boxes = self.find_element_by_id(
            'search_results_table'
        )
        report = BookingReport(hotel_boxes)

        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Rating"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)





