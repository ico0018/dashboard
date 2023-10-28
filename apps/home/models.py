from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Partner(Base):
    __tablename__ = 'partner'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    our_login = Column(String(255), nullable=False)
    our_password = Column(String(255), nullable=False)
    contact_info_id = Column(Integer, nullable=False, unique=True)
    login_down_samples = Column(String(255), nullable=False)
    pass_down_samples = Column(String(255), nullable=False)
    url_down_samples = Column(String(500), nullable=False)
    days_not_down = Column(Integer)
    priority = Column(Integer, nullable=False)
    quota = Column(Integer, nullable=False)
    password_decompress = Column(String(255))
    url_crawling_deep = Column(Integer, nullable=False)
    admin_web = Column(String(255), nullable=False)
    main_location = Column(String(255))
    main_location_code = Column(String(2), nullable=False)
    uid = Column(Integer)
    gid = Column(Integer)
    homedir = Column(String(255))
    shell = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
