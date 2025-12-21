import re
from playwright.sync_api import Page, expect

def test_navigate(page: Page):
    page.goto("https://demoqa.com/")

def test_to_have_title(page: Page):
    page.goto("https://demoqa.com/")
    expect(page.title).to_have_title(re.compile("DEMOQA"))