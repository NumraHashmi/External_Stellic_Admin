#!./venv/bin/python
# -*- coding: utf-8 -*-

"""Runs all the test: $ python main.py"""

# Standard library
import unittest

# Third-party
import HTMLTestRunner

# First-party
from testCases.test_courses import TestCourses
from testCases.test_login import TestLogin
from testCases.test_program import TestProgram
from testCases.test_staff import TestStaff
from testCases.test_student import TestStudents


def test_suite():
    """
    Function to create Test Suite from Unit-Tests
    :return:
    """
    test1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    test2 = unittest.TestLoader().loadTestsFromTestCase(TestProgram)
    test3 = unittest.TestLoader().loadTestsFromTestCase(TestCourses)
    test4 = unittest.TestLoader().loadTestsFromTestCase(TestStaff)
    test5 = unittest.TestLoader().loadTestsFromTestCase(TestStudents)
    suite = unittest.TestSuite([test1, test2, test3, test4, test5])
    runner = HTMLTestRunner.HTMLTestRunner(
        log=True,
        verbosity=2,
        output='outfile.html',
        title='Test report',
        report_name='report',
        open_in_browser=True,
        description='HTMLTestReport',
    )
    runner.run(suite)


if __name__ == '__main__':
    test_suite()
