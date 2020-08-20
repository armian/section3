from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class NcafeWrtieAtt:
    # 초기화 실행
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") # CLI (User-agent)
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/Users/armian/Inflearn/workspace/section3/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(5)

    # 네이버 카페 로그인 && 출석 체크
    def writeAttendCheck(self):
        self.driver.get("https://nid.naver.com/nidlogin.login")
        self.driver.find_element_by_name('id').send_keys('user')
        self.driver.find_element_by_name('pw').send_keys('pass')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.implicitly_wait(30)
        # 아래 URL은 개발자도구 -> 네트워크 -> preserve log를 통해서 얻어낸다.
        # 실제로 네이버는 iframe을 사용하므로, 아래 URL이 보이지 않는다.
        self.driver.get('http://cafe.naver.com/paramsx?iframe_url=......')
        self.driver.implicitly_wait(30)
        # '출석' 쓰기 영역은 iframe에 있으므로, 위 URL에 없으므로, 아래와 같이 가져와야 함
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다!!.')
        self.driver.find_element_by_xpath('//....').click()  # '출석하기' 버튼
        time.sleep(3)

    # 소멸자
    def __del__(self):
        # self.driver.close() # 현재 실행 포커스 된 영역을 종료
        self.driver.quit()  # Selenium 전체 프로그램 종료
        print("Removed driver Object")

# 실행
if __name__ == "__main__":
    # 객체 생성
    a = NcafeWrtieAtt()
    # 시작 시간
    start_time = time.time()

    # 프로그램 실행
    a.writeAttendCheck()

    # 종료 시간
    print("---Total {} seconds ---".format(time.time() - start_time))
    # 객체 소멸
    del a
