import Host
import Extern
import pickle
import Match

import logging
log = logging.getLogger(__name__)


class DataPool:
    def __init__(self):
        self.host_lst = []
        self.extern_lst = []
        self.match_lst = []

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
            self.extern_lst.append(extern_obj)

        log.debug(f"Length of extern_list : {len(self.extern_lst)}")
    def print_host_list(self):
        for host in self.host_lst:
            print(host)

    def print_extern_list(self):
        for extern in self.extern_lst:
            print(extern)

    def pouulate_match_list(self):

        filename = r"/home/jamie/source/python/skillMatch/data/zip_distance_dict.pickle"
        with open(filename, 'rb') as handle:
            zip_distance_dict = pickle.load(handle)
            handle.close()

        for extern in self.extern_lst:
            for host in self.host_lst:
                distance = zip_distance_dict[(extern.zip, host.zip)]

                #create the empty match object
                match_obj = Match.Match()

                #populate the match object
                match_obj.set_host(host)
                match_obj.set_extern(extern)
                match_obj.set_distance(distance)
                match_obj.set_match_score(extern+host)

                # append the match object into the list
                self.match_lst.append(match_obj)

        log.debug(f"length of match_list is {len(self.match_lst)}")

    def print_match_list(self):
        for m in self.match_lst:
            print(f"{m}")

    def sort_match_list_distance(self):
        self.match_lst.sort(key=lambda match: (match.distance, -1 * match.match_score,))
        # the sort() method of self.match_lst sorts the list in place.
        # the key is used to sort by the distance and match score.
        # we form a tuple here because we want to sort by both.
        # we want to sort by distance, decending (which  is the natural sort direction)
        # we multiple the match score by -1 to reverse the sort direction (i.e. highest values (lowest calculated values) appear first.

