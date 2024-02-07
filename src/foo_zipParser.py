import csv
import haversine
from haversine import Unit
import pickle

def main():
    print("In foo_zipParser")
    input_file = r"/home/jamie/PycharmProjects/skillMatch/data/uszips.csv"
    output_file = r"/home/jamie/PycharmProjects/skillMatch/data/uszips_idaho.csv"
    idaho_zips = []

    ## read in the .csv file which contains zips for the entire country.
    ## create a list of lists (idaho_zips) of only those that are in Idaho.
    with open(input_file, newline='') as uszips:
        reader = csv.reader(uszips, delimiter=",",quotechar='"')
        for row in reader:
            if row[4] == "ID":
                idaho_zips.append(row)
    uszips.close()

    ## write a .csv file generated from the subset of the zips in Idaho.
    with open(output_file, 'w', newline='') as idzips:
        spamwriter = csv.writer(idzips, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in idaho_zips:
            spamwriter.writerow(row)
    idzips.close()


def hav(loc1,loc2):
    #loc1 = (43.35079, 116.6357)
    #loc2 = (43.57334, 116.40116)

    result = haversine.haversine(loc1, loc2, unit=Unit.MILES)
    result = int(result)
    #print("The distance calculated is:", result)
    return result

def make_dict():
    distance_miles = {}

    input_file = r"/home/jamie/PycharmProjects/skillMatch/data/uszips.csv"
    idaho_zips = []
    with open(input_file, newline='') as uszips:
        reader = csv.reader(uszips, delimiter=",",quotechar='"')
        for row in reader:
            if row[4] == "ID":
                idaho_zips.append(row)
    uszips.close()

    #for row in idaho_zips:
        #print(row)

    zip_pairs = []
    for first_row in idaho_zips:
        for second_row in idaho_zips:
            #zip_pairs.append(f"{first_row} : {second_row}")
            first_row_lat = float((first_row[1]))
            first_row_lon = abs(float(first_row[2]))
            second_row_lat = float(second_row[1])
            second_row_lon = abs(float(second_row[2]))

            distance_miles[(first_row[0],second_row[0])]=hav((first_row_lat,first_row_lon),(second_row_lat,second_row_lon))
            #for n in distance_miles.keys():
                #print(f"{n} : {distance_miles[n]}")

    pickle_file = r"/home/jamie/PycharmProjects/skillMatch/data/distance_miles.pickle"
    with open(pickle_file, 'wb') as handle:
        pickle.dump(distance_miles, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    #main()
    #hav()
    make_dict()
