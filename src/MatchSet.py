import openpyxl

import Host as Host
import Extern as Extern
import Match as Match
from prettytable import PrettyTable as pt

class MatchSet():

    def parse_host_dataframe(self, dataframe):
        """
        :param dataframe:
        :return: a list of lists holding the information in the dataframe.
        """

        out_lst = []

        FIRST_DATA_ROW = 2

        for row in dataframe.iter_rows(FIRST_DATA_ROW, dataframe.max_row):
            ## each row represents a host
            ## create and populate host object
            host_obj = Host.Host(row)
            out_lst.append(host_obj)

        return out_lst

    def get_extern_dataframe(self):
        print("foo_populate_Extern")
        filename = r"/home/jamie/PycharmProjects/skillMatch/data/240218-055306_Educator.xlsx"

        dataframe = openpyxl.load_workbook(filename)
        dataframe1 = dataframe.active

        return dataframe1

    def parse_extern_dataframe(self, dataframe):
        out_lst = []
        FIRST_DATA_ROW = 2
        for row in dataframe.iter_rows(FIRST_DATA_ROW, dataframe.max_row):
            extern_obj = Extern.Extern(row)
            out_lst.append(extern_obj)

        return out_lst

    def get_host_objects_lst(self):
        host_dataframe = self.get_host_dataframe()
        host_objects_lst = self.parse_host_dataframe(host_dataframe)
        return host_objects_lst

    def get_extern_obj_lst(self):
        extern_dataframe = self.get_extern_dataframe()
        extern_objects_lst = self.parse_extern_dataframe(extern_dataframe)
        return extern_objects_lst

    def get_match_object_lst(self):

        match_obj_list = []
        for extern in self.get_extern_obj_lst():
            for host in self.get_host_objects_lst():
                # make a empty match object.
                match_obj = Match.Match(extern, host)
                match_obj_list.append(match_obj)

        return match_obj_list

    def get_host_dataframe(self, host_filename="/home/jamie/PycharmProjects/skillMatch/data/240218-055238_Host.xlsx"):
        """
        Given a path to a host file return a dataframe records.
        :return:
        """
        dataframe = openpyxl.load_workbook(host_filename)
        dataframe1 = dataframe.active

        return dataframe1

    def __init__(self):
        self.extern_obj_lst = self.get_extern_obj_lst()
        self.host_obj_lst = self.get_host_objects_lst()
        self.match_obj_lst = self.get_match_object_lst()

    def get_number_hosts(self):
        return len(self.host_obj_lst)

    def get_number_externs(self):
        return len(self.extern_obj_lst)


    def get_number_matches(self):
        return len(self.match_obj_lst)

    def print_match_chart(self):
        out_table = pt()
        out_table.field_names = ["KEY", "EXTERN", "HOST", "DISTANCE"]
        for match in self.match_obj_lst:
            out_row = []
            out_row.append(f"{match.get_key()}")
            out_row.append(f"{match.get_extern_name()}")
            out_row.append(f"{match.get_host_name()}")
            out_row.append(f"{match.get_distance()}")

            out_table.add_row(out_row)

        print(out_table)

    def print_extern_city(self):
        for extern_obj in self.extern_obj_lst:
            print(extern_obj.get_city_you_live_in())
