from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # CLI environment

#driver = webdriver.Chrome('/Users/armian/Inflearn/workspace/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/armian/Inflearn/workspace/section3/webdriver/chrome/chromedriver')
#driver.set_window_size(1920,1280)

#driver.implicitly_wait(5)

driver.get('https://google.com')
#time.sleep(5)

driver.save_screenshot('/Users/armian/tmp/website1_ch.png')

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')
#time.sleep(5)

driver.save_screenshot('/Users/armian/tmp/website2_ch.png')

driver.quit()

print('스크린샷 완료')
