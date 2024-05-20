from pages.base_page import BasePage, Page, expect
from utils.TestInfo import TestInfo


class AdminPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.id = 0
        self.name = 'ADMIN'
        self.load()

    inp_id = '//*[@id="email"]'
    inp_pw = '//*[@id="password"]'

    btn_login = '//*[text()="Login"]'
    btn_resetPW = '//a[text()="パスワード再設定"]'
    btn_join = '//a[text()="認証及び会員登録"]'

    mail_title = {
        "FINDPW": '[EnergyShares] パスワード再設定用のメールです。',
        "JOIN": '[EnergyShares] 会員登録用の認証メールです。'
    }

    def load(self):
        self.page.goto(TestInfo.URL["ADMIN"])
        self.get_loc(self.inp_id).fill(TestInfo.adminInfo['ID'])
        self.get_loc(self.inp_pw).fill(TestInfo.adminInfo['PW'])
        self.get_loc(self.btn_login).click()

    def get_sendmail_link(self, mail_type: str, mail_id: str) -> str:
        expect(self.page).to_have_url(TestInfo.URL["ADMIN_dashboard"])
        self.page.goto(TestInfo.URL["ADMIN_mail"])
        mail = self.page.get_by_role("cell", name=self.mail_title[mail_type]).nth(0)
        assert mail, "No mail recv"

        mail.click()
        if self.page.get_by_text(mail_id) is None:
            self.log(False, "수신회원 동일하지 않음")
            return ""
        else:
            if mail_type == "FINDPW":
                return self.get_loc(self.btn_resetPW).get_attribute("href")
            elif mail_type == "JOIN":
                return self.get_loc(self.btn_join).get_attribute("href")
            else:
                pass





