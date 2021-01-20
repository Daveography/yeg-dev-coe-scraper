import logging
from argparse import ArgumentParser
from datetime import datetime
from typing import List

import scraper.model.coe.planning.pages as pages
from scraper.infrastructure.persistence.db_context import DbContext
from scraper.model.coe.planning.db.planning_project import PlanningProject
from scraper.model.coe.planning.project import ProjectElement
from scraper.model.scraper_driver import ScraperDriver


def main():
    args = parse_cli_args()

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
    context = DbContext()

    driver = ScraperDriver()
    planning_page = pages.PlanningApplicationsPage(driver)
    all_wards = planning_page.get_all_wards()

    new_projects: List[PlanningProject] = []

    for ward in all_wards:
        for neighbourhood in ward.neighbourhoods:
            neighbourhood_page = pages.NeighbourhoodApplicationsPage(
                driver, neighbourhood
            )

            if args.bulk_load:
                new_projects.extend(
                    [
                        _get_project(project, neighbourhood.title, ward.title)
                        for project in neighbourhood_page.get_all_proposed_projects()
                    ]
                )

    if args.bulk_load:
        context.planning_project_repository.bulk_load(new_projects)


def _get_project(
    proj_elem: ProjectElement, neighbourhood: str, ward: str
) -> PlanningProject:
    project = PlanningProject()
    project.Title = proj_elem.title
    project.Summary = proj_elem.summary
    project.Neighbourhood = neighbourhood
    project.Ward = int(ward.split()[1])
    project.DateAdded = datetime.now()

    return project


def parse_cli_args() -> object:
    parser = ArgumentParser(description="Scrape and monitor websites for changes")
    parser.add_argument(
        "-b",
        "--bulk-load",
        action="store_true",
        help="Bulk load all projects",
    )

    return parser.parse_args()


main()
