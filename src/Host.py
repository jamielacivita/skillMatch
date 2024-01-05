from AttributeSet import AttributeSet


import logging
log = logging.getLogger(__name__)

class Host(AttributeSet):
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


