'''Module to store generic utility classes.
'''

class SingletonMetaClass(type):
    '''Generic singleton metaclass.
    '''
    def __init__(cls, name, bases, _dict):  # pragma: no cover
        '''Initializer method, no practical way to test this as of yet.
        So using a coverage pragma to hide it.
        '''
        super(SingletonMetaClass, cls).__init__(name, bases, dict)
        original_new = cls.__new__
        def new_instance(cls, *args, **kwargs):
            '''Method to only call the singleton constructor once.
            '''
            if cls.instance is None:
                cls.instance = original_new(cls, *args, **kwargs)
            return cls.instance
        cls.instance = None
        cls.__new__ = staticmethod(new_instance)


class SingletonBaseClass:
    '''Abstract class to create singletons.
    '''
    __metaclass__ = SingletonMetaClass
