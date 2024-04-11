# ruff: noqa
from sqlalchemy import Column, String, Boolean, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

# from dev.exceptions import *

Base = declarative_base()


class Project_:
    def __init__(self, data: dict) -> None:
        self.data = data

        self.id: int = data.get('id')
        self.name: str = data.get('name')
        self.description: str = data.get('description')
        self.image: str = data.get('image')
        self.isPublic: bool = data.get('isPublic', True)
        self.tags: list = data.get('tags', [])
        self.github: str = data.get('github')
        self.web: str = data.get('web')


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tags = Column(JSON, default=[])
    description = Column(String)
    isPublic = Column(Boolean, default=True)
    image = Column(String, default=None)
    github = Column(String, default=None)
    web = Column(String, default=None)


class ProjectsTable:
    
    """Projects table"""
    def __init__(self, Session):
        self.Session = Session


    def get_all(self) -> list[Project]:
        session = self.Session()
        try:
            projects = session.query(Project).all()
            return projects
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()


    def insert(self, project: Project_) -> None:
        session = self.Session()
        try:
            new_project = Project(
                name=project.name,
                description=project.description,
                image=project.image,
                isPublic=project.isPublic,
                tags=project.tags
            )
            session.add(new_project)
            session.commit()
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()
    

    def edit(self, project_id: int, **kwargs) -> None:
        session = self.Session()
        try:
            project = session.query(Project).filter_by(id=project_id).first()
            if project:
                for key, value in kwargs.items():
                    setattr(project, key, value)
                session.commit()
            else:
                raise ValueError(f"Project with id {project_id} does not exist.")
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()
