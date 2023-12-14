
from sqlalchemy import create_engine, Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

Base = declarative_base()

hiker_trip_association = Table(
    'hiker_trip_association', Base.metadata,
    Column('hiker_id',Integer, ForeignKey('hiker.id')),
    Column('trip_id', Integer,ForeignKey('trip.id'))
    
)
