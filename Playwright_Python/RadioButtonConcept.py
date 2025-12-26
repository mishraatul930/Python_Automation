import re
import time

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://demoqa.com/")
    yield

    print("after the test runs")

def test_to_click_radio_button(page: Page):
    page.get_by_role("heading", name="Elements").click()
    page.wait_for_timeout(5000)
    page.locator("//span[@class='text' and normalize-space() = 'Radio Button']").click()
    page.wait_for_timeout(5000)
    # page.get_by_label("Yes").check()
    page.locator("label", has_text="Yes").click()
    page.wait_for_timeout(5000)
    # page.get_by_label("Impressive").check()
    page.locator("label", has_text="Impressive").click()
    page.wait_for_timeout(5000)