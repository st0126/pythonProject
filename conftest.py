import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    iphone_13 = playwright.devices['iPhone 13 Pro']
    pixel_4 = playwright.devices['Pixel 4']
    return {
        **browser_context_args,
        # **iphone_13,
        "viewport": {
            "width": 1700,
            "height": 750,
        }
    }
