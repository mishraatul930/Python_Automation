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

def test_to_click_checkbox(page: Page):
    page.get_by_role("heading", name="Elements").click()
    time.sleep(5)
    # page.get_by_text("Text Box", exact=True).click()
    page.locator("//span[@class='text' and normalize-space() = 'Text Box']").click()
    page.wait_for_timeout(5000)
    page.locator("//span[@class='text' and normalize-space() = 'Check Box']").click()
    page.wait_for_timeout(5000)
    page.locator("//span[@class='rct-title' and text() = 'Home']").click()