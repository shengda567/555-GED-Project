import unittest
from The_Real_Project03 import *

class Test_case_us10_us31(unittest.TestCase):
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


        '''Shengda Sprint 2: US10, US31'''
        self.US10_report = marriage_after_14(family_dict, individual_dict)
        self.US31_report = list_living_single(family_dict, individual_dict)

    def test_US10(self):
        expect = {'@F1@': ['1988-1-1', '1990-1-1', '1991-1-1'],
                  '@F2@': True, '@F4@': ['2000-1-1', '1991-1-1', '1990-1-1'],
                  '@F5@': True, '@F6@': ['1993-1-1', '1992-1-1', '1992-1-1']}
        actual = self.US10_report
        self.assertEqual(actual, expect)

    def test_US31(self):
        expect = {'@I1@': False, '@I2@': False, '@I3@': False,
                  '@I4@': False, '@I5@': False, '@I6@': False,
                  '@I7@': False, '@I9@': False, '@I11@': [220, 'NA'],
                  '@I12@': False, '@I13@': False, '@I14@': False,
                  '@I15@': False, '@I16@': False, '@I17@': False,
                  '@I18@': False, '@I19@': False, '@I20@': False,
                  '@I21@': False, '@I22@': False, '@I23@': False,
                  '@I24@': False, '@I25@': False, '@I26@': False,
                  '@I27@': False, '@I28@': False}
        actual = self.US31_report
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()
