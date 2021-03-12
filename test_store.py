from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:\Quality Assurance Tester\Automation Test Python\PyCharm\chromedriver.exe')


driver.get('http://automationpractice.com/index.php')
search_input = driver.find_element_by_name('search_query')
search_input.send_keys('dress')

search_btn = driver.find_element_by_name('submit_search')
search_btn.click()