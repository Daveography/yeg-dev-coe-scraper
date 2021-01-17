import logging
from scraper.model.coe.planning.project_profile import ProjectProfileElement
from typing import List
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._logger = logging.getLogger(__name__)


class PlanningApplicationsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        self.url = "https://www.edmonton.ca/residential_neighbourhoods/neighbourhoods/planning-applications.aspx"  # noqa E501

        self._logger.info("Loading Planning Applications page...")
        self._driver.get(self.url)

    def get_all_neighbourhood_urls(self) -> List[str]:
        return [
            link.get_attribute("href")
            for link in self._driver.find_elements_by_xpath(
                "//div[@class='tiles__tile']/a"
            )
        ]


class NeighbourhoodApplicationsPage(BasePage):
    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver)

        self.url = url

        self._logger.info("Loading Neighbourhood Applications page...")
        self._driver.get(self.url)

    def get_all_proposed_projects(self) -> List[ProjectProfileElement]:
        return [
            ProjectProfileElement(element)
            for element in self._driver.find_elements_by_xpath(
                "//h2[text()='Proposed']"
                "/following-sibling::div[@class='accordion']"
                "/div[contains(@class,'accordion__section')]"
            )
        ]
