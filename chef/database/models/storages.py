from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

# TODO: Do Sqlalchemy have log Management

Base = declarative_base()


# TODO: Design For Database.

class FileLocation(Base):
    __tablename__ = 'File_Location'


class Status(Base):
    __tablename__ = "Status_Service"


class logs(Base):
    __tablename__ = "logs"


class user(Base):
    __tablename__ = "User"


