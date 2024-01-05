from prettytable import PrettyTable

import logging
log = logging.getLogger(__name__)

class Host():
    def __init__(self, selections_lst = None):
        self.name = None
        self.zip = None
        self.skill01 = None
        self.skill02 = None
        self.skill03 = None
        self.skill04 = None
        self.skill05 = None
        self.attitude01 = None
        self.attitude02 = None
        self.attitude03 = None
        self.attitude04 = None
        self.attitude05 = None

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


    def __str__(self):
        out_str = ""

        # Specify the Column Names while initializing the Table
        header_lst = []
        header_lst.append("name")
        header_lst.append("zip")
        header_lst.append("Skill 01")
        header_lst.append("Skill 02")
        header_lst.append("Skill 03")
        header_lst.append("Skill 04")
        header_lst.append("Skill 05")
        header_lst.append("Attitude 01")
        header_lst.append("Attitude 02")
        header_lst.append("Attitude 03")
        header_lst.append("Attitude 04")
        header_lst.append("Attitude 05")

        myTable = PrettyTable(header_lst)

        # Add rows
        row_data = []
        row_data.append(self.name)
        row_data.append(self.zip)
        row_data.append(self.skill01)
        row_data.append(self.skill02)
        row_data.append(self.skill03)
        row_data.append(self.skill04)
        row_data.append(self.skill05)
        row_data.append(self.attitude01)
        row_data.append(self.attitude02)
        row_data.append(self.attitude03)
        row_data.append(self.attitude04)
        row_data.append(self.attitude05)

        myTable.add_row(row_data)

        print(myTable)
        return out_str