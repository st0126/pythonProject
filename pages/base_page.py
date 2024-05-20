from datetime import datetime
from playwright.sync_api import Page, expect
from utils.TestInfo import TestInfo
import utils.LogManager as Lm


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.id = 0
        self.name = 'TEST'

    # 로그 관련
    def get_id(self) -> str:
        self.id += 1
        return f"{self.name}_{str(self.id).zfill(3)}"

    def log(self, result: bool, comment=''):
        if result is False:
            fileName = f"ss_{self.name.lower()}_{datetime.today().strftime('%m%d%H%M%S')}"
            self.page.screenshot(path=fileName)
            Lm.send_msg(comment, fileName)
        if comment != "":
            Lm.log(self.get_id(), result, comment)

    # 기본 기능
    def goto_url(self, link: str, comment=""):
        self.page.goto(link)
        if comment != "":
            self.log(link in self.page.url, comment)
            try:
                assert link in self.page.url, f"not expected url : {self.page.url}"
            except:
                Lm.log(self.get_id(), False, f"not expected url : {self.page.url}")

    def wait(self, time=1, selector='', state=''):
        if state is not None:
            self.page.wait_for_load_state(state)
        elif selector is not None:
            self.page.wait_for_selector(selector)
        else:
            self.page.wait_for_timeout(time*1000)

    def scroll_page(self, x_pos=0, y_pos=100):
        self.page.mouse.wheel(x_pos, y_pos)

    def get_loc(self, loc_name: str, loc_nth=0, focus=False):
        loc = self.page.locator(loc_name).nth(loc_nth)
        assert loc, f"locator '{loc_name}' not found"
        if loc.is_visible() and focus is True:
            loc.focus()
        return loc

    def fill_text(self, input_name: str, text=""):
        self.get_loc(input_name).fill(text)

    def check_validation(self, loc_name, expect_text="", comment="") -> bool:
        loc = self.get_loc(loc_name)
        assert loc, f"locator '{loc}' not found"
        if expect_text == "":
            self.log(loc.is_hidden(), comment)
        else:
            self.log(loc.inner_text() == expect_text, f"{comment} : {expect_text}")

    def check_btn_state(self, loc_name, expect_isEnabled: bool, comment=""):
        loc = self.get_loc(loc_name)
        assert loc, f"locator '{loc}' not found"
        self.log(loc.is_enabled() == expect_isEnabled, comment)

    # 비교
    def compare(self, compare_res, comment=""):
        self.log(compare_res, comment)

    def compare_loc_text(self, loc_name: str, text: str, comment=""):
        loc_text = self.get_loc(loc_name).inner_text()
        self.log(loc_text == text, comment)
        if loc_text != text:
            print(loc_text)
            print(text)

    def compare_loc_value(self, loc_name: str, value: str, comment=""):
        loc_value = self.get_loc(loc_name).input_value()
        self.log(loc_value == value, comment)
        if loc_value != value:
            print(f"{loc_value}")
            print(f"{value}")

    def compare_title(self, expect_title: str, comment=""):
        if expect_title not in self.page.title():
            print(expect_title, self.page.title())
        self.log(expect_title in self.page.title(), comment)

    def compare_url(self, expect_url_id: str, comment=""):
        expect(self.page).to_have_url(TestInfo.URL[expect_url_id])
        if comment != "":
            self.log(TestInfo.URL[expect_url_id] in self.page.url, comment)

    def compare_attribute(self, loc_name: str, attribute: str, expect_value, comment=""):
        loc = self.get_loc(loc_name)
        self.log(loc.get_attribute(attribute) == expect_value, comment)

    def new_tab(self) -> Page:
        return self.page.context.new_page()


