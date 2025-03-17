
import pickle

#from OpenGL.wrapper import none_or_pass

import Skills as Skills
from prettytable import PrettyTable as PrettyTable
import logging
import data_config

log = logging.getLogger(__name__)
filelog = logging.getLogger("FileLogger")
# set level to 10 to enable debugging.


# Load in the dictionary that holds in the distances between zipcodes.
distance_miles_pickle = data_config.distance_miles_pickle
#with open('/home/jamie/Source/Python/skillMatch/data/Input/distance_miles.pickle', 'rb') as distance:
with open(distance_miles_pickle, 'rb') as distance:
    distance_dict = pickle.load(distance)


class Match:

    def __init__(self, extern_obj, host_obj):
        log.debug("\nCreating a match object")
        self.extern_obj = None
        self.host_obj = None
        self.key = None
        self.distance = None
        self.distance_notes = None
        self.arson = None # used to store 1st Filter - location result.
        self.basin = None # used to store 2nd Filter - location Host AN / Extern U
        self.career = None # used to store teaching openness filter result.
        self.defend = None # used to store business skills match
        self.endorse = None # used to store STEM skills match.
        self.fortify = None # used to store STEM intrest match.
        self.gavel = None # Used to store Hours Match

        self.extern_obj = extern_obj
        self.host_obj = host_obj

        self.set_key()

        log.debug(f"match key : {self.key}")
        self.host_id = f"{host_obj.get_id()}"
        self.host_name = f"{self.host_obj.get_organization_name()}"
        self.host_city = f"{self.host_obj.get_location_of_organization()}"
        self.host_no_skills_needed = f"{self.host_obj.get_no_skills_needed()}"
        self.host_work_done_remotely = f"{self.host_obj.get_work_done_remotely()}"

        self.extern_id = f"{extern_obj.get_id()}"
        self.extern_name = f"{self.extern_obj.get_last_name()}, {self.extern_obj.get_first_name()}"
        self.extern_city = f"{self.extern_obj.get_city_you_live_in()}"
        self.extern_remote_only = f"{self.extern_obj.get_remote_only()}"
        self.extern_open_to = f"{self.extern_obj.get_open_to()}"


        # Teaching/Curriculum Needs Match Data #
        self.teaching_needs_match = None
        self.curriculum_design_match = None

        # Perform Matching on Skills
        self.stem_experience_match_score = 0
        self.biz_skills_match_score = 0
        self.work_style_match_score = 0
        self.total_score = 0
        self.distance_notes = ""
        self.remote_match = None
        self.skills = Skills.Skills()
        self.match_score = 0

        extern_skills = self.extern_obj.skills
        host_skills = self.host_obj.skills

        self.perform_matching_for_stemexp(extern_skills, host_skills)
        self.perform_matching_for_biz_ed(extern_skills, host_skills)
        self.perform_matching_for_style(extern_skills, host_skills)
        self.perform_matching_for_teaching_needs()
        self.perform_matching_for_curriculum_needs()
        self.calculate_distance()
        self.calculate_remote_match()
        self.set_total_score()

        # Added Matching Logic 2025
        self.set_arson()
        self.set_basin()
        self.set_career()
        self.set_defend()
        self.set_endorse()
        self.set_fortify()
        self.set_gavel()

        if log.level <= logging.DEBUG:
            self.print_skill_chart()

        log.debug("Placeholder")

    def __str__(self):
        out_str = ""
        out_str = out_str + "\n"
        out_str = out_str + f"key : {self.key} : match score : {self.match_score}\n"
        out_str = out_str + f"curriculum design match : {self.curriculum_design_match}\n"
        out_str = out_str + "-- host object skills --\n"
        out_str = out_str + f"{self.host_obj.skills}\n"
        out_str = out_str + "-- extern object skills --\n"
        out_str = out_str + f"{self.extern_obj.skills}\n"
        # out_str = out_str + self.print_skill_chart()
        out_str = out_str + "\n"
        return out_str

    def perform_matching_for_stemexp(self, extern_skills, host_skills):
        # calculate matching for stemexp
        # stemexp_na - don't match on this.

        # stemexp_lifesci
        if extern_skills.stemexp_lifesci and host_skills.stemexp_lifesci:
            self.skills.set_stemexp_lifesci(True)
            self.skills.set_stemexp_notes("lifesci")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_lifesci")
        # stemexp_chem
        if extern_skills.stemexp_chem and host_skills.stemexp_chem:
            self.skills.set_stemexp_chem(True)
            self.skills.set_stemexp_notes("chem")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_chem")
        # stemexp_phys
        if extern_skills.stemexp_phys and host_skills.stemexp_phys:
            self.skills.set_stemexp_phys(True)
            self.skills.set_stemexp_notes("phys")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_phys")
        # stemexp_math
        if extern_skills.stemexp_math and host_skills.stemexp_math:
            self.skills.set_stemexp_math(True)
            self.skills.set_stemexp_notes("math")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_math")
        # stemexp_compsci
        if extern_skills.stemexp_compsci and host_skills.stemexp_compsci:
            self.skills.set_stemexp_compsci(True)
            self.skills.set_stemexp_notes("compsci")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_compsci")
        # stemexp_it
        if extern_skills.stemexp_it and host_skills.stemexp_it:
            self.skills.set_stemexp_it(True)
            self.skills.set_stemexp_notes("it")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_it")
        # stemexp_ag
        if extern_skills.stemexp_ag and host_skills.stemexp_ag:
            self.skills.set_stemexp_ag(True)
            self.skills.set_stemexp_notes("ag")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_ag")
        # stemexp_eng
        if extern_skills.stemexp_eng and host_skills.stemexp_eng:
            self.skills.set_stemexp_eng(True)
            self.skills.set_stemexp_notes("eng")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_eng")
        # stemexp_health
        if extern_skills.stemexp_health and host_skills.stemexp_health:
            self.skills.set_stemexp_health(True)
            self.skills.set_stemexp_notes("health")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_health")
        # stemexp_trade
        if extern_skills.stemexp_trade and host_skills.stemexp_trade:
            self.skills.set_stemexp_trade(True)
            self.skills.set_stemexp_notes("trade")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_trade")
        # stemexp_env
        if extern_skills.stemexp_env and host_skills.stemexp_env:
            self.skills.set_stemexp_env(True)
            self.skills.set_stemexp_notes("env")
            self.stem_experience_match_score = self.stem_experience_match_score + 1
            log.debug(f"match found on stemexp_env")

        # stemexp_other - don't match on this.

    def perform_matching_for_biz_ed(self, extern_skills, host_skills):
        # Business Skills Match
        # skills_biz_na
        if extern_skills.skills_biz_na and host_skills.skills_biz_na:
            self.skills.set_skills_biz_na(True)
            self.skills.set_skills_biz_notes("na")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_biz_na")

        # skills_biz_sheets
        if extern_skills.skills_biz_sheets and host_skills.skills_biz_sheets:
            self.skills.set_skills_biz_sheets(True)
            self.skills.set_skills_biz_notes("sheets")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_biz_sheets")

        # skills_biz_word
        if extern_skills.skills_biz_word and host_skills.skills_biz_word:
            self.skills.set_skills_biz_word(True)
            self.skills.set_skills_biz_notes("word")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_biz_word")

        # skills_biz_slides
        if extern_skills.skills_biz_slides and host_skills.skills_biz_slides:
            self.skills.set_skills_biz_slides(True)
            self.skills.set_skills_biz_notes("slides")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_biz_slides")

        # skills_biz_pm
        if extern_skills.skills_biz_pm and host_skills.skills_biz_pm:
            self.skills.set_skills_biz_pm(True)
            self.skills.set_skills_biz_notes("pm")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_biz_pm")

        # skills_biz_speaking
        if extern_skills.skills_biz_speaking and host_skills.skills_biz_speaking:
            self.skills.set_skills_biz_speaking(True)
            self.skills.set_skills_biz_notes("speaking")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_biz_speaking")

        # skills_biz_email
        if extern_skills.skills_biz_email and host_skills.skills_biz_email:
            self.skills.set_skills_biz_email(True)
            self.skills.set_skills_biz_notes("email")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_biz_email")

        # skills_ed_secondary
        if extern_skills.skills_ed_secondary and host_skills.skills_ed_secondary:
            self.skills.set_skills_ed_secondary(True)
            self.skills.set_skills_biz_notes("secondary")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_ed_secondary")

        # skills_ed_adult
        if extern_skills.skills_ed_adult and host_skills.skills_ed_adult:
            self.skills.set_skills_ed_adult(True)
            self.skills.set_skills_biz_notes("adult")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_ed_adult")

        # skills_ed_elem
        if extern_skills.skills_ed_elem and host_skills.skills_ed_elem:
            self.skills.set_skills_ed_elem(True)
            self.skills.set_skills_biz_notes("elem")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_ed_elem")

        # skills_ed_curriculum
        if extern_skills.skills_ed_curriculum and host_skills.skills_ed_curriculum:
            self.skills.set_skills_ed_curriculum(True)
            self.skills.set_skills_biz_notes("curriculum")
            self.biz_skills_match_score = self.biz_skills_match_score + 1
            log.debug(f"match found on skills_ed_curriculum")

        # skills_other

    def perform_matching_for_style(self, extern_skills, host_skills):
        # Work Style Matches

        # style_driven
        if extern_skills.style_driven and host_skills.style_driven:
            self.skills.set_style_driven(True)
            self.skills.set_style_notes("driven")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_driven")

        # style_collab
        if extern_skills.style_collab and host_skills.style_collab:
            self.skills.set_style_collab(True)
            self.skills.set_style_notes("collab")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_collab")

        # style_creative
        if extern_skills.style_creative and host_skills.style_creative:
            self.skills.set_style_creative(True)
            self.skills.set_style_notes("creative")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_creative")

        # style_investigate
        if extern_skills.style_investigate and host_skills.style_investigate:
            self.skills.set_style_investigate(True)
            self.skills.set_style_notes("investigate")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_investigate")

        # style_task
        if extern_skills.style_task and host_skills.style_task:
            self.skills.set_style_task(True)
            self.skills.set_style_notes("task")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_task")

        # style_ambiguity
        if extern_skills.style_ambiguity and host_skills.style_ambiguity:
            self.skills.set_style_ambiguity(True)
            self.skills.set_style_notes("ambiguity")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_ambiguity")

        # style_organized
        if extern_skills.style_organized and host_skills.style_organized:
            self.skills.set_style_organized(True)
            self.skills.set_style_notes("organized")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_organized")

        # style_direction
        if extern_skills.style_direction and host_skills.style_direction:
            self.skills.set_style_direction(True)
            self.skills.set_style_notes("direction")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_direction")

        # style_networker
        if extern_skills.style_networker and host_skills.style_networker:
            self.skills.set_style_networker(True)
            self.skills.set_style_notes("networker")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_networker")

        # style_structured
        if extern_skills.style_structured and host_skills.style_structured:
            self.skills.set_style_structured(True)
            self.skills.set_style_notes("structured")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_structured")

        # style_teamlead
        if extern_skills.style_teamlead and host_skills.style_teamlead:
            self.skills.set_style_teamlead(True)
            self.skills.set_style_notes("teamlead")
            self.work_style_match_score = self.work_style_match_score + 1
            log.debug(f"match found on skills_style_teamlead")

        # style_other

    def perform_matching_for_teaching_needs(self):
        # Set Teaching Needs Match
        # If Host is requesting elementary or secondary instruction in col AH and extern col R is a match set to "Y"
        # If Host is requesting elementary or secondary instruction in col AH and extern col R is NOT a match set to "N"
        # If host does not need elementary or secondary instruction set to "N/A"

        host_business_education_skills = self.host_obj.get_business_education_skills()
        if "Secondary-Level Instructional Experience" in host_business_education_skills:
            host_requires_education = True
        elif "Elementary-Level Instructional experience" in host_business_education_skills:
            host_requires_education = True
        else:
            host_requires_education = False

        extern_open_to_teach = self.extern_obj.get_open_to_teaching()
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

    def perform_matching_for_curriculum_needs(self):
        # set curriculum_design_match
        host_business_education_skills = self.host_obj.get_business_education_skills()
        if "Curriculum Design" in host_business_education_skills:
            host_requires_curriculum_design = True
        else:
            host_requires_curriculum_design = False

        extern_open_to_curriculum = self.extern_obj.get_open_to_curriculum_design()
        if "Yes" in extern_open_to_curriculum:
            extern_has_curriculum = True
        else:
            extern_has_curriculum = False

        if host_requires_curriculum_design and extern_has_curriculum:
            self.set_curriculum_design_match("Y")
        elif host_requires_curriculum_design and not extern_has_curriculum:
            self.set_curriculum_design_match("N")
        else:
            self.set_curriculum_design_match("N/A")

    def calculate_distance(self):
        log.debug("Calculating Distance")
        # Calculate Distance (self.distance)
        # we find distance by using a dictionary which stores the distances in miles between zipcodes.
        extern_zip = self.extern_obj.get_zip()
        log.debug(f"Extern Zip : {extern_zip}")
        host_zip = self.host_obj.get_zip()
        log.debug(f"Host Zip : {host_zip}")
        distance_from_dictionary = distance_dict.get((extern_zip, host_zip))
        if distance_from_dictionary is not None:
            self.distance = distance_from_dictionary
            log.debug(f"Calculated distance : {distance_from_dictionary}")
            self.set_distance_notes(f"{extern_zip}<-->{host_zip}")

        else:
            # if you are here the dictionary lookup has failed.
            log.debug("Dictionary lookup has failed.")
            if host_zip == "remote":
                self.distance = "n/a"
                self.set_distance_notes("host zip is 'remote'")
            else:
                self.distance = 9999
                log.debug(f"ext:{self.extern_obj.get_id()} zip: {extern_zip} host:{self.host_obj.get_id()} zip:{host_zip}")

        return None

    def calculate_remote_match(self):
        # set remote match
        # A remote match is Extern V (what work locations are you open to) and Host AN (can this work be done remotely)
        extern_remote_match = self.extern_obj.get_what_work_locations()
        host_remote_match = self.host_obj.get_work_done_remotely()

        if ("Remote" in extern_remote_match) and ("Yes" in host_remote_match):
            self.set_remote_match(True)
        else:
            self.set_remote_match(False)

    def set_total_score(self):
        log.debug("Setting total score...")
        stemexp_score = self.get_stem_experience_match_score()
        log.debug(f"stemexp score:{stemexp_score}")
        biz = self.get_biz_skills_match_score()
        log.debug(f"biz score:{biz}")
        style = self.get_work_style_match_score()
        log.debug(f"style score:{style}")
        out_score = stemexp_score + biz + style
        log.debug(f"total score:{out_score}")

        self.total_score = out_score
        return out_score

    def print_skill_chart(self):
        out_table = PrettyTable()
        out_table.field_names = ["Skill", "Extern", "Host"]

        skill = "stemexp_lifesci"
        extern_value = self.extern_obj.skills.get_stemexp_lifesci()
        host_value = self.host_obj.skills.get_stemexp_lifesci()
        out_table.add_row([skill, extern_value, host_value])

        skill = "stemexp_chem"
        extern_value = self.extern_obj.skills.get_stemexp_chem()
        host_value = self.host_obj.skills.get_stemexp_chem()
        out_table.add_row([skill, extern_value, host_value])

        skill = "stemexp_phys"
        extern_value = self.extern_obj.skills.get_stemexp_phys()
        host_value = self.host_obj.skills.get_stemexp_phys()
        out_table.add_row([skill, extern_value, host_value])

        # stemexp_math
        skill = "stemexp_math"
        extern_value = self.extern_obj.skills.get_stemexp_math()
        host_value = self.host_obj.skills.get_stemexp_math()
        out_table.add_row([skill, extern_value, host_value])

        # stemexp_compsci
        skill = "stemexp_compsci"
        extern_value = self.extern_obj.skills.get_stemexp_compsci()
        host_value = self.host_obj.skills.get_stemexp_compsci()
        out_table.add_row([skill, extern_value, host_value])

        # stemexp_it
        skill = "stemexp_it"
        extern_value = self.extern_obj.skills.get_stemexp_it()
        host_value = self.host_obj.skills.get_stemexp_it()
        out_table.add_row([skill, extern_value, host_value])

        # stemexp_ag
        skill = "stemexp_ag"
        extern_value = self.extern_obj.skills.get_stemexp_ag()
        host_value = self.host_obj.skills.get_stemexp_ag()
        out_table.add_row([skill, extern_value, host_value])

        # stemexp_eng
        skill = "stemexp_eng"
        extern_value = self.extern_obj.skills.get_stemexp_eng()
        host_value = self.host_obj.skills.get_stemexp_eng()
        out_table.add_row([skill, extern_value, host_value])

        # stemexp_health
        # stemexp_trade
        # stemexp_env
        # stemexp_other

        out_table.add_row(["4", "5", "6"])

        print(out_table)
        return None

    def set_key(self):
        #self.key = (self.extern_obj.get_id(), self.host_obj.get_id())
        self.key = f"E{self.extern_obj.get_id()}-H{self.host_obj.get_id()}"

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

    def get_extern_open_to(self):
        return self.extern_open_to

    def get_host_work_done_remotely(self):
        return self.host_work_done_remotely

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

    def get_how_many_externs(self):
        return self.host_obj.get_how_many_externs()

    def get_min_externs(self):
        return self.host_obj.get_min_externs()

    def get_max_externs(self):
        return self.host_obj.get_max_externs()

    def get_total_score(self):
        return self.total_score

    def get_arson(self):
        return self.arson

    def set_arson(self):
        """
        :Input: None - uses embedded peroperties.
        :return: None - side effect is to set the first filter location - distance based on zip code.
        """
        filelog.debug("In Arson")
        # todo: sanity check against bad distances.
        if self.distance < 30:
            self.arson = "GOOD"
        elif self.distance >= 30 and self.distance < 50:
            self.arson = "IFFY"
        else:
            self.arson = "POOR"

        filelog.debug(f"ARSON value is {self.arson} because distance is {self.distance}.")
        filelog.debug(f"\n")

        return self.arson

    def get_basin(self):
        return self.basin

    def set_basin(self):

        # set default value for basin
        self.basin = "POOR"

        # set physical distance values
        physical_distance_good = False
        physical_distance_iffy = False
        physical_distance_poor = False
        physical_distance_code = None

        physical_distance = self.arson
        if physical_distance == "GOOD":
            physical_distance_good = True
            physical_distance_code = "G"
        elif physical_distance == "IFFY":
            physical_distance_iffy = True
            physical_distance_code = "I"
        elif physical_distance == "POOR":
            physical_distance_poor = True
            physical_distance_code = "P"

        assert (physical_distance_good or physical_distance_iffy or physical_distance_poor)
        assert (physical_distance_code == "G" or physical_distance_code == "I" or physical_distance_code == "P")


        # set host_work_location values
        host_work_location = self.host_obj.work_done_remotely
        host_work_location_code = None

        if host_work_location == "Hybrid - sometimes in office":
            host_work_location_hybrid = True
            host_work_location_code = "H"
        if host_work_location == "100% in office":
            host_work_location_office = True
            host_work_location_code = "O"
        if host_work_location == "Externâ\x80\x99s choice":
            host_work_location_externchoice = True
            host_work_location_code = "E"
        if host_work_location == "100% remote":
            host_work_location_remote = True
            host_work_location_code = "R"

        assert (host_work_location_code == "O" or host_work_location_code == "H" or host_work_location_code == "R" or host_work_location_code == "E")

        # set extern open to values and codes
        extern_open_to_code = ""
        extern_open_to_remote = False
        extern_open_to_inperson = False
        extern_open_to_hybrid = False

        extern_open_to = self.extern_obj.what_work_locations
        if "Remote" in extern_open_to:
            extern_open_to_remote = True
            extern_open_to_code = extern_open_to_code + "M"
        if "In-Person" in extern_open_to:
            extern_open_to_inperson = True
            extern_open_to_code = extern_open_to_code + "N"
        if "Hybrid" in extern_open_to:
            extern_open_to_hybrid = True
            extern_open_to_code = extern_open_to_code + "Y"

        # check that at least once choice is made
        assert (extern_open_to_remote or extern_open_to_inperson or extern_open_to_hybrid)

        assert extern_open_to_code in ["MNY","MN","NY","MY","M","N","Y"]

        option_code = None
        option_code = physical_distance_code + host_work_location_code + extern_open_to_code

        location_choices_output = {}

        # Good and Office
        location_choices_output["GOMNY"] = "GOOD (close)"
        location_choices_output["GOMN"] = "GOOD (close)"
        location_choices_output["GONY"] = "GOOD (close)"
        location_choices_output["GOMY"] = "IFFY"
        location_choices_output["GOM"] = "POOR"
        location_choices_output["GON"] = "GOOD (close)"
        location_choices_output["GOY"] = "IFFY"

        # Good and Hybrid
        location_choices_output["GHMNY"] = "GOOD (close)"
        location_choices_output["GHMN"] = "GOOD (close)"
        location_choices_output["GHNY"] = "GOOD (close)"
        location_choices_output["GHMY"] = "GOOD (close)"
        location_choices_output["GHM"] = "POOR"
        location_choices_output["GHN"] = "GOOD (close)"
        location_choices_output["GHY"] = "GOOD (close)"

        # GOOD and Extern's Choice
        location_choices_output["GEMNY"] = "GOOD (close)"
        location_choices_output["GEMN"] = "GOOD (close)"
        location_choices_output["GENY"] = "GOOD (close)"
        location_choices_output["GEMY"] = "GOOD (close)"
        location_choices_output["GEM"] = "GOOD (remote)"
        location_choices_output["GEN"] = "GOOD (close)"
        location_choices_output["GEY"] = "GOOD (close)"

        # Good and Remote
        location_choices_output["GRMNY"] = "GOOD (remote)"
        location_choices_output["GRMN"] = "GOOD (remote)"
        location_choices_output["GRNY"] = "POOR"
        location_choices_output["GRMY"] = "GOOD (remote)"
        location_choices_output["GRM"] = "GOOD (remote)"
        location_choices_output["GRN"] = "POOR"
        location_choices_output["GRY"] = "POOR"

        # Iffy and Office
        location_choices_output["IOMNY"] = "IFFY"
        location_choices_output["IOMN"] = "IFFY"
        location_choices_output["IONY"] = "IFFY"
        location_choices_output["IOMY"] = "IFFY"
        location_choices_output["IOM"] = "POOR"
        location_choices_output["ION"] = "IFFY"
        location_choices_output["IOY"] = "IFFY"

        # IFFY and Hybrid
        location_choices_output["IHMNY"] = "IFFY"
        location_choices_output["IHMN"] = "IFFY"
        location_choices_output["IHNY"] = "IFFY"
        location_choices_output["IHMY"] = "IFFY"
        location_choices_output["IHM"] = "POOR"
        location_choices_output["IHN"] = "IFFY"
        location_choices_output["IHY"] = "IFFY"

        # IFFY and Remote
        location_choices_output["IRMNY"] = "GOOD (remote)"
        location_choices_output["IRMN"] = "GOOD (remote)"
        location_choices_output["IRNY"] = "POOR"
        location_choices_output["IRMY"] = "GOOD (remote)"
        location_choices_output["IRM"] = "GOOD (remote)"
        location_choices_output["IRN"] = "POOR"
        location_choices_output["IRY"] = "POOR"

        # IFFY and Extern's choice
        location_choices_output["IEMNY"] = "GOOD (remote)"
        location_choices_output["IEMN"] = "GOOD (remote)"
        location_choices_output["IENY"] = "IFFY"
        location_choices_output["IEMY"] = "GOOD (remote)"
        location_choices_output["IEM"] = "GOOD (remote)"
        location_choices_output["IEN"] = "IFFY"
        location_choices_output["IEY"] = "IFFY"

        # Poor and Office
        location_choices_output["POMNY"] = "POOR"
        location_choices_output["POMN"] = "POOR"
        location_choices_output["PONY"] = "POOR"
        location_choices_output["POMY"] = "POOR"
        location_choices_output["POM"] = "POOR"
        location_choices_output["PON"] = "POOR"
        location_choices_output["POY"] = "POOR"

        # Poor and Hybrid
        location_choices_output["PHMNY"] = "POOR"
        location_choices_output["PHMN"] = "POOR"
        location_choices_output["PHNY"] = "POOR"
        location_choices_output["PHMY"] = "POOR"
        location_choices_output["PHM"] = "POOR"
        location_choices_output["PHN"] = "POOR"
        location_choices_output["PHY"] = "POOR"

        # poor and office
        location_choices_output["POMNY"] = "POOR"

        # poor and remote
        location_choices_output["PRMNY"] = "GOOD (remote)"
        location_choices_output["PRMN"] = "GOOD (remote)"
        location_choices_output["PRNY"] = "POOR"
        location_choices_output["PRMY"] = "GOOD (remote)"
        location_choices_output["PRM"] = "GOOD (remote)"
        location_choices_output["PRN"] = "POOR"
        location_choices_output["PRY"] = "POOR"

        # poor and extern's choice
        location_choices_output["PEMNY"] = "GOOD (remote)"
        location_choices_output["PEMN"] = "GOOD (remote)"
        location_choices_output["PENY"] = "POOR"
        location_choices_output["PEMY"] = "GOOD (remote)"
        location_choices_output["PEM"] = "GOOD (remote)"
        location_choices_output["PEN"] = "POOR"
        location_choices_output["PEY"] = "POOR"


        self.basin = location_choices_output[option_code]

        filelog.info(f"basin : {self.basin}\n")

    def get_carrear(self):
        return self.career

    def set_career(self):
        filelog.debug(f"In Career {self.get_key()}")

        host_column = self.host_obj.education_student_skills
        extern_elementary = self.extern_obj.get_elementary_level_instruction() #Q
        extern_secondary = self.extern_obj.get_open_to_secondary_teaching()
        extern_adult = self.extern_obj.get_open_to_adult_teaching()
        extern_camp = self.extern_obj.get_Open_to_camp_counselor()
        extern_curriculum = self.extern_obj.get_open_to_curriculum_design()

        #filelog.debug(f"host_column : {host_column}")

        #filelog.debug(f"extern_elementary : {extern_elementary}")
        #filelog.debug(f"extern_secondary : {extern_secondary}")
        #filelog.debug(f"extern_adult : {extern_adult}")
        #filelog.debug(f"extern_camp : {extern_camp}")
        #filelog.debug(f"extern_curriculum : {extern_curriculum}")

        #deafult value
        self.career = "FINE"

        if "Elementary" in host_column and extern_elementary == "No":
            self.career = "POOR"
            #filelog.debug("Poor for Elementary")

        if "Secondary" in host_column and extern_secondary == "No":
            self.career = "POOR"
            #filelog.debug("Poor for Secondary")


        if "counselor" in host_column and extern_camp == "No":
            self.career = "POOR"
            #filelog.debug("Poor for Conselor")

        if "Curriculum" in host_column and extern_curriculum == "No":
            self.career = "POOR"
            #filelog.debug("Poor for Curriculum")

        if "adult" in host_column and extern_adult == "No":
            self.career = "POOR"
            #filelog.debug("Poor for Adult")

        #filelog.debug(f"{self.get_carrear()}\n")

    def get_defend(self):
        return self.defend

    def set_defend(self):
        filelog.debug(f"Defend {self.get_key()}")
        host_column = self.host_obj.get_business_education_skills()
        extern_colum = self.extern_obj.get_business_software_and_skills()
        host_column_lst = host_column.split(";")
        extern_column_lst = extern_colum.split(";")

        #host_column_lst.remove("")
        extern_column_lst.remove("")

        common = set(host_column_lst) & set(extern_column_lst)
        number_common = len(common)

        filelog.debug(f"host column : {host_column_lst}")
        filelog.debug(f"extern column: {extern_column_lst}")
        filelog.debug(f"common: {common}")
        filelog.debug(f"number in common: {number_common}")

        if number_common <= 1:
            self.defend = "IFFY"

        if (number_common >= 2) and (number_common <= 4):
            self.defend = "GOOD"

        if (number_common >= 5) and (number_common <= 7):
            self.defend = "STRONG"

        if "No specific skills needed" in host_column:
            self.defend = "FINE"

        filelog.debug(f"{self.get_defend()}\n")

    def get_endorse(self):
        return self.endorse

    def set_endorse(self):
        filelog.debug(f"Endorse {self.get_key()}")

        host_ai = self.host_obj.get_looking_for_experience()
        extern_x = self.extern_obj.get_stem_domains()

        host_ai_lst = host_ai.split(";")
        extern_x_lst_raw = extern_x.split(";")
        extern_x_lst = []
        for n in extern_x_lst_raw:
            extern_x_lst.append(n.strip())

        #host_ai_lst.remove("")
        extern_x_lst.remove("")

        common = set(host_ai_lst) & set(extern_x_lst)
        number_common = len(common)

        filelog.debug(f"host_ai : {host_ai}")
        filelog.debug(f"extern_x : {extern_x}")
        filelog.debug(f"common : {common}")
        filelog.debug(f"number common : {number_common}")

        self.endorse = "FINE" # Default Value
        if number_common == 1:
            self.endorse = "GOOD"

        if number_common > 1:
            self.endorse = "STRONG"

        filelog.debug(f"endorse : {self.get_endorse()}\n")

    def get_fortify(self):
        return self.fortify

    def set_fortify(self):
        #filelog.debug(f"Fortify {self.get_key()}")
        log.debug(f"Fortify {self.get_key()}")

        self.fortify = "FINE"

        host_ai = self.host_obj.get_looking_for_experience()
        extern_t = self.extern_obj.get_particular_stem_fields()

        host_ai_lst = host_ai.split(";")
        extern_t_lst = extern_t.split(";")

        #host_ai_lst.remove("")
        if "" in extern_t_lst:
            extern_t_lst.remove("")

        common = set(host_ai_lst) & set(extern_t_lst)
        number_common = len(common)

        filelog.debug(f"host_ai : {host_ai}")
        filelog.debug(f"extern_t : {extern_t}")
        filelog.debug(f"common : {common}")
        filelog.debug(f"number common : {number_common}")

        log.debug(f"host_ai : {host_ai}")
        log.debug(f"extern_t : {extern_t}")
        log.debug(f"common : {common}")
        log.debug(f"number common : {number_common}")

        if number_common == 1:
            self.fortify = "GOOD"

        if number_common > 1:
            self.fortify = "STRONG"

        filelog.debug(f"fortify : {self.get_fortify()}\n")
        log.debug(f"fortify : {self.get_fortify()}\n")

    def get_gavel(self):
        return self.gavel

    def set_gavel(self):
        filelog.debug(f"Gavel : {self.get_key()}")

        host_hours_lst = []
        extern_hours_lst = []

        host_ax = self.host_obj.get_one_hundred_hours()
        # ax is No for 200 only
        # ax is Yes for 100 or 200.
        extern_av = self.extern_obj.get_externship_durations()
        extern_av_lst = extern_av.split(";")

        for n in extern_av_lst:
            if "100" in n:
                extern_hours_lst.append("100")
            if "200" in n:
                extern_hours_lst.append("200")

        if host_ax == "Yes":
            host_hours_lst.append("100")
            host_hours_lst.append("200")
        else:
            host_hours_lst.append("200")

        common = set(host_hours_lst) & set(extern_hours_lst)
        number_common = len(common)

        filelog.debug(f"host ax : {host_ax}")
        filelog.debug(f"extern av : {extern_av}")

        filelog.debug(f"host_hours_lst : {host_hours_lst}")
        filelog.debug(f"extern_hours_lst : {extern_hours_lst}")

        filelog.debug(f"common : {common}")
        filelog.debug(f"{number_common}")

        if number_common >= 1:
            self.gavel = "GOOD"
        else:
            self.gavel = "POOR"

        filelog.debug(f"{self.get_gavel()}")











