import logging
from typing import List

from scraper.model.coe.planning.neighbourhood import NeighbourhoodElement
from scraper.model.coe.planning.project import ProjectElement
from scraper.model.coe.planning.ward import WardElement
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

        self.__ward_elements = self._driver.find_elements_by_xpath(
            "//div[contains(concat(' ', normalize-space(@class), ' '), ' accordion__section ')]"
        )

    def get_all_wards(self) -> List[WardElement]:
        return [WardElement(element) for element in self.__ward_elements]


class NeighbourhoodApplicationsPage(BasePage):
    def __init__(self, driver: WebDriver, neighbourhood: NeighbourhoodElement):
        super().__init__(driver)

        self.neighbourhood = neighbourhood
        self.url = self.neighbourhood.url

        self._logger.info(
            f"Loading Applications page for {self.neighbourhood.title}..."
        )
        self._driver.get(self.url)

        self.__proposed_projects_elements = self._driver.find_elements_by_xpath(
            "//h2[text()='Proposed']"
            "/following-sibling::div[@class='accordion']"
            "/div[contains(concat(' ', normalize-space(@class), ' '), 'accordion__section')]"
        )

    def get_all_proposed_projects(self) -> List[ProjectElement]:
        return [
            ProjectElement(element) for element in self.__proposed_projects_elements
        ]
