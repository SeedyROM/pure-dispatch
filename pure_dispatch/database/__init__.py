'''Database module.
'''
from pure_dispatch.database.conf import create_database_engine
from pure_dispatch.utils.generic.singleton import SingletonBaseClass


class DatabaseEngine(SingletonBaseClass):
    '''Singleton to wrap our database engine connection.
    '''
    def __init__(self):
        self.instance = create_database_engine()

    def __call__(self):
        return self.instance

class DatabaseSession(SingletonBaseClass):
    '''Singleton to wrap our database session.
    '''
    def __init__(self):
        pass

DATABASE_ENGINE = DatabaseEngine()
DATABASE_SESSION = DatabaseSession()
