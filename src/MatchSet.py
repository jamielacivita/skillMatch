import openpyxl
import csv
import time

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

    def get_match_chart_header_row(self):
        return ["Extern ID", "Host ID", "EXTERN", "EXTERN CITY", "HOST", "HOST CITY","HOST NO EXP NEEDED", "DISTANCE", "DISTANCE NOTES", "REMOTE MATCH", "REMOTE ONLY", "STEM experience match", "STEM experience matched on", "Biz Skills Score", "Biz Skills Match", "Work Style Score", "Work Style Notes", "Teaching Needs Match", "Curriculum Needs Match", "Total Experience Match"]

    def get_match_chart_data_rows(self, extern_id = None):
        out_rows = []
        for match in self.match_obj_lst:
            out_row = []

            #out_row.append(f"{match.get_key()}")
            out_row.append(f"{match.get_extern_id()}")
            out_row.append(f"{match.get_host_id()}")
            out_row.append(f"{match.get_extern_name()}")
            out_row.append(f"{match.get_extern_city()}")
            out_row.append(f"{match.get_host_name()}")
            out_row.append(f"{match.get_host_city()}")
            out_row.append(f"{match.get_host_no_skills_needed()}")
            out_row.append(f"{match.get_distance()}")
            out_row.append(f"{match.get_distance_notes()}")
            out_row.append(f"{match.get_remote_match()}")
            out_row.append(f"{match.get_extern_remote_only()}")
            out_row.append(f"{match.get_stem_experience_match_score()}")
            out_row.append(f"{match.get_stem_experience_match_notes()}")
            out_row.append(f"{match.get_biz_skills_match_score()}")
            out_row.append(f"{match.get_biz_skills_match_notes()}")
            out_row.append(f"{match.get_work_style_match_score()}")
            out_row.append(f"{match.get_work_style_match_notes()}")
            out_row.append(f"{match.get_teaching_needs_match()}")
            out_row.append(f"{match.get_curriculum_design_match()}")
            out_row.append(f"{match.get_total_score()}")

            out_rows.append(out_row)

        return out_rows

    def print_match_chart(self):

        out_table = pt()
        out_table.field_names = self.get_match_chart_header_row()
        for row in self.get_match_chart_data_rows():
            out_table.add_row(row)

        print(out_table)
        return None

    def print_extern_city(self):
        """
        :return: None : printed output is a list of cities that Externs live in.
        """
        for extern_obj in self.extern_obj_lst:
            print(extern_obj.get_city_you_live_in())

    def save_match_chart_csv(self):
        """
        :return: None - effect is to save the match chart data to a CSV.
        """
        path = f"/home/jamie/PycharmProjects/skillMatch/data/"
        filename = f"{time.strftime('%Y%m%d-%H%M%S')}_out.csv"
        path_to_file = path + filename
        with open(path_to_file, "w", newline='') as csvfile:
            match_chart_write = csv.writer(csvfile)
            match_chart_write.writerow(self.get_match_chart_header_row())
            for row in self.get_match_chart_data_rows():
                match_chart_write.writerow(row)
        csvfile.close()
        return None
