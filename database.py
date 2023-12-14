
from sqlalchemy import create_engine, Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

Base = declarative_base()

hiker_trip_association = Table(
    'hiker_trip_association', Base.metadata,
    Column('hiker_id',Integer, ForeignKey('hiker.id')),
    Column('trip_id', Integer,ForeignKey('trip.id'))

)
class hiker(Base):
    __tablename__ = 'hiker'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contact_info = Column(String)
    emergency_contact = Column(String)
    preferences = Column(String)
    trips = relationship("Trip", secondary=hiker_trip_association)


class Equipment(Base):
    __tablename__ = 'equipment'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    condition = Column(String)

class Trip(Base):
    __tablename__ = 'trip'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    trips = relationship("Trip", secondary=hiker_trip_association)

def __init__(self, name, destination):
        self.name = name
        self.destination = destination


engine = create_engine("sqlite:///hikers_management.db", echo = True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

def initialize_database():
    Base.metadata.create_all(bind=engine)
    