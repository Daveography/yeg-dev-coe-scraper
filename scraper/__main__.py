import logging

import scraper.model.coe.planning.pages as pages
from scraper.model.scraper_driver import ScraperDriver


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
    all_wards = planning_page.get_all_wards()

    for ward in all_wards:
        for neighbourhood in ward.neighbourhoods:
            neighbourhood_page = pages.NeighbourhoodApplicationsPage(
                driver, neighbourhood
            )

            [
                logger.info(
                    f"{ward.title} - {neighbourhood.title} - {project.title}"
                )
                for project in neighbourhood_page.get_all_proposed_projects()
            ]


main()
