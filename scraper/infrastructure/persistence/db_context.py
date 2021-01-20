from scraper.model.coe.planning.db._base import DB_BASE
from scraper.model.coe.planning.db.planning_project_repository import (
    PlanningProjectRepository,
)
from scraper.services.config.config_service import ConfigService
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class DbContext:
    def __init__(self, session: Session = None) -> None:
        self.config = ConfigService()

        if session is None:
            self.engine = create_engine(self.config.DB_URI)

            if self.config.create_tables:
                self.create_table_if_not_exist()

            self.session = sessionmaker(bind=self.engine, autoflush=True)()
        else:
            self.session = session

        self.planning_project_repository = PlanningProjectRepository(self.session)

    def create_table_if_not_exist(self) -> None:
        DB_BASE.metadata.create_all(self.engine)
