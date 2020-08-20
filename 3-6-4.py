from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

#chrome_options = Options()
#chrome_options.add_argument("--headless")  # CLI environment

driver = webdriver.Chrome('/Users/armian/Inflearn/workspace/section3/webdriver/chrome/chromedriver')
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/armian/Inflearn/workspace/section3/webdriver/chrome/chromedriver')
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F')
time.sleep(7)
driver.implicitly_wait(3)

driver.find_element_by_name('log').send_keys('cysoo')
driver.implicitly_wait(1)
driver.find_elemnet_by_name('pwd').send_keys('pwd')
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="wp-submit"]').click()




driver.quit()

print('스크린샷 완료')
