from selenium import webdriver

driver = webdriver.Chrome('/Users/armian/Inflearn/workspace/section3/webdriver/chrome/chromedriver')

driver.implicitly_wait(5)

driver.get('https://google.com')
driver.save_screenshot('/Users/armian/tmp/website1.png')

driver.implicitly_wait(5)

driver.get('https://www.daum.net')
driver.save_screenshot('/Users/armian/tmp/website2.png')

driver.quit()

print('스크린샷 완료')
