from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

firefox_options = Options()
firefox_options.add_argument("--headless")  # CLI environment

#driver = webdriver.Chrome('/Users/armian/Inflearn/workspace/section3/webdriver/chrome/chromedriver')
driver = webdriver.Firefox(firefox_options=firefox_options, executable_path='/Users/armian/Inflearn/workspace/section3/webdriver/firefox/geckodriver')
#driver.set_window_size(1920,1280)

#driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)

driver.save_screenshot('/Users/armian/tmp/website1_ff.png')

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)

driver.save_screenshot('/Users/armian/tmp/website2_ff.png')

driver.quit()

print('스크린샷 완료')
