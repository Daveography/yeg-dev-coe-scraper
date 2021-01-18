from scraper.model.coe.common.tile import TileElement
from selenium.webdriver.remote.webelement import WebElement


class NeighbourhoodElement(TileElement):
    def __init__(self, element: WebElement) -> None:
        super().__init__(element)
