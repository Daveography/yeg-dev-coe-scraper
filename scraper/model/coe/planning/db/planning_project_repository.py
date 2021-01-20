from datetime import datetime
from typing import List

from scraper.model.coe.planning.db.planning_project import PlanningProject
from sqlalchemy.orm.session import Session


class PlanningProjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, project: PlanningProject) -> None:
        self.session.add(project)
        self.session.commit()

    def bulk_load(self, projects: List[PlanningProject]) -> None:
        self.session.bulk_save_objects(projects)
        self.session.commit()

    def remove(self, project: PlanningProject) -> None:
        project.DateRemoved = datetime.now()
        self.session.commit()
