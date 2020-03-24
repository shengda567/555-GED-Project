from The_Real_Project03 import *
import unittest


class GedTest(unittest.TestCase):

    def setUp(self):
        file_path = 'JM.ged'

        individuals = {}
        families = {}

        with open(file_path, 'r') as file:
            unfiltered_file = file.readlines()

            filter_file(unfiltered_file, individuals, families)

        individual_dict = {}
        family_dict = {}

        raw_individuals_to_structured_dict(individuals, individual_dict)
        raw_families_to_structured_dict(families, family_dict)

        self.US17 = no_marriage_to_children(family_dict)

    def test_US17(self):
        exp = {'@F2@': ['@F2@', '@F2@', '@F2@']}
        rlt = self.US17
        self.assertEqual(exp, rlt)


if __name__ == '__main__':
    unittest.main()

