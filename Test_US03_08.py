import unittest
import The_Real_Project03

class Test_Sprint_2(unittest.TestCase):
    '''Test Cases for Sprint 2, US03 + US08'''
    main = The_Real_Project03.main()
    individual_dict = main[0]
    family_dict = main[1]

    '''US03 Test Case'''
    def test_birth_before_death(self):
        expected = [['@I1@', 'Normal /Sprint2/', 'M', '1994-1-1', 'NA', '@F2@', '@F1@'],
                    ['@I2@', 'NormalDad /Sprint2/', 'M', '1969-1-1', 'NA', 'NA', '@F2@'],
                    ['@I3@', 'NormalMom /Sprint2/', 'F', '1970-1-1', 'NA', 'NA', '@F2@'],
                    ['@I4@', 'BirthBefMarrPar /Sprint2/', 'F', 'NA', 'NA', '@F3@', '@F1@'],
                    ['@I5@', 'ErrDad /Sprint2/', 'M', '1969-1-1', 'NA', 'NA', '@F3@'],
                    ['@I6@', 'ErrMom /Sprint2/', 'F', '1970-1-1', 'NA', 'NA', '@F3@'],
                    ['@I7@', 'BirthBefDeath /Sprint2/', 'M', 'NA', '1995-1-1', '@F2@', 'NA']]
        actual = []
        for key, value in self.individual_dict.items():
            actual.append([key, value.name, value.sex, value.birt.snake_year_month_day(), value.deat.snake_year_month_day(), value.famc, value.fams])

        self.assertEqual(expected, actual)
    '''US08 Test Case'''
    def test_birth_before_marriage_of_parents(self):
        expected_individual = [['@I1@', 'Normal /Sprint2/', 'M', '1994-1-1', 'NA', '@F2@', '@F1@'],
                    ['@I2@', 'NormalDad /Sprint2/', 'M', '1969-1-1', 'NA', 'NA', '@F2@'],
                    ['@I3@', 'NormalMom /Sprint2/', 'F', '1970-1-1', 'NA', 'NA', '@F2@'],
                    ['@I4@', 'BirthBefMarrPar /Sprint2/', 'F', 'NA', 'NA', '@F3@', '@F1@'],
                    ['@I5@', 'ErrDad /Sprint2/', 'M', '1969-1-1', 'NA', 'NA', '@F3@'],
                    ['@I6@', 'ErrMom /Sprint2/', 'F', '1970-1-1', 'NA', 'NA', '@F3@'],
                    ['@I7@', 'BirthBefDeath /Sprint2/', 'M', 'NA', '1995-1-1', '@F2@', 'NA']]

        expected_family = [['@F1@', 'NA', '@I1@', '@I4@', 'NA', 'NA'],
                           ['@F2@', 'NA', '@I2@', '@I3@', {'@I7@', '@I1@'}, 'NA'],
                           ['@F3@', '1999-1-1', '@I5@', '@I6@', {'@I4@'}, 'NA']]

        actual_individual = []
        actual_family = []

        for key, value in self.individual_dict.items():
            actual_individual.append([key, value.name, value.sex, value.birt.snake_year_month_day(), value.deat.snake_year_month_day(), value.famc, value.fams])
        for key, value in self.family_dict.items():
            actual_family.append([key, value.marr.snake_year_month_day(), value.husb, value.wife, value.chil, value.div.snake_year_month_day()])

        self.assertEqual(expected_individual, actual_individual)
        self.assertEqual(expected_family, actual_family)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)