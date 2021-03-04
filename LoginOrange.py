from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

Username = 'admin'
Password = 'admin123'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://orangehrm-demo-6x.orangehrmlive.com/auth/login")

user_input = driver.find_elements_by_id('txtUsername')
user_input.send_keys(Username)

password_input = driver.find_elements_by_id('txtPassword')
password_input.send_keys(Password)

login_button = driver.find_elements_by_id('btnLogin')
login_button.click()