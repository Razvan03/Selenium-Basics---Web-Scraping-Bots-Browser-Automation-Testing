#This file is going to include method that will parse
#The specific data that we need from each one of the deal boxes
from selenium.webdriver.remote.webelement import WebElement

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

