from sqlalchemy import create_engine

from pure_dispatch import settings


def create_database_engine():
    return create_engine(f'sqlite:///{settings.DATABASE_CONFIGURATION["PATH"]}')
