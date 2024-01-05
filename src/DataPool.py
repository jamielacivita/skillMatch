import Host

import logging
log = logging.getLogger(__name__)



class DataPool():
    def __init__(self):
        self.host_lst = []
        self.extern_lst = []

    def populate_host_list(self):
        filename = r"/home/jamie/source/python/skillMatch/data/host_faux.csv"
        with open(filename) as f:
            data = f.readlines()
        f.close()

        # read in line of data and convert it into a list.
        for l in data:
            raw_host = l.strip()
            raw_host = raw_host.split(",")
            #log.debug(f"length of raw_host : {len(raw_host)} (should be 12).")

            # create a new host object and initalize it with the data in raw host.  This transforms the list into an object.
            host_obj = Host.Host(raw_host)

            # append the host object into the list
            self.host_lst.append(host_obj)

    def print_host_list(self):
        for host in self.host_lst:
            print(host)
