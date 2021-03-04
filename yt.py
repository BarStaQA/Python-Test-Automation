from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://www.youtube.pl")

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('david guetta')

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
searchButton.click()