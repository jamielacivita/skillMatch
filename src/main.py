import DataPool


import logging.config
logging.config.fileConfig("/home/jamie/source/python/skillMatch/src/logging_config.ini")
log = logging.getLogger(__name__)

def main():

    dp = DataPool.DataPool()
    dp.populate_host_list()
    dp.populate_extern_list()
    #dp.print_host_list()
    dp.print_extern_list()


if __name__ == "__main__":
    main()
