import DataPool
import pickle


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

    for extern in dp.extern_lst:
        for host in dp.host_lst:
            #print(extern)
            #print(host)
            print(f"Extern {extern.name} matches with host {host.name} : {extern+host} at an aproximate distance of {zip_distance[(extern.zip, host.zip)]}.")

        print()

    log.debug("finished")

if __name__ == "__main__":
    main()
