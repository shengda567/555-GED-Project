#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import The_Real_Project03

class Test_Sprint_2(unittest.TestCase):
    '''Test Cases for Sprint 2, US13 + US14'''
    '''US13 US14 Test Case'''
    def test(self):
        main = The_Real_Project03.main()
        individual_dict = main[0]
        family_dict = main[1]
        actual = main[2]
        expected = ['ERROR: US13: @I1@ has a sibling whose birth date is too close', 
                    'ERROR: US13: @I7@ has a sibling whose birth date is too close', 
                    'ERROR: US14: @I10@ has too many siblings born at the same time', 
                    'ERROR: US14: @I11@ has too many siblings born at the same time', 
                    'ERROR: US14: @I12@ has too many siblings born at the same time', 
                    'ERROR: US14: @I13@ has too many siblings born at the same time', 
                    'ERROR: US14: @I14@ has too many siblings born at the same time', 
                    'ERROR: US14: @I15@ has too many siblings born at the same time']
        print(actual)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity = 2)


# In[ ]:




