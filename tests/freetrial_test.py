import pytest
from utils.TestInfo import TestInfo
from pages.freetrial_page import FreetrialPage
from playwright.sync_api import Page, expect


def test_ft(page: Page) -> None:
    lp = FreetrialPage(page)


