import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/python/docs/input")
    yield

    print("after the test runs")

def test_footer(page: Page):
    page.locator("//footer[@class='theme-layout-footer footer footer--dark']").hover()
    page.wait_for_timeout(5000)
    page.mouse.wheel(0,10)
    page.wait_for_timeout(5000)