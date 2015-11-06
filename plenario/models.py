import os
from sqlalchemy import Column, Integer, String, Boolean, Table, Date, DateTime, \
    Float, Numeric, Text, TypeDecorator, BigInteger
from sqlalchemy.dialects.postgresql import TIMESTAMP, DOUBLE_PRECISION, TIME,\
    DATE, ARRAY
from geoalchemy2 import Geometry
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, deferred, synonym
from sqlalchemy.ext.hybrid import hybrid_property
from uuid import uuid4
from flask_bcrypt import Bcrypt
from plenario.database import session

from plenario.database import Base, app_engine as engine
#from plenario.auth import bcrypt
bcrypt = Bcrypt()

class MetaTable(Base):
    __tablename__ = 'meta_master'
    dataset_name = Column(String(100), nullable=False)
    human_name = Column(String(255), nullable=False)
    description = Column(Text)
    source_url = Column(String(255))
    source_url_hash = Column(String(32), primary_key=True)
    attribution = Column(String(255))
    obs_from = Column(Date)
    obs_to = Column(Date)
    bbox = Column(Geometry('POLYGON', srid=4326))
    update_freq = Column(String(100), nullable=False)
    last_update = Column(DateTime)
    date_added = Column(DateTime)
    # Store the names of fields in source data
    business_key = Column(String, nullable=False)
    observed_date = Column(String, nullable=False)
    latitude = Column(String)
    longitude = Column(String)
    location = Column(String)
    approved_status = Column(String) # if False, then do not display without first getting administrator approval
    contributor_name = Column(String)
    contributor_organization = Column(String)
    contributor_email = Column(String)
    contributed_data_types = Column(Text) # Temporarily store user-submitted data types for later approval
    is_socrata_source = Column(Boolean, default=False)
    result_ids = Column(ARRAY(String))

    def __repr__(self):
        return '<MetaTable %r (%r)>' % (self.human_name, self.dataset_name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class MasterTable(Base):
    __tablename__ = 'dat_master'
    master_row_id = Column(BigInteger, primary_key=True)
    # Looks like start_date and end_date aren't used.
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)
    # current_flag is never updated. We can probably get rid of this
    current_flag = Column(Boolean, default=True)
    location = Column(String(200))
    latitude = Column(DOUBLE_PRECISION(precision=53))
    longitude = Column(DOUBLE_PRECISION(precision=53))
    obs_date = Column(TIMESTAMP, index=True)
    weather_observation_id = Column(BigInteger, index=True)
    census_block = Column(String(15), index=True)
    # Looks like geotag3 is unused
    geotag3 = Column(String(50))
    dataset_name = Column(String(100), index=True)
    dataset_row_id = Column(Integer)
    location_geom = Column(Geometry('POINT', srid=4326))

    def __repr__(self):
        return '<Master %r (%r)>' % (self.dataset_row_id, self.dataset_name)


class PolygonMetadata(Base):
    __tablename__ = 'meta_polygon'
    dataset_name = Column(String(100), primary_key=True)
    human_name = Column(String(100), primary_key=True)
    source_url = Column(String)
    source_srid = Column(Integer, nullable=False)
    source_hash = Column(String(40), nullable=False)  # SHA-1 digest, stored as 40 hex characters
    last_update = Column(DateTime, nullable=False)
    date_added = Column(DateTime, nullable=False)
    # Wait, there's a 2DBox data type!
    bbox = Column(Geometry('POLYGON', srid=4326), nullable=False)

def get_uuid():
    return unicode(uuid4())

class User(Base):
    __tablename__ = 'plenario_user'
    id = Column(String(36), default=get_uuid, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
    _password = Column('password', String(60), nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, value):
        self._password = bcrypt.generate_password_hash(value)

    password = property(_get_password, _set_password)
    password = synonym('_password', descriptor=password)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    @classmethod
    def get_by_username(cls, name):
        return session.query(cls).filter(cls.name == name).first()

    @classmethod
    def check_password(cls, name, value):
        user = cls.get_by_username(name)
        if not user:
            return False
        return bcrypt.check_password_hash(user.password, value)

    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
''' Not used
def crime_table(name, metadata):
    table = Table(name, metadata,
            Column('id', Integer),
            Column('case_number', String(length=10)),
            Column('orig_date', TIMESTAMP),
            Column('block', String(length=50)),
            Column('iucr', String(length=10)),
            Column('primary_type', String(length=100)),
            Column('description', String(length=100)),
            Column('location_description', String(length=50)),
            Column('arrest', Boolean),
            Column('domestic', Boolean),
            Column('beat', String(length=10)),
            Column('district', String(length=5)),
            Column('ward', Integer),
            Column('community_area', String(length=10)),
            Column('fbi_code', String(length=10)),
            Column('x_coordinate', Integer, nullable=True),
            Column('y_coordinate', Integer, nullable=True),
            Column('year', Integer),
            Column('updated_on', TIMESTAMP, default=None),
            Column('latitude', DOUBLE_PRECISION(precision=53)),
            Column('longitude', DOUBLE_PRECISION(precision=53)),
            Column('location', Point),
    extend_existing=True)
    return table
'''