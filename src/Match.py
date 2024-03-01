import logging
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
        self.host_id = f"{host_obj.get_id()}"
        self.host_name = f"{self.host_obj.get_organization_name()}"
        self.host_city = f"{self.host_obj.get_location_of_organization()}"
        self.host_no_skills_needed = f"{self.host_obj.get_no_skills_needed()}"

        self.extern_id = f"{extern_obj.get_id()}"
        self.extern_name = f"{self.extern_obj.get_last_name()}, {self.extern_obj.get_first_name()}"
        self.extern_city = f"{self.extern_obj.get_city_you_live_in()}"
        self.extern_remote_only = f"{self.extern_obj.get_remote_only()}"

        # Teaching/Curriculum Needs Match Data #
        self.teaching_needs_match = None
        self.curriculum_design_match = None

        ## Perform Matching on Skills
        self.stem_experience_match_score = 0
        self.biz_skills_match_score = 0
        self.work_style_match_score = 0

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


        ## Business Skills Match
        #skills_biz_na
        if extern_skills.skills_biz_na and host_skills.skills_biz_na:
            self.skills.set_skills_biz_na(True)
            self.skills.set_skills_biz_notes("na")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_biz_sheets
        if extern_skills.skills_biz_sheets and host_skills.skills_biz_sheets:
            self.skills.set_skills_biz_sheets(True)
            self.skills.set_skills_biz_notes("sheets")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_biz_word
        if extern_skills.skills_biz_word and host_skills.skills_biz_word:
            self.skills.set_skills_biz_word(True)
            self.skills.set_skills_biz_notes("word")
            self.biz_skills_match_score = self.biz_skills_match_score + 1


        #skills_biz_slides
        if extern_skills.skills_biz_slides and host_skills.skills_biz_slides:
            self.skills.set_skills_biz_slides(True)
            self.skills.set_skills_biz_notes("slides")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_biz_pm
        if extern_skills.skills_biz_pm and host_skills.skills_biz_pm:
            self.skills.set_skills_biz_pm(True)
            self.skills.set_skills_biz_notes("pm")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_biz_speaking
        if extern_skills.skills_biz_speaking and host_skills.skills_biz_speaking:
            self.skills.set_skills_biz_speaking(True)
            self.skills.set_skills_biz_notes("speaking")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_biz_email
        if extern_skills.skills_biz_email and host_skills.skills_biz_email:
            self.skills.set_skills_biz_email(True)
            self.skills.set_skills_biz_notes("email")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_ed_secondary
        if extern_skills.skills_ed_secondary and host_skills.skills_ed_secondary:
            self.skills.set_skills_ed_secondary(True)
            self.skills.set_skills_biz_notes("secondary")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_ed_adult
        if extern_skills.skills_ed_adult and host_skills.skills_ed_adult:
            self.skills.set_skills_ed_adult(True)
            self.skills.set_skills_biz_notes("adult")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_ed_elem
        if extern_skills.skills_ed_elem and host_skills.skills_ed_elem:
            self.skills.set_skills_ed_elem(True)
            self.skills.set_skills_biz_notes("elem")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        #skills_ed_curriculum
        if extern_skills.skills_ed_curriculum and host_skills.skills_ed_curriculum:
            self.skills.set_skills_ed_curriculum(True)
            self.skills.set_skills_biz_notes("curriculum")
            self.biz_skills_match_score = self.biz_skills_match_score + 1

        # skills_other

        # Work Style Matches

        # style_driven
        if extern_skills.style_driven and host_skills.style_driven:
            self.skills.set_style_driven(True)
            self.skills.set_style_notes("driven")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_collab
        if extern_skills.style_collab and host_skills.style_collab:
            self.skills.set_style_collab(True)
            self.skills.set_style_notes("collab")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_creative
        if extern_skills.style_creative and host_skills.style_creative:
            self.skills.set_style_creative(True)
            self.skills.set_style_notes("creative")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_investigate
        if extern_skills.style_investigate and host_skills.style_investigate:
            self.skills.set_style_investigate(True)
            self.skills.set_style_notes("investigate")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_task
        if extern_skills.style_task and host_skills.style_task:
            self.skills.set_style_task(True)
            self.skills.set_style_notes("task")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_ambiguity
        if extern_skills.style_ambiguity and host_skills.style_ambiguity:
            self.skills.set_style_ambiguity(True)
            self.skills.set_style_notes("ambiguity")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_organized
        if extern_skills.style_organized and host_skills.style_organized:
            self.skills.set_style_organized(True)
            self.skills.set_style_notes("organized")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_direction
        if extern_skills.style_direction and host_skills.style_direction:
            self.skills.set_style_direction(True)
            self.skills.set_style_notes("direction")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_networker
        if extern_skills.style_networker and host_skills.style_networker:
            self.skills.set_style_networker(True)
            self.skills.set_style_notes("networker")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_structured
        if extern_skills.style_structured and host_skills.style_structured:
            self.skills.set_style_structured(True)
            self.skills.set_style_notes("structured")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_teamlead
        if extern_skills.style_teamlead and host_skills.style_teamlead:
            self.skills.set_style_teamlead(True)
            self.skills.set_style_notes("teamlead")
            self.work_style_match_score = self.work_style_match_score + 1

        # style_other

        # Set Teaching Needs Match
        # If Host is requesting elementary or secondary instruction in col AH and extern col R is a match set to "Y"
        # If Host is requesting elementary or secondary instruction in col AH and extern col R is NOT a match set to "N"
        # If host does not need elementary or secondary instruction set to "N/A"

        host_business_education_skills = self.host_obj.get_business_education_skills()
        host_requires_education = None
        if "Secondary-Level Instructional Experience" in host_business_education_skills:
            host_requires_education = True
        elif "Elementary-Level Instructional experience" in host_business_education_skills:
            host_requires_education = True
        else:
            host_requires_education = False

        extern_open_to_teach = self.extern_obj.get_open_to_teaching()
        extern_has_education = None
        if "Yes" in extern_open_to_teach:
            extern_has_education = True
        else:
            extern_has_education = False

        if host_requires_education and extern_has_education:
            self.set_teaching_needs_match("Y")
        if host_requires_education and not extern_has_education:
            self.set_teaching_needs_match("N")
        if not host_requires_education:
            self.set_teaching_needs_match("N/A")

        # set curriculum_design_match
        host_business_education_skills = self.host_obj.get_business_education_skills()
        host_requires_curriculum_design = None
        if "Curriculum Design" in host_business_education_skills:
            host_requires_curriculum_design = True
        else:
            host_requires_curriculum_design = False

        extern_open_to_curriculum = self.extern_obj.get_open_to_curriculum_design()
        if "Yes" in extern_open_to_curriculum:
            extern_has_curriculum = True
        else:
            extern_has_curriculum  = False

        if host_requires_curriculum_design and extern_has_curriculum:
            self.set_curriculum_design_match("Y")
        elif host_requires_curriculum_design and not extern_has_curriculum:
            self.set_curriculum_design_match("N")
        else:
            self.set_curriculum_design_match("N/A")

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
                self.distance = "n/a"
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

    def get_host_id(self):
        return self.host_id

    def get_host_city(self):
        return self.host_city

    def get_extern_id(self):
        return self.extern_id

    def get_extern_city(self):
        return self.extern_city

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

    def get_host_no_skills_needed(self):
        return self.host_no_skills_needed

    def get_extern_remote_only(self):
        return self.extern_remote_only

    def get_biz_skills_match_score(self):
        return self.biz_skills_match_score

    def get_biz_skills_match_notes(self):
        return self.skills.get_skills_biz_notes()

    def get_work_style_match_score(self):
        return self.work_style_match_score

    def get_work_style_match_notes(self):
        return self.skills.get_style_notes()

    def set_teaching_needs_match(self, teaching_needs_match):
        self.teaching_needs_match = teaching_needs_match

    def get_teaching_needs_match(self):
        return self.teaching_needs_match

    def set_curriculum_design_match(self, curriculum_design_match):
        self.curriculum_design_match = curriculum_design_match

    def get_curriculum_design_match(self):
        return self.curriculum_design_match


