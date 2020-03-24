import unittest
import The_Real_Project03

class Test_US17_US22(unittest.TestCase):
    def test_US_17_US22(self):
        output = The_Real_Project03.main()
        individual_dict = output[0]
        family_dict = output[1]

        expected_individual = [['@I1@', 'Mars /Hulu/', 'M', '1990-1-1', 'NA', '@F1@', '@F3@'],
                               ['@I2@', 'Jose /Hulu/', 'M', '1970-1-1', '1995-1-1', 'NA', '@F1@'],
                               ['@I3@', 'MarriedToChild /Hulu/', 'F', '1970-1-1', 'NA', 'NA', '@F3@'],
                               ['@I4@', 'SameID2 /Hulu/', 'F', '1992-1-1', 'NA', '@F1@', 'NA']]
        expected_family = [['@F1@', 'NA', '@I2@', '@I3@', {'@I1@', '@I4@', '@I5@'}, 'NA'],
                           ['@F3@', 'NA', '@I1@', '@I3@', 'NA', 'NA']]
        actual_individual = []
        actual_family = []

        for key, value in individual_dict.items():
            actual_individual.append([key, value.name, value.sex, value.birt.snake_year_month_day(), value.deat.snake_year_month_day(), value.famc, value.fams])
        for key, value in family_dict.items():
            actual_family.append([key, value.marr.snake_year_month_day(), value.husb, value.wife, value.chil, value.div.snake_year_month_day()])

        self.assertEqual(expected_family, actual_family)
        self.assertEqual(expected_individual, actual_individual)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
