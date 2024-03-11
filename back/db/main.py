import db.tables as tables
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database:
    """Database"""

    def __init__(self, Session, engine):
        self.Session = Session
        self.engine = engine

        self.projects = tables.ProjectsTable(self.Session)
        """Projects"""
        self.events = tables.EventsTable(self.Session)
        """Events"""
        self.skills = tables.SkillsTable(self.Session)
        """Skills"""

    def create(self) -> None:
        """
        Create database tables.
        """
        tables.Base.metadata.create_all(bind=self.engine)
