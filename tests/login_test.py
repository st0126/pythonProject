import pytest
from utils.TestInfo import TestInfo
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect



def test_login(page: Page) -> None:
    lp = LoginPage(page)
    lp.login_enter()
    lp.fill_email("sdfsfs","이메일 주소를 정확하게 입력해 주세요.","유효하지 않은 아이디")
    lp.fill_email(TestInfo.userInfo['privateID'],comment = "유효한 아이디")
    lp.fill_pw("dsdss","비밀번호는 최소 8글자 이상 입력해 주세요.","유효하지 않은 패스워드")
    lp.fill_pw(TestInfo.userInfo['privatePW'],comment="유효한 패스워드")
    lp.click_login()


