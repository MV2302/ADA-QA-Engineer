
from xml.dom.minidom import Element
from selenium import webdriver

driver=webdriver.Safari()


driver.get("https://testpages.herokuapp.com/styled/index.html")

element1=driver.find_element_by_partial_link_text("Dynamic Buttons Challenge 01")
element1.click()
element2=driver.find_element_by_partial_link_text("Index")
element2.click()