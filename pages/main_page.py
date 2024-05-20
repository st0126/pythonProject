from utils.TestInfo import TestInfo
from pages.base_page import BasePage, Page, expect


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.id = 0
        self.name = 'MAIN'
        self.load()


    #input
    #inp_displaycode = '//input[@type="password"]'

    # button
    btn_login = '//a[text()="로그인"]'
    btn_ft = '//button[text()="무료 체험 신청"]'

    def load(self):
        self.page.goto(TestInfo.URL["MAIN"])

    def click_login(self):
        self.get_loc(self.btn_login).click()
        self.compare_url("LOGIN","로그인 페이지 이동")

    def click_ft(self):
        self.get_loc(self.btn_ft).click()
        self.compare_url("?","무료체험신청 페이지 이동")


    # header
    nav_main_logo = '//h1/a[@href="/"]'




    def click_mainLogo(self):
        self.get_loc(self.nav_main_logo).click()
        self.log(TestInfo.URL["USER"] is self.page.url)

    def check_banner_UI(self, text):
        # Title
        self.compare_title(text['banner']['title'], "페이지 타이틀 확인")
        # Banner Text
        self.compare_loc_text(self.txt_title, text['banner']['title'], "배너 타이틀 확인")
        self.compare_loc_text(self.txt_content, text['banner']['content'], "배너 설명 확인")

    def goto_green_energy_page(self):
        self.get_loc(self.nav_greenenergy).click()
        self.compare_url('green_energy', "green_energy 페이지 이동")

    def goto_fund_list_page(self):
        self.get_loc(self.nav_fundlist).click()
        self.compare_url('fund_list', "fund_list 페이지 이동")

    def goto_user_guide_page(self):
        self.get_loc(self.nav_userguide).click()
        self.compare_url('user_guide', "user_guide 페이지 이동")

    def goto_faq_page(self):
        self.get_loc(self.nav_faq).click()
        self.compare_url('faq', "faq 페이지 이동")

    def goto_news_page(self):
        self.get_loc(self.nav_news).click()
        self.compare_url('news', "news 페이지 이동")

    def goto_about_page(self):
        self.get_loc(self.nav_about).click()
        self.compare_url('about', "about 페이지 이동")

    def goto_contact_page(self):
        self.get_loc(self.nav_contact).click()
        self.compare_url('contact', "contact 페이지 이동")

    def goto_login_page(self):
        loc = self.get_loc(self.nav_login)
        if loc.inner_text() == "ログイン":
            loc.click()
        else:
            print("user_page > goto_login_page : not ready to login")

        self.compare_url('login', "login 페이지 이동")
