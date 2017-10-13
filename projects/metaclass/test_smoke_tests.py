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
