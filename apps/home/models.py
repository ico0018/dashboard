from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
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

class RawMalware(Base):
    __tablename__ = 'raw_malware'
    
    id = Column(Integer, primary_key=True)
    sample_id = Column(Integer, nullable=False)
    sha1 = Column(String(40), unique=True)
    filetype = Column(String(50), nullable=False)
    av_output_old = Column(String(255))
    packer = Column(String(255))
    av_output_family = Column(String(255))
    av_output_id = Column(Integer)
    received_date = Column(DateTime)
    partner_id = Column(Integer)
    md5 = Column(String(32))
    analysis_status = Column(String(1))
    ssdeep = Column(String(159))
    analyzed = Column(String(1))
    sent_to_partners = Column(String(1))
    static_results_id = Column(Integer)
