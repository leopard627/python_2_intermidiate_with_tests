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
        """
        setUp
        """
        assert 1 is 1

    def tearDown(self):
        """
        tearDown
        """
        assert 1 is 1

    def test_name(self):
        """
        test_name
        """
        assert 1 is 1, "Should be cool"
