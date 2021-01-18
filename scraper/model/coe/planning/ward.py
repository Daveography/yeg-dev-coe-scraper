from typing import List

from scraper.model.coe.common.accordion_section import AccordionSectionElement
from scraper.model.coe.planning.neighbourhood import NeighbourhoodElement
from selenium.webdriver.remote.webelement import WebElement


class WardElement(AccordionSectionElement):
    def __init__(self, element: WebElement) -> None:
        super().__init__(element)

        if not self.title.startswith("Ward"):
            raise Exception("Accordion section is not a Ward")

        self.__neighbourhood_elements = element.find_elements_by_class_name(
            "tiles__tile"
        )

        self.neighbourhoods = [
            NeighbourhoodElement(element) for element in self.__neighbourhood_elements
        ]
