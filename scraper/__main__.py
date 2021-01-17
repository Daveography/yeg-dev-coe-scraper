import logging
from typing import List
from scraper.model.coe.planning.project_profile import ProjectProfileElement
from scraper.model.scraper_driver import ScraperDriver
import scraper.model.coe.planning.pages as pages


def main():
    # Logger setup
    logformat = (
        "[%(levelname)s] %(asctime)s G- %(name)s"
        "- %(funcName)s: line %(lineno)d: %(message)s"
    )
    logging.root.handlers = []
    logging.basicConfig(
        format=logformat,
        datefmt="%H:%M:%S",
        level=logging.INFO,
        handlers=[
            logging.StreamHandler(),
        ],
    )
    logger = logging.getLogger(__name__)

    driver = ScraperDriver()
    planning_page = pages.PlanningApplicationsPage(driver)
    all_nbhds = planning_page.get_all_neighbourhood_urls()

    planning_projects: List[ProjectProfileElement] = []

    for nbhd in all_nbhds:
        nbhd_page = pages.NeighbourhoodApplicationsPage(driver, nbhd)
        planning_projects.extend(nbhd_page.get_all_proposed_projects())

    [logger.info(project.title) for project in planning_projects]


main()
