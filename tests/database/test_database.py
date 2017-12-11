# This file is part of pure-dispatch.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>
'''Test our database module.
'''
from tests.base import TestCase

from pure_dispatch.database import DatabaseEngine, DatabaseSession
from preggy import expect


class DatabaseTestCase(TestCase):
    '''Create a generic test case for our suite.
    '''
    @classmethod
    def setUpClass(cls):
        cls.engine = DatabaseEngine()
        cls.session = DatabaseSession()


class TestDatabaseBase(DatabaseTestCase):
    '''Test the basic functionality of our module.
    '''
    def test_globals_initialize(self):
        '''Test our singleton's initialize at all.
        '''
        expect(DatabaseEngine).error_not_to_happen()
        expect(DatabaseSession).error_not_to_happen()

    def test_database_engine(self):
        '''Test if our singleton initializes the engine property.
        '''
        expect(self.engine).error_not_to_happen()

    def test_database_session(self):
        '''Test if our singleton initializes the session property.
        '''
        expect(self.session).error_not_to_happen()
