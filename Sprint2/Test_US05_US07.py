import unittest
from The_Real_Project03 import *

class Test_case_us05_us07(unittest.TestCase):
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


        '''Shengda Sprint 1: US05, US07'''
        self.US05_report = marriage_before_death(family_dict, individual_dict)
        self.US07_report = less_than_150_years_old(individual_dict)

    def test_US05(self):
        expect = {'@F1@': True, '@F2@': True, '@F3@': True,
                  '@F4@': True, '@F5@': False, '@F6@': True,
                  '@F7@': True, '@F8@': True, '@F9@': True}
        actual = self.US05_report
        self.assertEqual(actual, expect)

    def test_US07(self):
        expect = {'@I1@': True, '@I2@': True, '@I3@': True,
                  '@I4@': True, '@I5@': True, '@I6@': True,
                  '@I7@': True, '@I8@': True, '@I9@': True,
                  '@I10@': True, '@I11@': False, '@I12@': True,
                  '@I13@': True, '@I14@': True, '@I15@': True,
                  '@I16@': True, '@I17@': True, '@I18@': True,
                  '@I19@': True, '@I20@': True, '@I21@': True,
                  '@I22@': True, '@I23@': True, '@I24@': True,
                  '@I25@': True, '@I26@': True, '@I27@': True,
                  '@I28@': True}

        actual = self.US07_report
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()
