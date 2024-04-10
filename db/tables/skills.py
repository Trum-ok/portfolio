# ruff: noqa
from sqlalchemy import Column, String, Boolean, Integer, JSON, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

# from dev.exceptions import *

Base = declarative_base()


class Skill_:
    def __init__(self, data: dict) -> None:
        self.data = data

        self.id: int = data.get('id')
        self.name: str = data.get('name')
        self.image: str = data.get('image')
        self.isPublic: bool = data.get('isPublic', True)


class Skill(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    isPublic = Column(Boolean, default=True)
    image = Column(String, default=None)


class SkillsTable:
    """Skills table"""
    def __init__(self, Session):
        self.Session = Session


    def get_all(self) -> list[Skill]:
        session = self.Session()
        try:
            skills = session.query(Skill).all()
            return skills
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()


    def insert(self, skill: Skill_) -> None:
        session = self.Session()
        try:
            new_skill = Skill(
                name=skill.name,
                isPublic=skill.isPublic,
                image=skill.image
            )
            session.add(new_skill)
            session.commit()
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()


    def edit(self, skill_id: int, **kwargs) -> None:
        session = self.Session()
        try:
            skill = session.query(Skill).filter_by(id=skill_id).first()
            if skill:
                for key, value in kwargs.items():
                    setattr(skill, key, value)
                session.commit()
            else:
                raise ValueError(f"Skill with id {skill_id} does not exist.")
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()
