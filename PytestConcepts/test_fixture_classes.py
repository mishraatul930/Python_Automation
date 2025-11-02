from sys import executable

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(scope="class")
def init_driver(request):
    service = ChromeService(ChromeDriverManager().install())
    ch_driver = webdriver.Chrome(service=service)
    request.cls.driver = ch_driver
    yield
    ch_driver.quit()

@pytest.fixture(scope="class")
def init_ff_driver(request):
    service = FirefoxService(GeckoDriverManager().install())
    ff_driver = webdriver.Firefox(service=service)
    request.cls.driver = ff_driver
    yield
    ff_driver.quit()

@pytest.mark.usefixtures("init_driver")
class Base_Test:
    pass

class Test_Google_Chrome(Base_Test):

    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google", "Title does not match"


# @pytest.mark.usefixtures("init_ff_driver")
# class Base_FF_Test:
#     pass
#
# class Test_Google_FF(Base_FF_Test):
#
#     def test_google_title(self):
#         self.driver.get("https://www.google.com")
#         assert self.driver.title == "Google", "Title does not match"