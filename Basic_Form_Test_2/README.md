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