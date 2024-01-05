import Host
import Extern

import logging
log = logging.getLogger(__name__)


class DataPool:
    def __init__(self):
        self.host_lst = []
        self.extern_lst = []

    def populate_host_list(self):
        filename = r"/home/jamie/source/python/skillMatch/data/host_faux.csv"
        with open(filename) as f:
            data = f.readlines()
        f.close()

        # read in line of data and convert it into a list.
        for row in data:
            raw_host = row.strip()
            raw_host = raw_host.split(",")
            # log.debug(f"length of raw_host : {len(raw_host)} (should be 12).")

            # create a new host object and initialize it with the data in raw host.
            # This transforms the list into an object.
            host_obj = Host.Host(raw_host)

            # append the host object into the list
            self.host_lst.append(host_obj)

    def populate_extern_list(self):
        filename = r"/home/jamie/source/python/skillMatch/data/extern_faux.csv"
        with open(filename) as f:
            data = f.readlines()
        f.close()

        # read in line of data and convert it into a list.
        for row in data:
            raw_extern = row.strip()
            raw_extern = raw_extern.split(",")
            # log.debug(f"length of raw_extern : {len(raw_extern)} (should be 12).")

            # create a new Extern object and initialize it with the data in raw extern.
            # This transforms the list into an object.
            extern_obj = Extern.Extern(raw_extern)

            # append the host object into the list
            self.host_lst.append(extern_obj)

    def print_host_list(self):
        for host in self.host_lst:
            print(host)

    def print_extern_list(self):
        for extern in self.extern_lst:
            print(extern)
