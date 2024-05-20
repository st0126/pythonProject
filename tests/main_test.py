import pytest

from playwright.sync_api import expect, Page
from pages.main_page import MainPage


# @pytest.mark.skip   #함수 스킵
def test_main(page: Page) -> None:
    mp = MainPage(page)
    mp.click_login()








