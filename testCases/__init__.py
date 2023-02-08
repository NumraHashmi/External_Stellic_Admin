#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Imports tests and run them all"""

# Standard library
import unittest

# First-party
from testCases.test_courses import TestCourses
from testCases.test_login import TestLogin
from testCases.test_program import TestProgram
from testCases.test_staff import TestStaff

if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main(verbosity=2)
