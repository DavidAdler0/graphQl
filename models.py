from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base= declarative_base()


# user_subject_relation = Table(
#     'user_subject_relation',
#     Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('subject_id', Integer, ForeignKey('subjects.id'))
# )

class MissionModel(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(String)
    airborne_aircraft = Column(Float)
    attacking_aircraft = Column(Float)
    bombing_aircraft = Column(Float)
    aircraft_returned = Column(Float)
    aircraft_failed = Column(Float)
    aircraft_damaged = Column(Float)
    aircraft_lost = Column(Float)
    targets = relationship('TargetModel', back_populates='missions')

class CountryModel(Base):
    __tablename__ = 'countries'
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)

class CityModel(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.country_id'))
    latitude = Column(Float)
    longitude = Column(Float)

class TargetTypesModel(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)
    targets = relationship('TargetModel', back_populates='target_types')

class TargetModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)
    target_industry = Column(String)
    missions = relationship('MissionModel', back_populates='targets')

    target_types = relationship('TargetTypesModel', back_populates='targets')


