import sys

from AttributeSet import AttributeSet
import Skills as Skills

import logging
log = logging.getLogger(__name__)


city_zip = {}
city_zip["Ada County"] = 83706
city_zip["Blackfoot "] = 83221
city_zip["Blackfoot"] = 83221
city_zip["Boise"] = 83706
city_zip["Boise, ID"] = 83706
city_zip["Boise, Idaho"] = 83706
city_zip["Boise County, halfway between Idaho City and Boise"] = 83716
city_zip["Buhl"] = 83316
city_zip["Burley"] = 83318
city_zip["Caldwell"] = 83606
city_zip["Dayton"] = 83232
city_zip["Dietrich "] = 83324
city_zip["Eagle"] = 83616
city_zip["Eagle, Idaho"] = 83616
city_zip["Garden Valley"] = 83622
city_zip["Glenns Ferry"] = 83623
city_zip["Hailey"] = 83333
city_zip["Hazelton, ID"] = 83335
city_zip["Idaho City"] = 83631
city_zip["Idaho Falls"] = 83402
city_zip["Idaho Falls "] = 83402
city_zip["Idaho Falls, Idaho "] = 83402
city_zip["Inkom"] = 83245
city_zip["Kuna, Idaho"] = 83642
city_zip["McCall"] = 83638
city_zip["McCammon"] = 83250
city_zip["Meridian"] = 83646
city_zip["Meridian, Idaho"] = 83646
city_zip["Montpelier"] = 83254
city_zip["Mountain Home"] = 83647
city_zip["Nampa"] = 83651
city_zip["Nampa "] = 83651
city_zip["Nampa, ID"] = 83651
city_zip["Pocatello"] = 83205
city_zip["Pocatello, ID"] = 83205
city_zip["Pocatello, Idaho "] = 83205
city_zip["Pocatello Idaho"] = 83205
city_zip["Potlatch"] = 83855
city_zip["Preston"] = 83263
city_zip["Princeton, Idaho"] = 83857
city_zip["Rathdrum"] = 83858
city_zip["Rexburg"] = 83440
city_zip["Richfield"] = 83349
city_zip["Rigby"] = 83442
city_zip["Ririe"] = 83443
city_zip["Rupert"] = 83350
city_zip["Sandpoint"] = 83864
city_zip["Shelley"] = 83274
city_zip["Spirit Lake, Idaho but I commute to Coeur d'Alene daily. "] = 83869
city_zip["Sugar City Idaho"] = 83448
city_zip["Twin Falls"] = 83301
city_zip["Wilder"] = 83303


class Extern(AttributeSet):
    def __init__(self, row_data_tuple):

        self.ID = None                              ## A
        self.start_time = None
        self.completion_time = None
        self.email = None
        self.name = None
        self.who_are_you = None
        self.first_name = None
        self.last_name = None
        self.primary_email = None
        self.backup_email = None
        self.school_where_you_work = None
        self.district_where_you_work = None
        self.current_roles = None
        self.city_you_live_in = None
        self.why_part_of_program = None
        self.flavor_of_work = None                  ## P
        self.why_most_interesting = None
        self.open_to_teaching = None
        self.open_to_curriculum_design = None
        self.Open_to_camp_counselor = None
        self.particular_stem_fields = None          ## U
        self.what_work_locations = None
        self.open_to_travelling = None
        self.grade_levels = None                    ## X
        self.stem_domains = None                    ## Y
        self.spreadsheet_software = None                ## Z
        self.word_processings_software = None
        self.presentation_software = None
        self.elementary_level_instruction = None
        self.curriculum_design = None
        self.project_management = None
        self.secondary_level_instruction = None
        self.experiences_or_interests = None
        self.linkedin_profile = None
        self.adult_education_training = None
        self.public_speaking = None
        #self.group_presentation = None
        self.email_administrative_software = None
        self.zip = None # This is a synthetic property -- needs conversion from City Live In to a zip.
        self.remote_only = None  # This is a synthetic property -- If extern ONLY indicated “remote” in column V, True

        #append a skills object to hold data for skills matches.
        self.skills = Skills.Skills()
        # set the synthetic remote only property
        self.set_remote_only()


        ID_COL = 0                              # A
        START_TIME_COL = 1                      # B
        COMPLETION_TIME_COL = 2                 # C
        EMAIL_COL = 3                           # D
        NAME_COL = 4                            # E
        WHO_ARE_YOU_COL = 5                     # F
        FIRST_NAME_COL = 6                      # G
        LAST_NAME_COL = 7                       # H
        PRIMARY_EMAIL_COL = 8                   # I
        BACKUP_EMAIL_COL = 9                    # J
        SCHOOL_WHERE_YOU_WORK_COL = 10          # K
        DISTRICT_WHERE_YOU_WORK_COL = 11        # L
        CURRENT_ROLES_COL = 12                  # M
        CITY_YOU_LIVE_IN_COL = 13               # N
        WHY_PART_OF_PROGRAM_COL = 14            # O
        FLAVOR_OF_WORK_COL = 15                 # P
        WHY_MOST_INTERESTING_COL = 16           # Q
        OPEN_TO_TEACHING_COL = 17               # R
        OPEN_TO_CURRICULUM_DESIGN_COL = 18      # S
        OPEN_TO_CAMP_COUNSELOR_COL = 19         # T
        PARTICULAR_STEM_FIELDS_COL = 20         # U
        WHAT_WORK_LOCATIONS_COL = 21            # V
        OPEN_TO_TRAVELLING_COL = 22             # W
        GRADE_LEVELS_COL = 23                   # X
        STEM_DOMAINS_COL = 24                   # Y
        SPREADSHEET_SOFTWARE_COL = 25           # Z
        WORD_PROCESSINGS_SOFTWARE_COL = 26      # AA
        PRESENTATION_SOFTWARE_COL = 27          # AB
        ELEMENTARY_LEVEL_INSTRUCTION_COL = 28   # AC
        CURRICULUM_DESIGN_COL = 29              # AD
        PROJECT_MANAGEMENT_COL = 30             # AE
        SECONDARY_LEVEL_INSTRUCTION_COL = 31    # AF
        EXPERIENCES_OR_INTERESTS_COL = 32       # AG
        RESUME_COL = 33                         # AH - This column is blank and not used in our data set.
        LINKEDIN_PROFILE_COL = 34               # AI
        ADULT_EDUCATION_TRAINING_COL = 35       # AJ
        PUBLIC_SPEAKING_COL = 36                # AK
        GROUP_PRESENTATION_COL = 0
        EMAIL_ADMINISTRATIVE_SOFTWARE_COL = 37  # AL



        self.set_ID(row_data_tuple[ID_COL].value)
        self.set_start_time(row_data_tuple[START_TIME_COL].value)
        self.set_completion_time(row_data_tuple[COMPLETION_TIME_COL].value)
        self.set_email(row_data_tuple[EMAIL_COL].value)
        self.set_name(row_data_tuple[NAME_COL].value)
        self.set_who_are_you(row_data_tuple[WHO_ARE_YOU_COL].value)
        self.set_first_name(row_data_tuple[FIRST_NAME_COL].value)
        self.set_last_name(row_data_tuple[LAST_NAME_COL].value)
        self.set_primary_email(row_data_tuple[PRIMARY_EMAIL_COL].value)
        self.set_backup_email(row_data_tuple[BACKUP_EMAIL_COL].value)
        self.set_school_where_you_work(row_data_tuple[SCHOOL_WHERE_YOU_WORK_COL].value)
        self.set_district_where_you_work(row_data_tuple[DISTRICT_WHERE_YOU_WORK_COL].value)
        self.set_current_roles(row_data_tuple[CURRENT_ROLES_COL].value)
        self.set_city_you_live_in(row_data_tuple[CITY_YOU_LIVE_IN_COL].value)
        self.set_why_part_of_program(row_data_tuple[WHY_PART_OF_PROGRAM_COL].value)
        self.set_flavor_of_work(row_data_tuple[FLAVOR_OF_WORK_COL].value)
        self.set_why_most_interesting(row_data_tuple[WHY_MOST_INTERESTING_COL].value)
        self.set_open_to_teaching(row_data_tuple[OPEN_TO_TEACHING_COL].value)
        self.set_open_to_curriculum_design(row_data_tuple[OPEN_TO_CURRICULUM_DESIGN_COL].value)
        self.set_Open_to_camp_counselor(row_data_tuple[OPEN_TO_CAMP_COUNSELOR_COL].value)
        self.set_particular_stem_fields(row_data_tuple[PARTICULAR_STEM_FIELDS_COL].value)
        self.set_what_work_locations(row_data_tuple[WHAT_WORK_LOCATIONS_COL].value)
        self.set_open_to_travelling(row_data_tuple[OPEN_TO_TRAVELLING_COL].value)
        self.set_grade_levels(row_data_tuple[GRADE_LEVELS_COL].value)
        self.set_stem_domains(row_data_tuple[STEM_DOMAINS_COL].value)
        self.set_spreadsheet_software(row_data_tuple[SPREADSHEET_SOFTWARE_COL].value)
        self.set_word_processings_software(row_data_tuple[WORD_PROCESSINGS_SOFTWARE_COL].value)
        self.set_presentation_software(row_data_tuple[PRESENTATION_SOFTWARE_COL].value)
        self.set_elementary_level_instruction(row_data_tuple[ELEMENTARY_LEVEL_INSTRUCTION_COL].value)
        self.set_curriculum_design(row_data_tuple[CURRICULUM_DESIGN_COL].value)
        self.set_project_management(row_data_tuple[PROJECT_MANAGEMENT_COL].value)
        self.set_secondary_level_instruction(row_data_tuple[SECONDARY_LEVEL_INSTRUCTION_COL].value)
        self.set_experiences_or_interests(row_data_tuple[EXPERIENCES_OR_INTERESTS_COL].value)
        self.set_linkedin_profile(row_data_tuple[LINKEDIN_PROFILE_COL].value)
        self.set_adult_education_training(row_data_tuple[ADULT_EDUCATION_TRAINING_COL].value)
        self.set_public_speaking(row_data_tuple[PUBLIC_SPEAKING_COL].value)
        #self.set_group_presentation(row_data_tuple[GROUP_PRESENTATION_COL].value)
        self.set_email_administrative_software(row_data_tuple[EMAIL_ADMINISTRATIVE_SOFTWARE_COL].value)
        self.set_zip(city_zip[self.city_you_live_in])

        self.set_skills()
        self.set_remote_only()

    def set_ID(self, ID):
        self.ID = ID

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_completion_time(self, completion_time):
        self.completion_time = completion_time

    def set_email(self, set_email):
        self.set_email = set_email

    def set_name(self, name):
        self.name = name

    def set_who_are_you(self, who_are_you):
        self.who_are_you = who_are_you

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_primary_email(self, primary_email):
        self.primary_email = primary_email

    def set_backup_email(self, backup_email):
        self.backup_email = backup_email

    def set_school_where_you_work(self, school_where_you_work):
        self.school_where_you_work = school_where_you_work

    def set_district_where_you_work(self, district_where_you_work):
        self.district_where_you_work = district_where_you_work

    def set_current_roles(self, current_roles):
        self.current_roles = current_roles

    def set_city_you_live_in(self, city_you_live_in):
        self.city_you_live_in = city_you_live_in

    def set_why_part_of_program(self, why_part_of_program):
        self.why_part_of_program = why_part_of_program

    def set_flavor_of_work(self, flavor_of_work):
        self.flavor_of_work = flavor_of_work

    def set_why_most_interesting(self, why_most_interesting):
        self.why_most_interesting = why_most_interesting

    def set_open_to_teaching(self, open_to_teaching):
        self.open_to_teaching = open_to_teaching

    def set_open_to_curriculum_design(self, open_to_curriculum_design):
        self.open_to_curriculum_design = open_to_curriculum_design

    def set_Open_to_camp_counselor(self, Open_to_camp_counselor):
        self.Open_to_camp_counselor = Open_to_camp_counselor

    def set_particular_stem_fields(self, particular_stem_fields):
        self.particular_stem_fields = particular_stem_fields

    def set_what_work_locations(self, what_work_locations):
        self.what_work_locations = what_work_locations

    def set_remote_only(self):
        #log.debug(f"what work locations : {self.what_work_locations}")
        if self.what_work_locations == "Remote;":
            self.remote_only = True
        else:
            self.remote_only = False
        return None

    def get_remote_only(self):
        return self.remote_only

    def set_open_to_travelling(self, open_to_travelling):
        self.open_to_travelling = open_to_travelling

    def set_grade_levels(self, grade_levels):
        self.grade_levels = grade_levels

    def set_stem_domains(self, stem_domains):
        self.stem_domains = stem_domains

    def set_spreadsheet_software(self, spreadsheet_software):
        self.spreadsheet_software = spreadsheet_software

    def set_word_processings_software(self, word_processings_software):
        self.word_processings_software = word_processings_software

    def set_presentation_software(self, presentation_software):
        self.presentation_software = presentation_software

    def set_elementary_level_instruction(self, elementary_level_instruction):
        self.elementary_level_instruction = elementary_level_instruction

    def set_curriculum_design(self, curriculum_design):
        self.curriculum_design = curriculum_design

    def set_project_management(self, project_management):
        self.project_management = project_management

    def set_secondary_level_instruction(self, secondary_level_instruction):
        self.secondary_level_instruction = secondary_level_instruction

    def set_experiences_or_interests(self, experiences_or_interests):
        self.experiences_or_interests = experiences_or_interests

    def set_linkedin_profile(self, linkedin_profile):
        self.linkedin_profile = linkedin_profile

    def set_adult_education_training(self, adult_education_training):
        self.adult_education_training = adult_education_training

    def set_public_speaking(self, public_speaking):
        self.public_speaking = public_speaking

    def set_group_presentation(self, group_presentation):
        self.group_presentation = group_presentation

    def set_email_administrative_software(self, email_administrative_software):
        self.email_administrative_software = email_administrative_software

    def set_skills(self):
        ### STEM Experience Match ###
        extern_list = self.get_stem_domains()
        extern_list = extern_list.upper()

        if "No special interest - anything goes".upper() in extern_list:
            #log.debug("Matched on 'No special Interest'")
            self.skills.set_stemexp_na(True)

        if "Life Science / Biology".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_lifesci.")
            self.skills.set_stemexp_lifesci(True)

        if "Chemistry".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_chem.")
            self.skills.set_stemexp_chem(True)

        if "Physics".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_phys.")
            self.skills.set_stemexp_phys(True)

        if "Math".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_math.")
            self.skills.set_stemexp_math(True)

        if "Computer Science".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_compsci.")
            self.skills.set_stemexp_compsci(True)

        if "Information & communication Technology".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_it.")
            self.skills.set_stemexp_it(True)

        if "Agriculture, Food, Natural Resources".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_ag.")
            self.skills.set_stemexp_ag(True)

        if "Engineering & Technology".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_eng.")
            self.skills.set_stemexp_eng(True)

        if "Health Professions".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_health.")
            self.skills.set_stemexp_health(True)

        if "Trades & Industry".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_trade.")
            self.skills.set_stemexp_trade(True)

        if "Earth & Environmental Science".upper() in extern_list:
            #log.debug("Extern Matched on set_stemexp_env.")
            self.skills.set_stemexp_env(True)

        ### Set Business Skills ###
        #  (Z thru AF; AJ thru AL)

        #skills_biz_na -- no match is perfored on this criteria.
        #skills_biz_sheets (Z)
        if self.get_spreadsheet_software() != "No Experience":
            self.skills.set_skills_biz_sheets(True)
        else:
            self.skills.set_skills_biz_sheets(False)

        #skills_biz_word
        if self.get_word_processings_software() != "No Experience":
            self.skills.set_skills_biz_word(True)
        else:
            self.skills.set_skills_biz_word(False)

        #skills_biz_slides
        if self.get_presentation_software() != "No Experience":
            self.skills.set_skills_biz_slides(True)
        else:
            self.skills.set_skills_biz_slides(False)

        #skills_biz_pm
        if self.get_project_management() != "No Experience":
            self.skills.set_skills_biz_pm(True)
        else:
            self.skills.set_skills_biz_pm(False)


        #skills_biz_speaking
        if self.get_public_speaking() != "No Experience":
            self.skills.set_skills_biz_speaking(True)
        else:
            self.skills.set_skills_biz_speaking(True)

        #skills_biz_email
        if self.get_email_administrative_software() != "No Experience":
            self.skills.set_skills_biz_email(True)
        else:
            self.skills.set_skills_biz_email(False)


        #skills_ed_secondary
        if self.get_secondary_level_instruction() != "No Experience":
            self.skills.set_skills_ed_secondary(True)
        else:
            self.skills.set_skills_ed_secondary(False)


        #skills_ed_adult
        if self.get_adult_education_training() != "No Experience":
            self.skills.set_skills_ed_adult(True)
        else:
            self.skills.set_skills_ed_adult(False)


        #skills_ed_elem
        if self.get_elementary_level_instruction() != "No Experience":
            self.skills.set_skills_ed_elem(True)
        else:
            self.skills.set_skills_ed_elem(False)

        #skills_ed_curriculum
        if self.get_curriculum_design() != "No Experience":
            self.skills.set_skills_ed_curriculum(True)
        else:
            self.skills.set_skills_ed_curriculum(False)


        #skills_other -- no match is performed on this criteria.

        # Set this extern's Work Style Match Skills.
        extern_flavor_of_work_list = self.get_flavor_of_work()
        extern_flavor_of_work_list = extern_flavor_of_work_list.upper()

        #style_driven : Expect workers to be self-driven
        if "Expect workers to be self-driven".upper() in extern_flavor_of_work_list:
            self.skills.set_style_driven(True)
        else:
            self.skills.set_style_driven(False)

        #style_collab : Collaborative work
        if "Collaborative work".upper() in extern_flavor_of_work_list:
            self.skills.set_style_collab(True)
        else:
            self.skills.set_style_collab(False)

        #style_creative : Creative work
        if "Creative work".upper() in extern_flavor_of_work_list:
            self.skills.set_style_creative(True)
        else:
            self.skills.set_style_creative(True)

        #style_investigate : Research or investigative work
        if "Research or investigative work".upper() in extern_flavor_of_work_list:
            self.skills.set_style_investigate(True)
        else:
            self.skills.set_style_investigate(False)

        #style_task : Task-oriented work
        if "Task-oriented work".upper() in extern_flavor_of_work_list:
            self.skills.set_style_task(True)
        else:
            self.skills.set_style_task(False)

        #style_ambiguity : Comfort with ambiguity needed
        if "Comfort with ambiguity needed".upper() in extern_flavor_of_work_list:
            self.skills.set_style_ambiguity(True)
        else:
            self.skills.set_style_ambiguity(False)

        #style_organized : High level of organization needed
        if "High level of organization needed".upper() in extern_flavor_of_work_list:
            self.skills.set_style_organized(True)
        else:
            self.skills.set_style_organized(False)

        #style_direction : Directive in nature
        if "Directive in nature".upper() in extern_flavor_of_work_list:
            self.skills.set_style_direction(True)
        else:
            self.skills.set_style_direction(False)

        #style_networker : Strong appetite for networking & outreach needed
        if "Strong appetite for networking & outreach needed".upper() in extern_flavor_of_work_list:
            self.skills.set_style_networker(True)
        else:
            self.skills.set_style_networker(False)

        #style_structured : Has a structured environment
        if "Has a structured environment".upper() in extern_flavor_of_work_list:
            self.skills.set_style_structured(True)
        else:
            self.skills.set_style_structured(False)

        #style_teamlead : Has the opportunity for you to lead a small team
        if "Has the opportunity for you to lead a small team".upper() in extern_flavor_of_work_list:
            self.skills.set_style_teamlead(True)
        else:
            self.skills.set_style_teamlead(False)

        #style_other : - don't match on this.

        return None

    def get_id(self):
        return self.ID

    def get_start_time(self):
        return self.start_time

    def get_completion_time(self):
        return self.completion_time

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_who_are_you(self):
        return self.who_are_you

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_printable_name(self):
        return f"{self.get_last_name()}, {self.get_first_name()}"

    def get_primary_email(self):
        return self.primary_email

    def get_backup_email(self):
        return self.backup_email

    def get_school_where_you_work(self):
        return self.school_where_you_work

    def get_district_where_you_work(self):
        return self.district_where_you_work

    def get_current_roles(self):
        return self.current_roles

    def get_city_you_live_in(self):
        return self.city_you_live_in

    def get_why_part_of_program(self):
        return self.why_part_of_program

    def get_flavor_of_work(self):
        return self.flavor_of_work

    def get_flavor_of_work_printable_list(self):
        fow_lst = self.flavor_of_work.split(";")
        out_str = ""
        for f in fow_lst[0:-1]:
            out_str = out_str + f"\t* {f}\n"

        return out_str

    def get_why_most_interesting(self):
        return self.why_most_interesting

    def get_open_to_teaching(self):
        return self.open_to_teaching

    def get_open_to_curriculum_design(self):
        return self.open_to_curriculum_design

    def get_Open_to_camp_counselor(self):
        return self.Open_to_camp_counselor

    def get_particular_stem_fields(self):
        return self.particular_stem_fields

    def get_particular_stem_fields_printable_list(self):
        psf_lst = self.particular_stem_fields.split(";")
        out_str = ""
        for f in psf_lst[0:-1]:
            out_str = out_str + f"\t* {f}\n"

        return out_str

    def get_what_work_locations(self):
        return self.what_work_locations

    def get_open_to_remeote_printable(self):
        if "Remote" in self.what_work_locations:
            return "Yes"
        else:
            return "No"

    def get_open_to_travelling(self):
        return self.open_to_travelling

    def get_grade_levels(self):
        return self.grade_levels

    def get_grade_levels_printable_list(self):
        gl_lst = self.grade_levels.split(";")
        out_txt = ""
        for g in gl_lst[0:-1]:
            out_txt = out_txt + f"\t* {g}\n"

        return out_txt

    def get_stem_domains(self):
        return self.stem_domains

    def get_stem_domains_printable_list(self):
        out_txt = ""
        sd_lst = self.stem_domains.split(";")
        for s in sd_lst[0:-1]:
            out_txt = out_txt + f"\t* {s}\n"
        return out_txt

    def get_spreadsheet_software(self):
        return self.spreadsheet_software

    def get_word_processings_software(self):
        return self.word_processings_software

    def get_presentation_software(self):
        return self.presentation_software

    def get_business_software_skills_printable_list(self):
        out_txt = ""
        if self.get_spreadsheet_software() != "No Experience":
            out_txt = out_txt + f"\t* spreadsheet software:        {self.get_spreadsheet_software()}\n"
        if self.get_word_processings_software() != "No Experience":
            out_text = out_txt + f"\t* word processing:             {self.get_word_processings_software()}\n"
        if self.get_presentation_software() != "No Experience":
            out_txt = out_text + f"\t* presentation software:       {self.get_presentation_software()}\n"
        if self.get_project_management() != "No Experience":
            out_txt = out_txt + f"\t* project management software: {self.get_project_management()}\n"
        if self.get_email_administrative_software() != "No Experience":
            out_txt = out_txt + f"\t* administrative software:       {self.get_email_administrative_software()}\n"
        if self.get_public_speaking() != "No Experience":
            out_txt = out_txt + f"\t* public speaking:             {self.get_public_speaking()}\n"


        return out_txt

    def get_elementary_level_instruction(self):
         return self.elementary_level_instruction

    def get_curriculum_design(self):
        return self.curriculum_design

    def get_project_management(self):
        return self.project_management

    def get_secondary_level_instruction(self):
        return self.secondary_level_instruction

    def get_instructional_experience_printable_list(self):
        out_txt = ""
        if self.get_elementary_level_instruction() != "No Experience":
            out_txt = out_txt + f"\t* Elementary: {self.get_elementary_level_instruction()}\n"
        if self.get_secondary_level_instruction() != "No Experience:":
            out_txt = out_txt + f"\t* Secondary:  {self.get_secondary_level_instruction()}\n"
        if self.get_adult_education_training() != "No Experience":
            out_txt = out_txt + f"\t* Adult:      {self.get_adult_education_training()}"
        return out_txt

    def get_experiences_or_interests(self):
        return self.experiences_or_interests

    def get_linkedin_profile(self):
        return self.linkedin_profile

    def get_adult_education_training(self):
        return self.adult_education_training

    def get_public_speaking(self):
        return self.public_speaking

    def get_group_presentation(self):
        return self.group_presentation

    def get_email_administrative_software(self):
        return self.email_administrative_software

    def set_zip(self, zip):
        if zip == 83606:
            self.zip = 83605
        elif zip == 83205:
            self.zip = 83204
        elif zip == 83303:
            self.zip = 83301
        else:
            self.zip = zip

    def get_zip(self):
        return str(self.zip)

    def __str__(self):
        out_str = ""
        #out_str = out_str + f"ID : {self.ID}\n"
        #out_str = out_str + f"start_time : {self.start_time}\n"

        out_str = out_str + f"ID:{self.ID}\n"
        out_str = out_str + f"start_time:{self.start_time}\n"
        out_str = out_str + f"completion_time:{self.completion_time}\n"
        out_str = out_str + f"email:{self.email}\n"
        out_str = out_str + f"name:{self.name}\n"
        out_str = out_str + f"who_are_you:{self.who_are_you}\n"
        out_str = out_str + f"first_name:{self.first_name}\n"
        out_str = out_str + f"last_name:{self.last_name}\n"
        out_str = out_str + f"primary_email:{self.primary_email}\n"
        out_str = out_str + f"backup_email:{self.backup_email}\n"
        out_str = out_str + f"school_where_you_work:{self.school_where_you_work}\n"
        out_str = out_str + f"district_where_you_work:{self.district_where_you_work}\n"
        out_str = out_str + f"current_roles:{self.current_roles}\n"
        out_str = out_str + f"city_you_live_in:{self.city_you_live_in}\n"
        out_str = out_str + f"why_part_of_program:{self.why_part_of_program}\n"
        out_str = out_str + f"flavor_of_work:{self.flavor_of_work}\n"
        out_str = out_str + f"why_most_interesting:{self.why_most_interesting}\n"
        out_str = out_str + f"open_to_teaching:{self.open_to_teaching}\n"
        out_str = out_str + f"open_to_curriculum_design:{self.open_to_curriculum_design}\n"
        out_str = out_str + f"Open_to_camp_counselor:{self.Open_to_camp_counselor}\n"
        out_str = out_str + f"particular_stem_fields:{self.particular_stem_fields}\n"
        out_str = out_str + f"what_work_locations:{self.what_work_locations}\n"
        out_str = out_str + f"open_to_travelling:{self.open_to_travelling}\n"
        out_str = out_str + f"grade_levels:{self.grade_levels}\n"
        out_str = out_str + f"stem_domains:{self.stem_domains}\n"
        out_str = out_str + f"spreadsheet_software:{self.spreadsheet_software}\n"
        out_str = out_str + f"word_processings_software:{self.word_processings_software}\n"
        out_str = out_str + f"presentation_software:{self.presentation_software}\n"
        out_str = out_str + f"elementary_level_instruction:{self.elementary_level_instruction}\n"
        out_str = out_str + f"curriculum_design:{self.curriculum_design}\n"
        out_str = out_str + f"project_management:{self.project_management}\n"
        out_str = out_str + f"secondary_level_instruction:{self.secondary_level_instruction}\n"
        out_str = out_str + f"experiences_or_interests:{self.experiences_or_interests}\n"
        out_str = out_str + f"linkedin_profile:{self.linkedin_profile}\n"
        out_str = out_str + f"adult_education_training:{self.adult_education_training}\n"
        out_str = out_str + f"public_speaking:{self.public_speaking}\n"
        #out_str = out_str + f"group_presentation:{self.group_presentation}\n"
        out_str = out_str + f"email_administrative_software:{self.email_administrative_software}\n"

        out_str = out_str + "\n"
        out_str = out_str + f"{self.skills}"

        return out_str

    def save_dossier(self, to_file=False):
        origional_stdout = sys.stdout
        filename = f"{self.get_last_name()}_{self.get_first_name()}"
        # filepath = f"/home/jamie/PycharmProjects/skillMatch/data/dossier/{filename}.txt"
        filepath = f"/home/jamie/Source/Python/skillMatch/data/dossier{filename}.txt"

        with open(filepath, 'a') as f:
            sys.stdout = f
            #sys.stdout = origional_stdout #(uncomment this to print to the screen).

            print(f"Applicant : {self.get_printable_name()}")
            print(f"School (district) : {self.get_school_where_you_work()} ({self.get_district_where_you_work()})")
            print(f"Role(s) : {self.current_roles}")
            print(f"LinkedIn Profile : {self.get_linkedin_profile()}")
            print(f"")
            print(f"INTERESTS")
            print(f"Why they want to be a part of this program:")
            print(f"\t* {self.get_why_part_of_program()}")
            print(f"This applicant likes work environments that are:")
            print(f"{self.get_flavor_of_work_printable_list()}")
            print("STEM fields they are particularly interested in learning more about:")
            print(f"{self.get_particular_stem_fields_printable_list()}")
            print(f"EXPERIENCE")
            print(f"Grade Levels: ")    #From column X
            print(f"{self.get_grade_levels_printable_list()}")
            print(f"")
            print("Instructional Experience:")
            print(f"{self.get_instructional_experience_printable_list()}")
            print(f"")
            print("STEM Domain Experience")
            print(f"{self.get_stem_domains_printable_list()}")
            print("Business software & skills:")
            print(f"{self.get_business_software_skills_printable_list()}")
            print("Other interesting experience:")
            print(f"{self.get_experiences_or_interests()}")
            print(f"")
            print(f"LOGISTICS")
            print(f"Residence : {self.get_city_you_live_in()}") # Column N
            print(f"Open to Remote?")
            print(f"\t* {self.get_open_to_remeote_printable()}")
            print(f"")
            print(f"Open to temporary relocation?")
            print(f"\t* {self.get_open_to_travelling()}")
            print(f"")
            print(f"CONTACT")
            print(f"\t* Primary Email : {self.get_primary_email()}") # I
            print(f"\t* Secondary Email : {self.get_backup_email()}") # J



        # Return standard out back to origonal configuration.
        sys.stdout = origional_stdout

