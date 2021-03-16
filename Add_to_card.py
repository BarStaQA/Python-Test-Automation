from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='D:\QA_Tester\Automation Test Python\PyCharm\chromedriver.exe')


driver.get('http://automationpractice.com/index.php')
search_input = driver.find_element_by_name('search_query')
search_input.send_keys('dress')

search_btn = driver.find_element_by_name('submit_search')
search_btn.click()

choose_btn = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]')
choose_btn.click()

close_btn = driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span')
close_btn.click()