# ruff: noqa
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

# from dev.exceptions import *

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    t = Column(String)
    name = Column(String)
    year = Column(Integer)
    description = Column(String)
    isPublic = Column(Boolean, default=True)
    image = Column(String, default=None)


class EventsTable:
    name = 'events'
    schema = 'public'
    
    """Events table"""
    def __init__(self, Session):
        self.Session = Session

    def get_all(self) -> list[Event]:
        session = self.Session()
        try:
            events = session.query(Event).all()
            return events
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()

    def insert(self, event_data: dict) -> None:
        session = self.Session()
        try:
            new_event = Event(
                t=event_data.get('t'),
                name=event_data.get('name'),
                year=event_data.get('year'),
                description=event_data.get('description'),
                isPublic=event_data.get('isPublic', True),
                image=event_data.get('image')
            )
            session.add(new_event)
            session.commit()
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()

    def edit(self, event_id: int, **kwargs) -> None:
        session = self.Session()
        try:
            event = session.query(Event).filter_by(id=event_id).first()
            if event:
                for key, value in kwargs.items():
                    setattr(event, key, value)
                session.commit()
            else:
                raise ValueError(f"Event with id {event_id} does not exist.")
        except SQLAlchemyError as e:
            print(e)
            session.rollback()
            raise e
        finally:
            session.close()
