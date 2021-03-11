from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')

driver.get('http://automationpractice.com/index.php')
search = driver.find_elements_by_id('search_query_top')
search.send_Keys("dress", Keys.ENTER)
