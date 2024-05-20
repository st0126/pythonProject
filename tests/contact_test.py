import pytest

from playwright.sync_api import Page
from pages.contact_page import ContactPage


def test_contact(page: Page) -> None:
    page = ContactPage(page)

    page.goto_contact_page()

    page.check_banner_UI("contact")

    page.click_send_btn()

    # empty input validation
    req_data = "필수항목입니다."

    page.check_name_validation(req_data, "이름 하단 안내문구 노출")
    page.check_email_validation(req_data, "이메일 하단 안내문구 노출")
    page.check_contents_validation(req_data, "내용 하단 안내문구 노출")

    # Input
    name = "song"
    email = "dd@dd.dom"
    contents = "ddd"

    page.check_name_validation(expect="error msg", comment="스크린샷 테스트용 Fail 발생")

    page.fill_name(name)
    page.check_name_validation(comment="이름 입력 후 하단 안내문구 미노출")

    page.fill_email(email)
    page.check_email_validation(comment="이메일 입력 후 하단 안내문구 미노출")

    page.fill_contents(contents)
    page.check_contents_validation(comment="내용 입력 후 하단 안내문구 미노출")

