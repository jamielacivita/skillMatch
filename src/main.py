import DataPool
import pickle
import openpyxl
import Host as Host
import Extern as Extern
import Skills as Skills


import logging.config
#logging.config.fileConfig("/home/jamie/source/python/skillMatch/src/logging_config.ini")
logging.config.fileConfig("/home/jamie/PycharmProjects/skillMatch/src/logging_config.ini")


log = logging.getLogger(__name__)

def main():

    ## load the dictionary of distances between zip codes.
    pickle_file = r"/home/jamie/PycharmProjects/skillMatch/data/distance_miles.pickle"
    with open(pickle_file, 'rb') as handle:
        zip_distance = pickle.load(handle)

    dp = DataPool.DataPool()
    dp.populate_host_list()
    dp.populate_extern_list()
    #dp.print_host_list()
    #dp.print_extern_list()


    output_file = r"/home/jamie/PycharmProjects/skillMatch/data/out.txt"
    with open(output_file,"w") as output_file:
        for extern in dp.extern_lst:
            for host in dp.host_lst:
                #print(extern)
                #print(host)
                #print(f"Extern {extern.name} matches with host {host.name} : {extern+host} at an aproximate distance of {zip_distance[(extern.zip, host.zip)]}.")
                out_row = f"Extern {extern.name} matches with host {host.name} {extern+host} times at an approximate distance of {zip_distance[(extern.zip, host.zip)]}\n"
                output_file.write(out_row)
            output_file.write("\n")
    output_file.close()

    log.debug("finished")

def host_generate_field_headings(filename="/home/jamie/PycharmProjects/skillMatch/data/240218-055238_Host.xlsx"):
    """
    Given a path to a host file return a list of headings for the records.
    :return:
    """
    dataframe = openpyxl.load_workbook(filename)
    dataframe1 = dataframe.active
    for row in range(0, dataframe1.max_row):
    #for row in range(1, 2):
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            cell = col[row]
            if cell.column_letter == "AJ":
                print(f" {cell.column_letter} : {cell.value}")

def host_get_dataframe(filename="/home/jamie/PycharmProjects/skillMatch/data/240218-055238_Host.xlsx"):
    """
    Given a path to a host file return a dataframe records.
    :return:
    """
    dataframe = openpyxl.load_workbook(filename)
    dataframe1 = dataframe.active

    return dataframe1

def host_parse_dataframe(dataframe):
    """
    :param dataframe:
    :return: a list of lists holding the information in the dataframe.
    """

    hosts_obj_lst = []

    #for row in range(2, dataframe.max_row):


        #for col in dataframe.iter_cols(1, dataframe.max_column):
            #cell = col[row]
            #column_letter = cell.column_letter

    FIRST_DATA_ROW = 2


    for row in dataframe.iter_rows(FIRST_DATA_ROW, dataframe.max_row):
    ## each row represents a host
    ## create and populate host object
        host_obj = Host.Host(row)
        print(host_obj)



    print("done.")


def foo_populate_Extern():
    print("foo_populate_Extern")
    filename = r"/home/jamie/PycharmProjects/skillMatch/data/240218-055306_Educator.xlsx"

    dataframe = openpyxl.load_workbook(filename)
    dataframe1 = dataframe.active

    print(dataframe1)

    FIRST_DATA_ROW = 2
    for row in dataframe1.iter_rows(FIRST_DATA_ROW, dataframe1.max_row):
        extern_obj = Extern.Extern(row)
        print(extern_obj)


def foo_Skills():
    print("In foo_skills")
    print("Make a skills object and print it out.")
    skills_obj = Skills.Skills()
    print(skills_obj)
    print("toggle curiculum design.")
    skills_obj.set_curriculum_design(True)
    skills_obj.set_software_email(True)
    skills_obj.set_software_presentation(True)
    skills_obj.set_software_presentation(True)
    print(skills_obj)





if __name__ == "__main__":
    #main()
    #host_generate_field_headings()

    df = host_get_dataframe()
    host_parse_dataframe(df)
    #foo_populate_Extern()
    #foo_Skills()


