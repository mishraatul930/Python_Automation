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

def test_file_upload(page: Page):
    page.get_by_role("heading", name="Elements").click()
    time.sleep(5)
    # page.get_by_text("Text Box", exact=True).click()
    page.locator("//span[@class='text' and normalize-space() = 'Upload and Download']").click()
    page.wait_for_timeout(5000)
    page.get_by_label("Select a file").set_input_files("/Users/atulmishra/Documents/main.py")
    page.wait_for_timeout(5000)

def test_another_file_upload_button(page: Page):
    page.get_by_role("heading", name="Elements").click()
    page.wait_for_timeout(5000)
    page.locator("//span[@class='text' and normalize-space() = 'Upload and Download']").click()
    page.wait_for_timeout(5000)
    with page.expect_file_chooser() as fc_info:
        page.get_by_label("Select a file").click()
    file_chooser = fc_info.value
    file_chooser.set_files("/Users/atulmishra/Documents/main.py")
    page.wait_for_timeout(5000)