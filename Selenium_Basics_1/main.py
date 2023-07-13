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