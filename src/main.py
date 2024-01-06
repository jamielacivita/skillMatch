import itertools

import DataPool
import csv
import pickle
import haversine

import logging.config
logging.config.fileConfig("/home/jamie/source/python/skillMatch/src/logging_config.ini")
log = logging.getLogger(__name__)

def main():

    filename = r"/home/jamie/source/python/skillMatch/data/zip_distance_dict.pickle"
    with open(filename, 'rb') as handle:
        zip_distance_dict = pickle.load(handle)
        handle.close()

    dp = DataPool.DataPool()
    dp.populate_host_list()
    dp.populate_extern_list()
    dp.pouulate_match_list()
    #dp.print_host_list()
    #dp.print_extern_list()
    dp.sort_match_list_distance()
    dp.print_match_list()
    log.debug("finished")

def zips():
    print("In zips")
    zip_distance_dict = {}
    #zip_dict = {}
    #filename = r"/home/jamie/source/python/skillMatch/data/uszips.csv"
    #with open(filename, newline='') as csvfile:
        #zipreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        #for row in zipreader:
            #if row[4] == "ID":
                #print(row)
                #zip_dict[row[0]]=(row[1],row[2],row[3],row[11])
                #print(zip_dict[row[0]])
    #csvfile.close()

    #filename = r"/home/jamie/source/python/skillMatch/data/zip_dict.pickle"
    #with open(filename, 'wb') as handle:
        #pickle.dump(zip_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    #with open(filename, 'rb') as handle:
        #zip_dict = pickle.load(handle)
        #handle.close()

    # there are 279 zipcodes in Idaho.
    # get the cartsean products of the list of zipcodes. (77841)
    # somelists = [zip_dict.keys(), zip_dict.keys()]
    # for element in itertools.product(*somelists):
        #here element is a tuple of the pared zipcodes.

        #geneate the key
        #key = (element[0],element[1])

        # get the coordinates for the two zipcodes.  We need to convert them to floats to use in the distance formula.
        # lat_a = float(zip_dict[element[0]][0])
        # lon_a = float(zip_dict[element[0]][1])
        # lat_b = float(zip_dict[element[1]][0])
        # lon_b = float(zip_dict[element[1]][1])



        # calculate the distance
        # this will be the value of our dictionary
        # distance = haversine.haversine((lat_a,lon_a),(lat_b,lon_b))

        # print(distance)

        # add into the dictionary.
        #zip_distance_dict[key] = distance

    #print(len(zip_distance_dict.keys()))
    #print(zip_distance_dict[("83702","83840")])

    #pickle the dictionary we have created
    #filename = r"/home/jamie/source/python/skillMatch/data/zip_distance_dict.pickle"
    #with open(filename, 'wb') as handle:
    #    pickle.dump(zip_distance_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    #handle.close()


def add(num1, num2):
    return num1+num2


if __name__ == "__main__":
    main()
    #zips()