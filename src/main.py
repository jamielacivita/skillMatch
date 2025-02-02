import MatchSet as MatchSet
import data_config

import logging.config
logging_config_file = data_config.LoggingConfigurationFile
logging.config.fileConfig(logging_config_file)
log = logging.getLogger(__name__)

def host_generate_field_headings(filename="/home/jamie/PycharmProjects/skillMatch/data/240218-055238_Host.xlsx"):
    """
    Given a path to a host file return a list of headings for the records.
    :return:
    """
    dataframe = openpyxl.load_workbook(filename)
    dataframe1 = dataframe.active
    for row in range(0, dataframe1.max_row):
        # for row in range(1, 2):
        for col in dataframe1.iter_cols(1, dataframe1.max_column):
            cell = col[row]
            if cell.column_letter == "AJ":
                print(f" {cell.column_letter} : {cell.value}")

if __name__ == "__main__":

    log.debug("Generate a Match set Object")
    match_set_object = MatchSet.MatchSet()

    log.debug("Print host dossiers.")
    match_set_object.print_host_dossiers()
    log.debug("Print extern dossiers.")
    match_set_object.print_extern_dossiers()

    # match_set_object.print_match_chart()
    log.debug("save match chart")
    match_set_object.save_match_chart_csv()

    log.info(f"Number of externs : {match_set_object.get_number_externs()}")
    log.info(f"Number of hosts : {match_set_object.get_number_hosts()}")
    log.info(f"Number of matches : {match_set_object.get_number_matches()}")

    print("Done.")
