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

# def test_navigate(page: Page):
#     page.context.set_viewport_size({"width": 1920, "height": 1080})
#     page.goto("https://demoqa.com/")

def test_to_have_title(page: Page):
    # page.goto("https://demoqa.com/")
    expect(page).to_have_title(re.compile("DEMOQA"))

def test_to_click_on_element(page: Page):
    # page.goto("https://demoqa.com/")
    page.get_by_role("heading", name="Elements").click()
    time.sleep(5)
    # page.get_by_text("Text Box", exact=True).click()
    page.locator("//span[@class='text' and normalize-space() = 'Text Box']").click()
    time.sleep(5)

def test_to_fill_elements(page: Page):
    page.get_by_role("heading", name="Elements").click()
    time.sleep(5)
    # page.get_by_text("Text Box", exact=True).click()
    page.locator("//span[@class='text' and normalize-space() = 'Text Box']").click()
    page.wait_for_timeout(5000)
    page.locator("//input[@id='userName']").fill("Atul Mishra")
    page.wait_for_timeout(5000)
    page.locator("//input[@id='userEmail']").fill("mishraatul2796@gmail.com")
    page.wait_for_timeout(5000)
    page.locator("//textarea[@id='currentAddress']").fill("ABCD Lane No - 40, GHJK Town, Pincode-831001")
    page.wait_for_timeout(5000)
    page.locator("//textarea[@id='permanentAddress']").fill("ABCD Lane No - 40, GHJK Town, Pincode-831001")
    page.wait_for_timeout(5000)
    page.locator("//button[@id='submit']").click()