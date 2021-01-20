from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql.sqltypes import SmallInteger
from scraper.model.coe.planning.db._base import DB_BASE


class PlanningProject(DB_BASE):
    __tablename__ = "PlanningProject"

    Id = Column(Integer, primary_key=True)
    Title = Column(String(length=200), nullable=False, index=True)
    Summary = Column(String, nullable=True, index=False)
    Ward = Column(SmallInteger, nullable=False, index=False)
    Neighbourhood = Column(String(length=50), nullable=False, index=False)
    DateAdded = Column(DateTime, nullable=False, index=False)
    DateRemoved = Column(DateTime, nullable=True, index=False)
