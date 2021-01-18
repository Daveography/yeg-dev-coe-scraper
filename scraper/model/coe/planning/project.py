from scraper.model.coe.common.accordion_section import AccordionSectionElement
from selenium.webdriver.remote.webelement import WebElement


class ProjectElement(AccordionSectionElement):
    def __init__(self, element: WebElement) -> None:
        super().__init__(element)

        self.__summary_element: WebElement = element.find_element_by_class_name(
            "text-content"
        )

        self.summary: str = self.__summary_element.text
