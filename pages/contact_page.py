from pages.main_page import MainPage, Page


class ContactPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.id = 0
        self.name = "CONTACT"

    btn_send = '//button[text()="送信"]'

    inp_name = '//*[@id="name"]'
    inp_email = '//*[@id="email"]'
    inp_contents = '//*[@id="contents"]'

    val_name = '//*[@id="name"]/following-sibling::span'
    val_email = '//*[@id="email"]/following-sibling::span'
    val_contents = '//*[@id="contents"]/following-sibling::span'

    def fill_name(self, name):
        self.get_loc(self.inp_name).fill(name)

    def fill_email(self, email):
        self.get_loc(self.inp_email).fill(email)

    def fill_contents(self, content):
        self.get_loc(self.inp_contents).fill(content)

    def check_name_validation(self, expect="", comment=""):
        self.check_validation(self.val_name, expect, comment)

    def check_email_validation(self, expect="", comment=""):
        self.check_validation(self.val_email, expect, comment)

    def check_contents_validation(self, expect="", comment=""):
        self.check_validation(self.val_contents, expect, comment)

    def click_send_btn(self):
        self.get_loc(self.btn_send).click()

