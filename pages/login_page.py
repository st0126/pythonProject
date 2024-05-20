from utils.TestInfo import TestInfo
from pages.main_page import MainPage, Page

class LoginPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.id = 0
        self.name = "LOGIN"

    # button

    btn_login = '//button[text()="로그인"]'

    input_id = '//*[@id="email"]'
    val_id = '//*[@id="email"]/parent::div/following-sibling::span'
    input_pw = '//*[@id="password"]'
    val_pw = '//*[@id="password"]/parent::div/following-sibling::span'

    def login_enter(self):
        self.page.goto(TestInfo.URL["LOGIN"])
        self.compare_title("굿바이브웍스 GoodVibeWorks - 로그인", "타이틀 확인")
        self.compare_url("LOGIN", "로그인 페이지 이동")

    def fill_email(self, email, expect_msg= "", comment= ""):
        self.get_loc(self.input_id).fill(email)
        self.check_validation(self.val_id, expect_msg, comment)

    def fill_pw(self, pw, expect_msg= "", comment= ""):
        self.get_loc(self.input_pw).fill(pw)
        self.check_validation(self.val_pw, expect_msg, comment)

    def click_login(self):
        self.get_loc(self.btn_login).click()
        self.compare_url("MY_PAGE", "메인 페이지 이동")