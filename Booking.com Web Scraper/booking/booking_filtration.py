#This file will include a class with instance methods
#That will be responsible to interact with booking website
#After we have some results, to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver #The compiler doesn't know the type of the driver from constructor, so the autocomplete feature isn't working, and this is the fix

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    #Another way to find nested elements instead of xpath!
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

    def sort_lowestPrice_bestReviews(self):
        element_sortBy = self.driver.find_element_by_css_selector(
            'button[data-testid="sorters-dropdown-trigger"]'
        )
        element_sortBy.click()

        sort_by_lowest_price = self.driver.find_element_by_css_selector(
            'button[data-id="review_score_and_price"]'
        )
        sort_by_lowest_price.click()

