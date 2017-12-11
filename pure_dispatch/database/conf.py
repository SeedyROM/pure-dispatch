# This file is part of pure-dispatch.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>
from sqlalchemy import create_engine

from pure_dispatch import settings


def create_database_engine():
    return create_engine(f'sqlite:///{settings.DATABASE_CONFIGURATION["PATH"]}')
