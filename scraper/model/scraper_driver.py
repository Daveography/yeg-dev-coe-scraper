import logging
import os

from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


class ScraperDriver(WebDriver):
    def __init__(self):
        self.__logger = logging.getLogger(__name__)

        self.__logger.debug("Initializing Selenium WebDriver for scraping...")

        options = self.get_options()

        self.__logger.debug("Getting Chrome WebDriver...")
        executable_path = ChromeDriverManager().install()

        self.__logger.debug("Initializing WebDriver...")
        super().__init__(executable_path=executable_path, options=options)

        self.__logger.debug("WebDriver is ready")

    def get_options(self) -> ChromeOptions:
        options = ChromeOptions()
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--enable-automation")
        options.add_argument("--enable-javascript")
        options.add_argument("--no-sandbox")
        options.add_argument("--page-load-strategy=normal")
        options.add_argument(
            "--user-data-dir=" + os.path.abspath("./selenium")
        )  # enable cookies
        options.add_argument("--profile-directory=Default")
        # options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--headless")

        return options
