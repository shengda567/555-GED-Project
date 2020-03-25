"""The Brand New Project 03 With Better Data Structure And Better Visual"""
"""Please Make Code As Minimalist As Possible"""
from prettytable import PrettyTable
from datetime import date

"""Useful Functions And Classes"""
'''Individual Class'''
class Individual:
    def __init__(self, name, sex, birt, deat, famc, fams):
        self.name = name
        self.sex = sex
        self.birt = birt
        self.deat = deat
        self.famc = famc
        self.fams = fams

'''Family Class'''
class Family:
    def __init__(self, marr, husb, wife, chil, div):
        self.marr = marr
        self.husb = husb
        self.wife = wife
        self.chil = chil
        self.div = div

'''Date Class'''
class DateObject:
    def __init__(self, string_date):
        self.string_date = string_date
        self.year = 'NA'
        self.month = 'NA'
        self.day = 'NA'
        self.parse_string_date(string_date)

    def parse_string_date(self, string_date):
        '''1 Feb 1990 comes in'''
        if string_date == 'NA':
            self.year, self.month, self.day = 'NA', 'NA', 'NA'
        else:
            string_date_list = string_date.split(' ')
            month_dict = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}
            self.year = string_date_list[2]
            self.month = month_dict[string_date_list[1]]
            self.day = string_date_list[0]

    def snake_year_month_day(self):
        '''1990-2-1 comes out'''
        if self.year == 'NA' or self.month == 'NA' or self.day == 'NA':
            return 'NA'
        else:
            return f'{self.year}-{self.month}-{self.day}'

    def setNA(self):
        self.year, self.month, self.day = 'NA', 'NA', 'NA'

'''Age Calculator'''
def age_calculator(later_date, earlier_date):
    '''DateObjects, first parameter is for a later date, the second is for earlier'''
    def age_difference(later_date, earlier_date):
        y_l, m_l, d_l = later_date.year, later_date.month, later_date.day
        y_e, m_e, d_e = earlier_date.year, earlier_date.month, earlier_date.day
        return int(y_l) - int(y_e) - ((int(m_l), int(d_l)) < (int(m_e), int(d_e)))
    if isinstance(later_date, date):
        if earlier_date.snake_year_month_day() == 'NA':
            return 'NA'
        else:
            return age_difference(later_date, earlier_date)
    else:
        if later_date.snake_year_month_day() == 'NA' or earlier_date.snake_year_month_day() == 'NA':
            return 'NA'
        else:
            return age_difference(later_date, earlier_date)

'''Individual & Family Dictionary Constructor'''
def raw_individuals_to_structured_dict(raw_individuals, individual_dict):
    for key, value in raw_individuals.items():
        name, sex, birt, deat, famc, fams = 'NA', 'NA', DateObject('NA'), DateObject('NA'), 'NA', 'NA'
        for entry in range(len(value)):
            if value[entry][0] == '1' and value[entry][1] == 'NAME':
                name = value[entry][2]
            elif value[entry][0] == '1' and value[entry][1] == 'SEX':
                sex = value[entry][2]
            elif value[entry][0] == '1' and value[entry][1] == 'BIRT':
                if value[entry + 1][0] == '2' and value[entry + 1][1] == 'DATE':
                    birt = DateObject(value[entry + 1][2])
            elif value[entry][0] == '1' and value[entry][1] == 'DEAT':
                if value[entry + 1][0] == '2' and value[entry + 1][1] == 'DATE':
                    deat = DateObject(value[entry + 1][2])
            elif value[entry][0] == '1' and value[entry][1] == 'FAMC':
                famc = value[entry][2]
            elif value[entry][0] == '1' and value[entry][1] == 'FAMS':
                fams = value[entry][2]
        individual_dict[key] = Individual(name, sex, birt, deat, famc, fams)

def raw_families_to_structured_dict(raw_families, family_dict):
    for key, value in raw_families.items():
        marr, husb, wife, chil, div = DateObject('NA'), 'NA', 'NA', set(), DateObject('NA')
        for entry in range(len(value)):
            if value[entry][0] == '1' and value[entry][1] == 'MARR':
                if value[entry + 1][0] == '2' and value[entry + 1][1] == 'DATE':
                    marr = DateObject(value[entry + 1][2])
            elif value[entry][0] == '1' and value[entry][1] == 'HUSB':
                husb = value[entry][2]
            elif value[entry][0] == '1' and value[entry][1] == 'WIFE':
                wife = value[entry][2]
            elif value[entry][0] == '1' and value[entry][1] == 'CHIL':
                chil.add(value[entry][2])
            elif value[entry][0] == '1' and value[entry][1] == 'DIV':
                if value[entry + 1][0] == '2' and value[entry + 1][1] == 'DATE':
                    div = DateObject(value[entry + 1][2])
        if len(chil) == 0:
            chil = 'NA'
        family_dict[key] = Family(marr, husb, wife, chil, div)

'''Pretty Tables'''
def draw_individual_prettytable(individual_dict):
    '''this pretty table uses age_calculator'''
    pt = PrettyTable()
    pt.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for id, individual in individual_dict.items():
        alive = True
        death_date = 'NA'
        if individual.birt.snake_year_month_day() == 'NA':
            alive = 'NA'
        if individual.deat.snake_year_month_day() != 'NA':
            alive = False
            death_date = individual.deat.snake_year_month_day()
        pt.add_row([id, individual.name, individual.sex, individual.birt.snake_year_month_day(), age_calculator(date.today(), individual.birt), alive, death_date, individual.famc, individual.fams])
    print(pt)

def draw_family_prettytable(family_dict, individual_dict):
    pt = PrettyTable()
    pt.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for id, family in family_dict.items():
        '''marr, husb, wife, chil, div'''
        pt.add_row([id, family.marr.snake_year_month_day(), family.div.snake_year_month_day(), family.husb, individual_dict[family.husb].name, family.wife, individual_dict[family.wife].name, family.chil])
    print(pt)

'''File Filter'''
def filter_file(file_to_filter, individuals, families):
    # valid_tags_for_0 = ['HEAD', 'TRLR', 'NOTE']
    valid_tags_for_1 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
    valid_tags_for_2 = ['DATE']

    individual_or_family_flag = ''
    individual_id = ''
    family_id = ''
    for line in file_to_filter:
        if line == '':
            continue
        else:
            line = line.strip('\n')
            line_split = line.split(' ')
            if line_split[0] == '0':
                if 'INDI' in line_split and line_split[1] != 'INDI':
                    individual_or_family_flag = 'individual'
                    individual_id = line_split[1]
                    individuals[individual_id] = []
                elif 'FAM' in line_split and line_split[1] != 'FAM':
                    individual_or_family_flag = 'family'
                    family_id = line_split[1]
                    families[family_id] = []
            elif line_split[0] == '1':
                if line_split[1] in valid_tags_for_1:
                    if individual_or_family_flag == 'individual':
                        individuals[individual_id].append(line.split(' ', 2))
                    elif individual_or_family_flag == 'family':
                        families[family_id].append(line.split(' ', 2))
            elif line_split[0] == '2':
                if line_split[1] in valid_tags_for_2:
                    if individual_or_family_flag == 'individual':
                        individuals[individual_id].append(line.split(' ', 2))
                    elif individual_or_family_flag == 'family':
                        families[family_id].append(line.split(' ', 2))

'''Error Collector'''
class ErrorCollector:
    error_list = []

"""Hanqing's Code Goes Here"""
'''Sprint 1'''
'''User Story 01: Dates before current date'''
def dates_before_current_date(individual_dict, family_dict):
    '''This function uses age_calculator, any dates in the future becomes NA'''
    # There are 4 fields using date: birt, deat, marr, div
    for key, value in individual_dict.items():
        # birt
        if value.birt.snake_year_month_day() != 'NA':
            if isinstance(age_calculator(date.today(), value.birt), int) and age_calculator(date.today(), value.birt) <= 0:
                ErrorCollector.error_list.append(f"ERROR: US01: Individual {key} has a birthday {value.birt.snake_year_month_day()} occurs in the future. Birthday was set to NA.")
                # value.birt.setNA()
        #deat
        if value.deat.snake_year_month_day() != 'NA':
            if isinstance(age_calculator(date.today(), value.deat), int) and age_calculator(date.today(), value.deat) <= 0:
                ErrorCollector.error_list.append(f"ERROR: US01: Individual {key} has a dearh date {value.birt.snake_year_month_day()} occurs in the future. Death date was set to NA.")
                # value.deat.setNA()
    for key, value in family_dict.items():
        # marr
        if value.marr.snake_year_month_day() != 'NA':
            if age_calculator(date.today(), value.marr) <= 0:
                ErrorCollector.error_list.append(f"ERROR: US01: Individual {key} has a wedding date {value.marr.snake_year_month_day()} occurs in the future. Wedding date was set to NA.")
                # value.marr.setNA()
        # div
        if value.div.snake_year_month_day() != 'NA':
            if age_calculator(date.today(), value.div) <= 0:
                ErrorCollector.error_list.append(f"ERROR: US01: Individual {key} has a divorce date {value.div.snake_year_month_day()} occurs in the future. Divorce date was set to NA.")
                # value.div.setNA()

'''User Story 02: Birth before marriage'''
def birth_before_marriage(individual_dict, family_dict):
    '''Any wedding date before birthday becomes NA'''
    for key, value in individual_dict.items():
        if value.fams != 'NA':
            if value.birt.snake_year_month_day() != 'NA' and family_dict[value.fams].marr.snake_year_month_day() != 'NA':
                if age_calculator(family_dict[value.fams].marr, value.birt) < 0:
                    ErrorCollector.error_list.append(f"ERROR: US02: Individual {key} has a wedding date {family_dict[value.fams].marr.snake_year_month_day()} occurs before birthday {value.birt.snake_year_month_day()}. Wedding date was set to NA.")
                    # family_dict[value.fams].marr.setNA()

'''Sprint 2'''
'''User Story 03: Birth Before Death'''
def birth_before_death(individual_dict):
    for id, value in individual_dict.items():
        if value.birt.snake_year_month_day() != 'NA' and value.deat.snake_year_month_day() != 'NA':
            if age_calculator(value.deat, value.birt) <= 0:
                ErrorCollector.error_list.append(f"ERROR: US03: Individual {id} has a birthday {value.birt.snake_year_month_day()} that occurred after death date {value.deat.snake_year_month_day()}. Birthday was set to NA.")
                # value.birt.setNA()

'''User Story 08: Birth Before Marriage Of Parents'''
def birth_before_marriage_of_parents(individual_dict, family_dict):
    for id, value in individual_dict.items():
        if value.famc != 'NA':
            if family_dict[value.famc].marr != 'NA':
                if age_calculator(value.birt, family_dict[value.famc].marr) != 'NA' and age_calculator(value.birt, family_dict[value.famc].marr) < 0:
                    ErrorCollector.error_list.append(f"ERROR: US08: Individual {id} has a birth date {value.birt.snake_year_month_day()} that's earlier than parents' wedding date {family_dict[value.famc].marr.snake_year_month_day()}. Birthday was set to NA.")
                    # value.birt.setNA()


"""Jigar's Code Goes Here"""
'''Sprint 1'''
'''User Story 04: Marriage before divorce'''
def marriage_before_divorce(family_dict):
    for key, value in family_dict.items():
        if value.marr.snake_year_month_day() != 'NA' and value.div.snake_year_month_day() != 'NA':
            if age_calculator(value.div, value.marr) <= 0:
                wedding_date = value.marr.snake_year_month_day()
                divorce_date = value.div.snake_year_month_day()
                ErrorCollector.error_list.append(f"ERROR: US04: Family {key} has a divorce date {divorce_date} occurs before wedding date {wedding_date}. Divorce date was set to NA.")
                value.div.setNA()

'''User Story 06: Divorce before death'''
def divorce_before_death(family_dict, individual_dict):
    for key_family, value_family in family_dict.items():
        divorce_date = value_family.div
        if divorce_date.snake_year_month_day() != 'NA':
            # husband death
            husband_death = individual_dict[value_family.husb].deat
            if husband_death.snake_year_month_day() != 'NA':
                if age_calculator(husband_death, divorce_date) < 0:
                    ErrorCollector.error_list.append(f"ERROR: US06: Family {key_family} has a divorce date {divorce_date.snake_year_month_day()} occurs after husband's {value_family.husb} death at {husband_death.snake_year_month_day()}. Divorce date was set to NA.")
                    divorce_date.setNA()
            # wife death
            wife_death = individual_dict[value_family.wife].deat
            if wife_death.snake_year_month_day() != 'NA':
                if age_calculator(wife_death, divorce_date) < 0:
                    ErrorCollector.error_list.append(f"ERROR: US06: Family {key_family} has a divorce date {divorce_date.snake_year_month_day()} occurs after wife's {value_family.wife} death at {wife_death.snake_year_month_day()}. Divorce date was set to NA.")
                    divorce_date.setNA()

'''Sprint 2'''
'''User Story 17: No marriages to children'''
def no_marriage_to_children(family_dict, individual_dict):
    for key, individual in individual_dict.items():
        if individual.famc != 'NA' and individual.fams != 'NA':
            husband = family_dict[individual.fams].husb
            wife = family_dict[individual.fams].wife
            father = family_dict[individual.famc].husb
            mother = family_dict[individual.famc].wife
            if husband == father:
                ErrorCollector.error_list.append(f"ERROR: US17: Individual {key} is married to her father {father} which is illegal. Family eliminated.")
                del family_dict[individual.fams]
                individual_dict[husband].fams = 'NA'
                individual.fams = 'NA'
            elif wife == mother:
                ErrorCollector.error_list.append(f"ERROR: US17: Individual {key} is married to his mother {mother} which is illegal. Family eliminated.")
                del family_dict[individual.fams]
                individual.fams = 'NA'
                individual_dict[wife].fams = 'NA'

'''User Story 22: Unique IDs'''
def unique_ids(unfiltered_file):
    individuals = []
    families = []
    for line in unfiltered_file:
        if line == '':
            continue
        else:
            line = line.strip('\n')
            line_split = line.split(' ')
            if line_split[0] == '0':
                if 'INDI' in line_split and line_split[1] != 'INDI':
                    id = line_split[1]
                    if id in individuals:
                        ErrorCollector.error_list.append(f"ERROR: US22: Individual {id} already exists and will override previous data")
                    else:
                        individuals.append(id)
                elif 'FAM' in line_split and line_split[1] != 'FAM':
                    id = line_split[1]
                    if id in families:
                        ErrorCollector.error_list.append(f"ERROR: US22: Family {id} already exists and will override previous data")
                    else:
                        families.append(id)


"""Haoran's Code Goes Here"""
'''Sprint 1'''
'''User Story 11: No Bigamy'''
def no_bigamy(family_dict, individual_dict):
    individual_family_dict = {}
    for key, value in family_dict.items():
        if value.husb not in individual_family_dict:
            individual_family_dict[value.husb] = [key]
        else:
            individual_family_dict[value.husb].append(key)
        if value.wife not in individual_family_dict:
            individual_family_dict[value.wife] = [key]
        else:
            individual_family_dict[value.wife].append(key)
    for key, value in individual_family_dict.items():
        if len(value) > 1:
            # if one individual has more than 1 family.
            # correct their family in individual_dict and delete the second family from family_dict
            # set fams of the unlucky bast**d to NA
            ErrorCollector.error_list.append(f"ERROR: US11: {key} committed bigamy and the second family {value[1]} will be eliminated.")
            individual_dict[key].fams = value[0]
            del family_dict[value[1]]
            for key2, value2 in individual_dict.items():
                if value2.fams == value[1]:
                    value2.fams = 'NA'

'''User Story 12: Parents Not Too Old'''
def parents_not_too_old(family_dict, individual_dict):
    for id, individual in individual_dict.items():
        #print(id, individual)
        if individual.famc != 'NA':
            dad = family_dict[individual.famc].husb
            mom = family_dict[individual.famc].wife

            how_much_older_is_dad = age_calculator(individual.birt, individual_dict[dad].birt)
            how_much_older_is_mom = age_calculator(individual.birt, individual_dict[mom].birt)
            if how_much_older_is_dad != 'NA' and how_much_older_is_dad >= 80:
                ErrorCollector.error_list.append(f"ERROR: US12: {id} has a father who is {how_much_older_is_dad} older which is more than 80 and birthday is set to NA")
                individual_dict[dad].birt.setNA()
            if how_much_older_is_mom != 'NA' and how_much_older_is_mom >= 60:
                ErrorCollector.error_list.append(f"ERROR: US12: {id} has a father who is {how_much_older_is_mom} older which is more than 60 and birthday is set to NA")
                individual_dict[mom].birt.setNA()

"""Sprint 2"""
"""User Story 13: Siblings spacing"""
def siblings_spacing(family_dict, individual_dict):
    for id, individual in individual_dict.items():
        if individual.famc != 'NA':
            siblings = family_dict[individual.famc].chil
            if len(siblings) != 1:
                for child in siblings:
                    if individual_dict[child].birt.year != 'NA' and individual_dict[child].birt.month != 'NA' and individual_dict[child].birt.day != 'NA' and individual.birt.year != 'NA' and individual.birt.month != 'NA' and individual.birt.day != 'NA':
                        sib_age = date(int(float(individual_dict[child].birt.year)), int(float(individual_dict[child].birt.month)), int(float(individual_dict[child].birt.day)))
                        self_age = date(int(float(individual.birt.year)), int(float(individual.birt.month)), int(float(individual.birt.day)))
                        difference = abs(self_age - sib_age).days
                        '''8 months is 240 days '''
                        if difference > 1 and difference < 240:
                            ErrorCollector.error_list.append(f"ERROR: US13: {id} has a sibling whose birth date is too close")


"""User story 14: Mutiple births <= 5"""
def mutiple_birth(family_dict, individual_dict):
    for id, individual in individual_dict.items():
        if individual.famc != 'NA':
            siblings = family_dict[individual.famc].chil
            if len(siblings) > 5:
                birth = 0
                for child in siblings:
                    if individual_dict[child].birt.year != 'NA' and individual_dict[child].birt.month != 'NA' and individual_dict[child].birt.day != 'NA' and individual.birt.year != 'NA' and individual.birt.month != 'NA' and individual.birt.day != 'NA':
                        sib_age = date(int(float(individual_dict[child].birt.year)), int(float(individual_dict[child].birt.month)),
                                       int(float(individual_dict[child].birt.day)))
                        self_age = date(int(float(individual.birt.year)), int(float(individual.birt.month)),
                                        int(float(individual.birt.day)))
                        difference = abs(self_age - sib_age).days
                        '''8 months is 240 days '''
                        if difference <= 1:
                            birth += 1
                        if birth > 5:
                            ErrorCollector.error_list.append(f"ERROR: US14: {id} has too many siblings born at the same time")
                            break


"""Shengda's Code Goes Here"""
'''Sprint 1'''
'''User Story 05: Marriage Before Death'''
def marriage_before_death(family_dict, individual_dict):
    US05_report = {}
    for fam, family in family_dict.items():
        husband_ID = family.husb
        wife_ID = family.wife
        marriage_date = family.marr.snake_year_month_day()
        if husband_ID != 'NA' and wife_ID != 'NA':
            husband_death_date = individual_dict[husband_ID].deat.snake_year_month_day()
            wife_death_date = individual_dict[wife_ID].deat.snake_year_month_day()
            if marriage_date != 'NA':
                if husband_death_date == 'NA' and wife_death_date == 'NA':
                    US05_report[fam] = True
                elif husband_death_date != 'NA' and wife_death_date == 'NA':
                    US05_report[fam] = husband_death_date >= marriage_date
                elif wife_death_date != 'NA' and husband_death_date == 'NA':
                    US05_report[fam] = wife_death_date >= marriage_date
                else:
                    first_death_date = husband_death_date if husband_death_date <= wife_death_date else wife_death_date
                    US05_report[fam] = first_death_date >= marriage_date
    for id, boolean in US05_report.items():
        if boolean == False:
            ErrorCollector.error_list.append(f"ERROR: FAMILY: US05: Family ID: {id} Marriage occur before death of either spouse.")
    #print('5',US05_report)
    return US05_report

'''User Story 07: Less Than 150 Years Old'''
def less_than_150_years_old(individual_dict):
    US07_report = {}
    for id, individual in individual_dict.items():
        indi_death_date = individual.deat.snake_year_month_day()
        indi_birth_date = individual.birt.snake_year_month_day()

        if indi_death_date != 'NA' and indi_birth_date != 'NA':
            today = date.today()
            year, month, day = indi_birth_date.split("-")
            year_dif = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
            if year_dif > 150:
                US07_report[id] = False
            else:
                US07_report[id] = True
        else:
            if age_calculator(date.today(), individual.birt) != 'NA':
                if age_calculator(date.today(), individual.birt) > 150:
                    US07_report[id] = False
                else:
                    US07_report[id] = True
    for id, boolean in US07_report.items():
        if boolean == False:
            ErrorCollector.error_list.append(f"ERROR: INDIVIDUAL: US07: Individual ID: {id} "
                                             f"Death should be less than 150 years after birth for dead people, "
                                             f"and current date should be less than 150 years after birth for all living people")
    #print('7',US07_report)
    return US07_report

'''Sprint 2'''
'''User Story 10: Marriage after 14'''
def marriage_after_14(family_dict, individual_dict):
    US10_report = {}
    for fam, family in family_dict.items():
        #if individual.famc != 'NA':
        husband_ID = family.husb
        wife_ID = family.wife
        marriage_date = family.marr.snake_year_month_day()
        if marriage_date != 'NA':
            husband_birth_day = individual_dict[husband_ID].birt.snake_year_month_day()
            wife_birth_day = individual_dict[wife_ID].birt.snake_year_month_day()

            if calculate_year_dif(husband_birth_day, marriage_date) >= 14\
                and calculate_year_dif(wife_birth_day, marriage_date) >= 14:
                US10_report[fam] = True
            else:
                US10_report[fam] = [marriage_date, husband_birth_day, wife_birth_day]
    for id, boolean in US10_report.items():
        if boolean != True:
            ErrorCollector.error_list.append(f"ERROR: FAMILY: US10: Family ID: {id}, marriage date is {boolean[0]}, "
                  f"husband birth day is {boolean[1]}, wife birth day is {boolean[2]},"
                  f"married before 14 years old.")
    #print('10', US10_report)
    return US10_report

#User Story 10 helper
def calculate_year_dif(one_date_string, another_date_string):
    if one_date_string != 'NA' and another_date_string != 'NA':
        year1, month1, day1 = one_date_string.split("-")
        year2, month2, day2 = another_date_string.split("-")
        year_dif = int(year2) - int(year1) - ((int(month2), int(day2)) < (int(month1), int(day1)))
        return year_dif
    return True

'''User Story 31: List living single'''
def list_living_single(family_dict, individual_dict):
    US31_report = {}

    for indi, individual in individual_dict.items():
        indi_birth_date = individual.birt.snake_year_month_day()
        indi_death_date = individual.deat.snake_year_month_day()
        indi_spouse = individual.fams

        if indi_birth_date != 'NA' and indi_death_date == 'NA':
            if age_calculator(date.today(), individual.birt) >= 30 and indi_spouse == 'NA':
                US31_report[indi] = [age_calculator(date.today(), individual.birt), indi_spouse]
            else:
                US31_report[indi] = False
    for id, boolean in US31_report.items():
        if boolean != False:
            ErrorCollector.error_list.append(f"ERROR: INDIVIDUAL: US31: Individual ID: {id}, Age is {boolean[0]}, FamilyID is {boolean[1]}, "
                  f"who is living people over 30 but have never been married")
    #print('31',US31_report)
    return US31_report



"""Xiangyu's Code Goes Here"""
'''Sprint 1'''
'''User Story 15: Fewer Than 150 Siblings'''
def fewer_than_15_siblings(family_dict, individual_dict):
    for id, family in family_dict.items():
        if len(family.chil) >= 15:
            children = list(family.chil)
            unwanted_children = children[15:]
            ErrorCollector.error_list.append(f"ERROR: US15: Family {id} has more than 15 children and {len(unwanted_children)} child(ren) was removed.")
            for child in unwanted_children:
                individual_dict[child].famc = 'NA'
            family.chil = set(children[:15])

'''User Story 24: Unique Families By Spouses'''
def unique_families_by_spouses(family_dict, individual_dict):
    pass

'''Sprint 2'''
'''User Story 26: Corresponding entries'''
def corresponding_entries(family_dict, individual_dict):
    US26_report ={}
    for id, family in family_dict.items():
        husband_id = family.husb
        wife_id = family.wife
        children = family.chil
        # print("ddddd", children)
        if individual_dict[husband_id].fams != id:
            ErrorCollector.error_list.append(f"ERROR: US26: family id is {id}, wife is {wife_id}, husband is {husband_id} in family record, but in individual record, individual {husband_id} is in {individual_dict[husband_id].fams} family")
            US26_report.setdefault(id, []).append(individual_dict[husband_id].fams)
        if individual_dict[wife_id].fams != id:
            ErrorCollector.error_list.append(f"ERROR: US26: family id is {id}, wife is {wife_id}, husband is {husband_id} in family record, but in individual record, individual {wife_id} is in {individual_dict[husband_id].fams} family")
            US26_report.setdefault(id, []).append(individual_dict[wife_id].fams)
        if children != 'NA':
            for child in children:
                if child != 'NA' and individual_dict[child].famc != 'NA':
                    if individual_dict[child].famc != id:
                        ErrorCollector.error_list.append(f"ERROR: US26: family id is {id}, child {child} in family record, but in individual record, child {child} is in {individual_dict[child].famc} family")
                US26_report.setdefault(id, []).append(individual_dict[child].famc)
        for id, boolean in US26_report.items():
            if boolean != False:
                ErrorCollector.error_list.append(f"ERROR: US26: family id is {id}, wife is {wife_id}, husband is {husband_id} in family record, but in individual record, individual {wife_id} is in {individual_dict[husband_id].fams} family")
    #print("us26", US26_report)
    return US26_report

'''User Story 32: List multiple births'''
def list_multiple_births(individual_dict):
    US32_report = {}
    for id, individual in individual_dict.items():
        birth_date = individual.birt.snake_year_month_day()
        US32_report.setdefault(birth_date, []).append(id)
    for birth_date in US32_report:
        if len(US32_report[birth_date]) > 1:
            ErrorCollector.error_list.append(f"ERROR: INDIVIDUAL: US32: birth day {birth_date} has multiple births {US32_report[birth_date]}")
    for id, boolean in US32_report.items():
        if boolean != False:
            ErrorCollector.error_list.append(f"ERROR: INDIVIDUAL: US32: Individual ID: {id} who are multiple biths")
    #print("us32", US32_report)
    return US32_report


"""Main Function"""
def main():
    '''Operations in Order'''
    # 1. Read the file
    # 2. Filter the file
    # 3. Das Dictionary Für Individual Objects & Das Dictionary Für Family Objects
    # 4. Draw Pretty Tables
    # 5. Print all the errors
    # 6. Export for testing
    #
    file_path = '555Project(updates-often).ged'
    #
    '''Dictionaries of Individuals and Families'''
    individuals = {}
    families = {}
    # 1. Read the file
    with open(file_path, 'r') as file:
        unfiltered_file = file.readlines()
        # 2. Filter the file
        filter_file(unfiltered_file, individuals, families)

    '''Uncomment these if you want to see the individuals and families in raw format'''
    # for key, value in individuals.items():
    #     print(key, value)
    # for key, value in families.items():
    #     print(key, value)

    # 3. Das Dictionary Für Individual Objects & Das Dictionary Für Family Objects
    individual_dict = {}
    family_dict = {}
    '''the next 2 lines fill in the previous 2 lines individual_dict and family_dict'''
    raw_individuals_to_structured_dict(individuals, individual_dict)
    raw_families_to_structured_dict(families, family_dict)

    """User Stories Goes Here"""
    '''Hanqing Sprint 1: US01, US02'''
    dates_before_current_date(individual_dict, family_dict) # US01
    birth_before_marriage(individual_dict, family_dict) # US02
    '''Hanqing Sprint 2: US03, US08'''
    birth_before_death(individual_dict) # US03
    birth_before_marriage_of_parents(individual_dict, family_dict) # US08

    '''Jigar Sprint 1: US04, US06'''
    marriage_before_divorce(family_dict) # US04
    divorce_before_death(family_dict, individual_dict) # US06
    '''Jigar Sprint 2: US17, US22'''
    no_marriage_to_children(family_dict, individual_dict) # US17
    unique_ids(unfiltered_file) #US22

    '''Shengda Sprint 1: US05, US07'''
    marriage_before_death(family_dict, individual_dict) # US05
    less_than_150_years_old(individual_dict) # US07
    '''Shengda Sprint 2: US10, US31'''
    marriage_after_14(family_dict, individual_dict) # US10
    list_living_single(family_dict, individual_dict) # US31

    '''Haoran Sprint 1: US11, US12'''
    no_bigamy(family_dict, individual_dict) # US11
    parents_not_too_old(family_dict, individual_dict) # US12
    '''Haoran Sprint 2: US13, US14'''
    siblings_spacing(family_dict, individual_dict) # US13
    mutiple_birth(family_dict, individual_dict) # US14

    '''Xiangyu Sprint 1: US15, US24'''
    fewer_than_15_siblings(family_dict, individual_dict) # US15
    unique_families_by_spouses(family_dict, individual_dict) # US24
    '''Xiangyu Sprint 2: US26, US32'''
    corresponding_entries(family_dict, individual_dict) # US26
    list_multiple_births(individual_dict) # US32


    '''Uncomment these if you want to see the individual and family objects created from Individual and Family class'''
    # for key, value in individual_dict.items():
    #     print(key, value.name, value.sex, value.birt.snake_year_month_day(), value.deat.snake_year_month_day(), value.famc, value.fams)
    # for key, value in family_dict.items():
    #     print(key, value.marr.snake_year_month_day(), value.husb, value.wife, value.chil, value.div.snake_year_month_day())

    # 4. Draw Pretty Tables
    draw_individual_prettytable(individual_dict)
    draw_family_prettytable(family_dict, individual_dict)

    # 5. Print all errors
    for error in ErrorCollector.error_list:
        print(error)

    # 6. Export for testing
    return [individual_dict, family_dict]


"""Run Main Function"""
if __name__ == '__main__':
    main()