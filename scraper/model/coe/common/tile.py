from selenium.webdriver.remote.webelement import WebElement


class TileElement():
    def __init__(self, element: WebElement) -> None:
        if "tiles__tile" not in element.get_attribute("class"):
            raise Exception("Element is not a tile")

        self._link_element: WebElement = element.find_element_by_xpath("a")
        self._title_element: WebElement = self._link_element.find_element_by_tag_name("h2")
        self._summary_element: WebElement = self._link_element.find_element_by_tag_name("p")

        self.title: str = self._title_element.text
        self.summary: str = self._summary_element.text
        self.url: str = self._link_element.get_attribute("href")
