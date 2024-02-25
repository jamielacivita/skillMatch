import pickle
import Skills as Skills

# Load in the dictionary that holds in the distances between zipcodes.
with open('/home/jamie/PycharmProjects/skillMatch/data/distance_miles.pickle', 'rb') as distance:
    distance_dict = pickle.load(distance)

class Match():

    def __init__(self, extern_obj, host_obj):

        self.extern_obj = extern_obj
        self.host_obj = host_obj

        self.key = (extern_obj.get_id(), host_obj.get_id())
        self.host_name = f"{self.host_obj.get_organization_name()}"
        self.extern_name = f"{self.extern_obj.get_last_name()}, {self.extern_obj.get_first_name()}"

        ## Perform Matching on Skills
        self.stem_experience_match_score = 0
        self.skills = Skills.Skills()
        extern_skills = self.extern_obj.skills
        host_skills = self.host_obj.skills

        #stemexp_na - don't match on this.
        #stemexp_lifesci
        if (extern_skills.stemexp_lifesci and host_skills.stemexp_lifesci):
            self.skills.set_stemexp_lifesci(True)
            self.skills.set_stemexp_notes("lifesci")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_chem
        if (extern_skills.stemexp_chem and host_skills.stemexp_chem):
            self.skills.set_stemexp_chem(True)
            self.skills.set_stemexp_notes("chem")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_phys
        if (extern_skills.stemexp_phys and host_skills.stemexp_phys):
            self.skills.set_stemexp_phys(True)
            self.skills.set_stemexp_notes("phys")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_math
        if (extern_skills.stemexp_math and host_skills.stemexp_math):
            self.skills.set_stemexp_math(True)
            self.skills.set_stemexp_notes("math")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_compsci
        if (extern_skills.stemexp_compsci and host_skills.stemexp_compsci):
            self.skills.set_stemexp_compsci(True)
            self.skills.set_stemexp_notes("compsci")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_it
        if (extern_skills.stemexp_it and host_skills.stemexp_it):
            self.skills.set_stemexp_it(True)
            self.skills.set_stemexp_notes("it")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_ag
        if (extern_skills.stemexp_ag and host_skills.stemexp_ag):
            self.skills.set_stemexp_ag(True)
            self.skills.set_stemexp_notes("ag")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_eng
        if (extern_skills.stemexp_eng and host_skills.stemexp_eng):
            self.skills.set_stemexp_eng(True)
            self.skills.set_stemexp_notes("eng")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_health
        if (extern_skills.stemexp_health and host_skills.stemexp_health):
            self.skills.set_stemexp_health(True)
            self.skills.set_stemexp_notes("health")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_trade
        if (extern_skills.stemexp_trade and host_skills.stemexp_trade):
            self.skills.set_stemexp_trade(True)
            self.skills.set_stemexp_notes("trade")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_env
        if (extern_skills.stemexp_env and host_skills.stemexp_env):
            self.skills.set_stemexp_env(True)
            self.skills.set_stemexp_notes("env")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
        #stemexp_other - don't match on this.



        #self.extern_zip = extern_obj.get_zip()
        #self.host_zip = host_obj.get_zip()
        self.distance = None
        self.distance_notes = ""
        self.remote_match = None

        self.match_score = 0

        ## Calculate Distance (self.distance) ##
        # we find distance by using a dictionary which stores the distances in miles between zipcodes.
        extern_zip = self.extern_obj.get_zip()
        host_zip = self.host_obj.get_zip()
        distance_from_dictionary = distance_dict.get((extern_zip,host_zip))
        if distance_from_dictionary is not None:
            self.distance = distance_from_dictionary
            self.set_distance_notes(f"{extern_zip}<-->{host_zip}")

        else:
            # if you are here the dictionary lookup has failed.
            if host_zip == "remote":
                self.distance = 0
                self.set_distance_notes("host zip is 'remote'")
            else:
                self.distance = 9999
                print(f"extern {self.extern_obj.get_id()} zip : {extern_zip} -- host {self.host_obj.get_id()} zip : {host_zip}")
            #print(distance_dict[(extern_zip,host_zip)])

        ## set remote match ##
        # A remote match is Extern V (what work locations are you open to) and Host AN (can this work be done remotely)
        extern_remote_match = self.extern_obj.get_what_work_locations()
        host_remote_match = self.host_obj.get_work_done_remotely()

        if ("Remote" in extern_remote_match) and ("Yes" in host_remote_match):
            self.set_remote_match(True)
        else:
            self.set_remote_match(False)


    def __str__(self):
        out_str = ""
        out_str = out_str + "\n"
        out_str = out_str + f"key : {self.key} : match score : {self.match_score}\n"
        out_str = out_str + (f"curriculum design match : {self.curriculum_design_match}\n")
        out_str = out_str + "-- host object skills --\n"
        out_str = out_str + f"{self.host_obj.skills}\n"
        out_str = out_str + "-- extern object skills --\n"
        out_str = out_str + f"{self.extern_obj.skills}\n"
        out_str = out_str + self.print_skill_chart()
        out_str = out_str + "\n"
        return out_str

    def print_skill_chart(self):
        out_str = ""

        out_str = out_str + f"curriculum design : "
        out_str = out_str + f"{self.extern_obj.skills.curriculum_design} :"
        out_str = out_str + f"{self.host_obj.skills.curriculum_design}\n"


        return out_str

    def get_key(self):
        return self.key

    def get_extern_name(self):
        return self.extern_name

    def get_host_name(self):
        return self.host_name

    def get_distance(self):
        return self.distance

    def set_distance_notes(self, note):
        self.distance_notes = self.distance_notes + note
    def get_distance_notes(self):
        return self.distance_notes

    def set_remote_match(self, remote_match):
        self.remote_match = remote_match
        return None

    def get_remote_match(self):
        return self.remote_match

    def get_stem_experience_match_score(self):
        return self.stem_experience_match_score

    def get_stem_experience_match_notes(self):
        return self.skills.get_stemexp_notes()
