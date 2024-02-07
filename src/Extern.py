from AttributeSet import AttributeSet

import logging
log = logging.getLogger(__name__)
print(log)
class Extern(AttributeSet):
    def __init__(self, selections_lst = None):

        if selections_lst:
            self.name = selections_lst[0]
            self.zip = selections_lst[1]
            self.skill01 = selections_lst[2]
            self.skill02 = selections_lst[3]
            self.skill03 = selections_lst[4]
            self.skill04 = selections_lst[5]
            self.skill05 = selections_lst[6]
            self.attitude01 = selections_lst[7]
            self.attitude02 = selections_lst[8]
            self.attitude03 = selections_lst[9]
            self.attitude04 = selections_lst[10]
            self.attitude05 = selections_lst[11]

    def __add__(self, other):
        number_of_matches = 0

        if self.skill01 == other.skill01:
            number_of_matches = number_of_matches + 1
            #log.debug(f"Skill01 Match : {self.skill01} == {other.skill01}")
        else:
            pass

        if self.skill02 == other.skill02:
            number_of_matches = number_of_matches + 1
        else:
            pass

        if self.skill03 == other.skill03:
            number_of_matches = number_of_matches + 1
        else:
            pass

        if self.skill04 == other.skill04:
            number_of_matches = number_of_matches + 1
        else:
            pass

        if self.skill05 == other.skill05:
            number_of_matches = number_of_matches + 1
        else:
            pass

        if self.attitude01 == other.attitude01:
            number_of_matches = number_of_matches + 1
        else:
            pass

        if self.attitude02 == other.attitude02:
            number_of_matches = number_of_matches + 1
        else:
            pass

        if self.attitude03 == other.attitude03:
            number_of_matches = number_of_matches + 1
        else:
            pass

        if self.attitude04 == other.attitude04:
            number_of_matches = number_of_matches + 1
        else:
            pass

        if self.attitude05 == other.attitude05:
            number_of_matches = number_of_matches + 1
        else:
            pass

        return number_of_matches

