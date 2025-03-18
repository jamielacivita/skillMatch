import Host
import Extern

import logging
log = logging.getLogger(__name__)


class DataPool:
    def __init__(self):
        self.host_lst = []
        self.extern_lst = []

    def populate_host_list(self):
        filename = r"/home/jamie/PycharmProjects/skillMatch/data/host_faux.csv"
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
        filename = r"/home/jamie/PycharmProjects/skillMatch/data/extern_faux.csv"
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

    def get_city_dictionary(self):

        city_zip = {}
        city_zip["Ada County"] = 83706
        city_zip["Ammon "] = 83406
        city_zip["Arco"] = 83213
        city_zip["Bellevue"] = 83313
        city_zip["Blackfoot "] = 83221
        city_zip["Blackfoot"] = 83221
        city_zip["Blackfooot "] = 83221
        city_zip["Boise"] = 83706
        city_zip["Boise "] = 83706
        city_zip["Boise, ID"] = 83706
        city_zip["Boise, Idaho"] = 83706
        city_zip[
            "Gooding, Idaho, but I have a residence in Boise, ID that I can stay at during summer break if needed. "] = 83706
        city_zip["Boise County, halfway between Idaho City and Boise"] = 83716
        city_zip["Bonner Ferry and Rathdrum"] = 83805
        city_zip["Buhl"] = 83316
        city_zip["Burley"] = 83318
        city_zip["Burley, ID"] = 83318
        city_zip["Burley, Idaho"] = 83318
        city_zip["Caldwell"] = 83606
        city_zip["Caldwell "] = 83606
        city_zip["Caldwell, ID"] = 83606
        city_zip["Caldwell but more than willing to travel for a great fit!"] = 83606
        city_zip["Carey"] = 83320
        city_zip["Cataldo, ID"] = 83810
        city_zip["Chubbuck"] = 83202
        city_zip["Clarkston"] = 99403
        city_zip["Coeur d'Alene"] = 83815
        city_zip["Coeur d' Alene"] = 83815
        city_zip["Coeur d'Alene "] = 83815
        city_zip["Coeur d\"Alene"] = 83815
        city_zip["Coeur d Alene"] = 83815
        city_zip["Craigmont"] = 83523
        city_zip["Dayton"] = 83232
        city_zip["Dayton, Idaho"] = 83232
        city_zip["Dietrich "] = 83324
        city_zip["Downey"] = 83234
        city_zip["Driggs, ID"] = 83422
        city_zip["Driggs"] = 83422
        city_zip["Eagle"] = 83616
        city_zip["Eagle, ID"] = 83616
        city_zip["Eagle, Idaho"] = 83616
        city_zip["Emmett"] = 83617
        city_zip["Garden Valley"] = 83622
        city_zip["Glenns Ferry"] = 83623
        city_zip["Gooding"] = 83330
        city_zip["Grace"] = 83241
        city_zip["Grand View"] = 83624
        city_zip["Hailey"] = 83333
        city_zip["Hailey, ID"] = 83333
        city_zip["Heyburn"] = 83336
        city_zip["Heyburn (moving to Idaho Falls area this summer)  83401"] = 83401
        city_zip["Hayden Id"] = 83335
        city_zip["Hazelton, ID"] = 83335
        city_zip["Hazelton"] = 83335
        city_zip["Jerome"] = 83338
        city_zip["Idaho City"] = 83631
        city_zip["Idaho Falls"] = 83402
        city_zip["Idaho Falls "] = 83402
        city_zip["Idaho falls "] = 83402
        city_zip["Idaho Falls, ID"] = 83402
        city_zip["Idaho Falls, Idaho "] = 83402
        city_zip["Inkom"] = 83245
        city_zip["Kellogg"] = 83868
        city_zip["Kuna, Idaho"] = 83642
        city_zip["Kuna"] = 83642
        city_zip["Lewiston"] = 83501
        city_zip["Lewiston "] = 83501
        city_zip["Lewiston ID"] = 83501
        city_zip["Lewiston, ID"] = 83501
        city_zip["Logan"] = 84321
        city_zip["Malta"] = 83342
        city_zip["McCall"] = 83638
        city_zip["McCammon"] = 83250
        city_zip["McCammon, Idaho"] = 83250
        city_zip["Melba"] = 83641
        city_zip["Meridian"] = 83646
        city_zip["Meridian, Idaho"] = 83646
        city_zip["Meridian and Garden Valley"] = 83646
        city_zip["Meridian (Near Roaring Springs Water Park)"] = 83646
        city_zip["Middleton"] = 83646
        city_zip["Middleton "] = 83646
        city_zip["Midvale "] = 83645
        city_zip["Montpelier"] = 83254
        city_zip["moscow "] = 83843
        city_zip["Moscow"] = 83843
        city_zip["Mountain Home"] = 83647
        city_zip["Mountain Home "] = 83647
        city_zip["mountain home"] = 83647
        city_zip["Mountain Home, Idaho"] = 83647
        city_zip["Nampa"] = 83651
        city_zip["Nampa "] = 83651
        city_zip["Nampa, ID"] = 83651
        city_zip["Nampa, Idaho"] = 83651
        city_zip["Nezperce"] = 83543
        city_zip["Oakley"] = 83346
        city_zip["Palouse, WA"] = 99161
        city_zip["Parma Idaho"] = 83660
        city_zip["Parker, Idaho- live; work in Rexburg, Idaho "] = 83438
        city_zip["Paul"] = 83347
        city_zip["Pocatello"] = 83205
        city_zip["Pocatello, ID"] = 83205
        city_zip["Pocatello, Idaho "] = 83205
        city_zip["Pocatello Idaho"] = 83205
        city_zip["Post Falls"] = 83854
        city_zip["Potlatch"] = 83855
        city_zip["Preston"] = 83263
        city_zip["Preston, ID"] = 83263
        city_zip["Princeton, Idaho"] = 83857
        city_zip["Rathdrum"] = 83858
        city_zip["Rathdrum, ID"] = 83858
        city_zip["Rexburg"] = 83440
        city_zip["Rexburg "] = 83440
        city_zip["Rexburg, ID"] = 83440
        city_zip["Rexburg, Idaho"] = 83440
        city_zip["Richfield"] = 83349
        city_zip["Richfield, Idaho"] = 83349
        city_zip["Richfield, ID"] = 83349
        city_zip["Rigby"] = 83442
        city_zip["Riggins"] = 83549
        city_zip["Ririe"] = 83443
        city_zip["Ririe/Idaho Falls"] = 83443
        city_zip["Robin, Idaho (Arimo)"] = 83214
        city_zip["Rupert"] = 83350
        city_zip["Rupert, ID"] = 83350
        city_zip["St. Anthony"] = 83445
        city_zip["Saint anthony"] = 83445
        city_zip["St Anthony Idaho"] = 83445
        city_zip["Sandpoint"] = 83864
        city_zip["Sandpoint "] = 83864
        city_zip["Shelley"] = 83274
        city_zip["Shoshone "] = 83352
        city_zip["Spirit Lake, Idaho but I commute to Coeur d'Alene daily. "] = 83869
        city_zip["Star"] = 83646
        city_zip["Spokane Valley, WA"] = 99212
        city_zip["Sugar City Idaho"] = 83448
        city_zip["Twin Falls"] = 83301
        city_zip["Twin Falls, Idaho"] = 83301
        city_zip["Wallace, Id"] = 83873
        city_zip["Weiser"] = 83672
        city_zip["Wilder"] = 83303
        city_zip[""] = 99999

        return city_zip

