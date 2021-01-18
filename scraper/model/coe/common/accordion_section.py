from selenium.webdriver.remote.webelement import WebElement


class AccordionSectionElement:
    def __init__(self, element: WebElement) -> None:
        if "accordion__section" not in element.get_attribute("class"):
            raise Exception("Element is not an accordion section")

        self._element = element

        self._header_element: WebElement = self._element.find_element_by_xpath(
            "a[contains(concat(' ', normalize-space(@class), ' '), ' accordion__section__title ')]"
        )

        # Expand the accordian if not already expanded
        if "active" not in self._element.get_attribute("class"):
            self._header_element.click()

        title_element: WebElement = self._header_element.find_element_by_tag_name("span")

        self._content_element: WebElement = self._element.find_element_by_xpath(
            "div[contains("
            "concat(' ', normalize-space(@class), ' '),' accordion__section__content '"
            ")]"
        )

        self.title: str = title_element.text
