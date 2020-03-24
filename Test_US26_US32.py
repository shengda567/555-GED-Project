import unittest
from The_Real_Project03 import *

class Test_case_us26_us32(unittest.TestCase):
    def setUp(self):
        file_path = 'Sprint-1-test.ged'
        '''Dictionaries of Individuals and Families'''
        individuals = {}
        families = {}
        # 1. Read the file
        with open(file_path, 'r') as file:
            unfiltered_file = file.readlines()
            # 2. Filter the file
            filter_file(unfiltered_file, individuals, families)

        individual_dict = {}
        family_dict = {}
        '''the next 2 lines fill in the previous 2 lines individual_dict and family_dict'''
        raw_individuals_to_structured_dict(individuals, individual_dict)
        raw_families_to_structured_dict(families, family_dict)


        '''Xiangyu Sprint 2: US26, US32'''
        self.US26_report = corresponding_entries(family_dict, individual_dict)
        self.US32_report = list_multiple_births(individual_dict)

    def test_US26(self):
        expect = {'@F2@': ['@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@', '@F2@'],
                  '@F3@': ['@F3@'], '@F7@': ['@F8@']}
        actual = self.US26_report
        self.assertEqual(actual, expect)

    def test_US32(self):
        expect = {'1990-1-1': ['@I1@', '@I6@', '@I7@', '@I8@', '@I28@'],
                  '1961-1-1': ['@I2@'], '1960-1-1': ['@I3@'],
                  '1991-1-1': ['@I4@', '@I5@'], '1992-1-1': ['@I9@', '@I10@'],
                  '1800-1-1': ['@I11@'], '1993-1-1': ['@I12@', '@I13@', '@I14@'],
                  '1880-1-1': ['@I15@'], '1930-1-1': ['@I16@'],
                  '1999-1-1': ['@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@', '@I25@', '@I26@', '@I27@']}
        actual = self.US32_report
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()
