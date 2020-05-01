import unittest
import re #regular expression
import io

from Parse_File import case_num


class TodayTestCase(unittest.TestCase):

    def test_3_case_num(self):

        output = case_num("2020-04-12_145.txt")
        self.assertEqual(output, ('3'))

    def test_2_case_num(self):

        output = case_num("2020-04-15_150.txt")
        self.assertEqual(output, ('2'))

    def test_0_case_num(self):

        output = case_num("2020-04-29_173.txt")
        self.assertEqual(output, ('0'))

    def test_exception_case_num(self):

        output = case_num("2020-03-08_77.txt")
        self.assertEqual(output, ('0'))

    def test_exception_2_case_num(self):

        output = case_num("2020-03-05_71.txt")
        self.assertEqual(output, ('2'))

    def test_exception_death_case_num(self):

        output = case_num("2020-04-10_142.txt")
        self.assertEqual(output, None)


unittest.main()
