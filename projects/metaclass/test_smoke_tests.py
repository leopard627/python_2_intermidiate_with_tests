#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_smoke_tests
이것이... module doc string...
"""

import unittest


class TestClass(unittest.TestCase):
    """Test case docstring."""
    def setUp(self):
        pass

    def tearDown(self):
        assert 1 is 1

    def test_define_type_classes(self):

        class MyClass(object):
            pass

        x = MyClass()

        assert MyClass == type(x)

    def test_class_method_test(self):

        class MyClass(object):
            def __init__(self, ):
                self.x = 1000

            @property
            def my_method(self):
                print("is it working?")
                return self.x

            @my_method.setter
            def my_method(self, v):
                self.x = v
                return self.x

        y = MyClass()

        print(y.my_method)

        y.my_method = 100

        print(y.my_method)
