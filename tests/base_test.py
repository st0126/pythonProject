import pytest

from playwright.sync_api import Page, expect
from pages.base_page import BasePage


def test_Base(page: Page) -> None:
    p = BasePage(page)
    p.log(True, "test log 1")
    p.log(True, "test log 2")
    p.log(False, "test log Error 1")
    p.log(True, "test log 3")
    p.log(False, "test log Error 2")
    p.log(False, "test log Error 3")


