
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
