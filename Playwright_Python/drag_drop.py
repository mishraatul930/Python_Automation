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

def test_drag_drop(page: Page):
    page.get_by_role("heading", name="Elements").click()
    page.wait_for_timeout(5000)
    page.locator("//div[@class='header-text' and text()='Interactions']").click()
    page.wait_for_timeout(5000)
    # page.get_by_text("Text Box", exact=True).click()
    page.locator("//span[@class='text' and normalize-space() = 'Droppable']").click()
    page.wait_for_timeout(5000)
    page.locator("//div[@id='draggable']").drag_to(page.locator("//div[@id='droppableExample-tabpane-simple']//div[@id='droppable']"))
    page.wait_for_timeout(5000)