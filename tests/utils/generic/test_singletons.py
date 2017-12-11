# This file is part of pure-dispatch.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>
'''Test our generic singletons.
'''
from pure_dispatch.utils.generic.singleton import SingletonMetaClass
from tests.base import TestCase


class TestGenericSingletons(TestCase):
    '''Simple implmentation tests.
    '''
    def test_singleton_meta_class(self):
        '''Test if our singleton metaclass is working.
        '''
        class Tester:
            '''Test class'''
            __metaclass__ = SingletonMetaClass

        self.assertTrue(Tester.__metaclass__, SingletonMetaClass)