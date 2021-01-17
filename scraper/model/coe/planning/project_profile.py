from selenium.webdriver.remote.webelement import WebElement


class ProjectProfileElement():
    def __init__(self, element: WebElement) -> None:
        if "accordion__section" not in element.get_attribute("class"):
            raise Exception("Element is not a project profile")

        title_element: WebElement = element.find_element_by_xpath(
            "a[contains(@class,'accordion__section__title')]/span"
        )
        content_element: WebElement = element.find_element_by_class_name("text-content")

        self.title: str = title_element.text
        self.summary: str = content_element.text
