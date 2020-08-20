from bs4 import BeautifulSoup
import requests

# 로그인 유저정보
LOGIN_INFO = {
    'user_id' : 'armian',
    'user_pw' : '!Dkfmaldks'
}

# Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc', data=LOGIN_INFO)
    """
    # HTML 소스 확인
    print('login_req', login_req.text)
    # HEADER 확인
    print('header', login_req.headers)
    """
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://bbs.ruliweb.com/market/board/32/read/4749310?')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, "html.parser")
        #print(soup.prettify())
        article = soup.select_one("#board_read > div > div.board_main > div.board_main_view > div.view_content.autolink > div").find_all('p')
        #print(article)
        for i in article:
            if i.string is not None:
                print(i.string)
