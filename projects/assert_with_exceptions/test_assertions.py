#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
이것이... module doc string...
"""

import unittest

class TestForAsserTions(unittest.TestCase):
    """Test case docstring."""
    def test_name(self):
        try:
            assert 1 is not 1, "The Balance is negative numeric"

        except AssertionError as e:
            print(e)

    def test_is_negative_number(self):
        try:
            the_number = -100
            assert the_number >= 0, "The_number suppose to be greter than 0!!"

        except AssertionError as e:
            print(e)
            # raise 를 하게되면 무조건 Fail을 시킵니다...1

        except Exception as e:
            print ("Exception Part")
            raise

        finally:
            # 무조건 finally 로 가기떄문에, 조심
            print ("Finally Part")
            # raise
