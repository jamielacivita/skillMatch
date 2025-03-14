import sys
import os

from AttributeSet import AttributeSet
import Skills as Skills

import logging

from src.DataPool import DataPool

log = logging.getLogger(__name__)

city_zip = DataPool.get_city_dictionary(None)

class Extern(AttributeSet):
    def __init__(self, row_data_tuple):
        self.ID = None  # A
        self.start_time = None # B
        self.completion_time = None # C
        self.email = None # D
        self.name = None # E
        self.who_are_you = None # F
        self.first_name = None # G
        self.last_name = None # H
        self.primary_email = None # I
        self.backup_email = None # J
        self.school_where_you_work = None # K
        self.district_where_you_work = None # L
        self.current_roles = None # M
        self.city_you_live_in = None # N
        self.why_part_of_program = None # O
        self.flavor_of_work = None # P
        self.elementary_level_instruction = None # Q
        self.open_to_curriculum_design = None # R
        # Column S is just labeled "Colum1" and has no data.
        self.particular_stem_fields = None # T
        self.what_work_locations = None  # U
        self.open_to_travelling = None # V
        self.grade_levels = None # W
        self.stem_domains = None # X
        self.spreadsheet_software = None #Y
        # Column Z "Word Processing Software" does not have any data.

        self.why_most_interesting = None
        #self.open_to_teaching = None               ## Column Unknown

        self.Open_to_camp_counselor = None

        self.presentation_software = None #Z

        self.curriculum_design = None #AC
        self.project_management = None #AD
        self.secondary_level_instruction = None #AE
        self.experiences_or_interests = None #AI
        self.linkedin_profile = None #AJ
        self.adult_education_training = None #AF
        self.public_speaking = None #AG
        #self.group_presentation = None
        self.email_administrative_software = None #AH
        self.zip = None # This is a synthetic property -- needs conversion from City Live In to a zip.
        self.remote_only = None  # This is a synthetic property -- If extern ONLY indicated “remote” in column V, True
        self.phone = None # column AL (new in 2025)
        self.communication_and_availability = None # Column AN (new in 2025)
        self.open_to = None # column U (new in 2025)
        self.business_software_and_skills = None # column AW (revised in 2025)
        self.comfortable_and_confident = None # column AO
        self.open_to_secondary_teaching = None #(new in 2025) ## AQ
        self.open_to_adult_teaching = None #(new in 2025) ## AR
        self.externship_durations = None #(New in 2025) #AV
        self.zipcode_where_you_live = None #AP
        self.participated_before = None #AX

        #append a skills object to hold data for skills matches.
        self.skills = Skills.Skills()
        # set the synthetic remote only property
        self.set_remote_only()

        #extern column mapping dictionary
        extern_column = {}
        extern_column["A"] = 0
        extern_column["ID"] = 0
        extern_column["B"] = 1
        extern_column["Start time"] = 1
        extern_column["C"] = 2
        extern_column["Completion time"] = 2
        extern_column["D"] = 3
        extern_column["Email"] = 3
        extern_column["E"] = 4
        extern_column["Name"] = 4

        extern_column["F"] = 5
        extern_column["Who are you?"] = 5
        extern_column["G"] = 6
        extern_column["FIRST name:"] = 6
        extern_column["H"] = 7
        extern_column["LAST name:"] = 7
        extern_column["I"] = 8
        extern_column["Primary EMAIL address:"] = 8
        extern_column["J"] = 9
        extern_column["BACKUP EMAIL address::"] = 9

        extern_column["K"] = 10
        extern_column["Name of the SCHOOL where you work:"] = 10
        extern_column["L"] = 11
        extern_column["Name the DISTRICT where you work:"] = 11
        extern_column["M"] = 12
        extern_column["What are your CURRENT ROLE(S) at your school?"] = 12
        extern_column["N"] = 13
        extern_column["What city do you live in?"] = 13
        extern_column["O"] = 14
        extern_column["Why do you want to be a part of this program?"] = 14

        extern_column["P"]= 15
        extern_column["We also want to match you with the right flavor of work for you."]= 15
        extern_column["Q"]=16
        extern_column["Open to teaching elementary school kids?"]=16
        extern_column["R"]=17
        extern_column["Open to curriculum design?"]=17
        extern_column["S"]=18
        extern_column["Column1"]=18
        extern_column["T"]=19
        extern_column["Are there particular STEM fields you are interested in learning more about this summer?"]=19

        extern_column["U"] = 20
        extern_column["What work location(s) are you open to?"] = 20
        extern_column["V"] = 21
        extern_column["Are you open to travelling / temporary relocation for the externship?"] = 21
        extern_column["W"] = 22
        extern_column["What grade levels do you have experience working with?"] = 22
        extern_column["X"] = 23
        extern_column["Projects don't typically require any prior STEM domain experience, but occasionally it helps."] = 23
        extern_column["Y"] = 24
        extern_column["Spreadsheet Software (MS Excel or Google Sheets)"] = 24

        extern_column["Z"] = 25
        extern_column["Word Processing Software (MS Word or Google Docs)"] = 25
        extern_column["AA"] = 26
        extern_column["Presentation Software (MS Powerpoint or Google Slides)"] = 26
        extern_column["AB"] = 27
        extern_column["Elementary-Level Instruction"] = 27
        extern_column["AC"] = 28
        extern_column["Curriculum Design"] = 28
        extern_column["AD"] = 29
        extern_column["Project Management"] = 29

        extern_column["AE"] = 30
        extern_column["Secondary-Level Instruction"] = 30
        extern_column["AF"] = 31
        extern_column["Adult Education / Training"] = 31
        extern_column["AG"] = 32
        extern_column["Public Speaking / Group Presentation"] = 32
        extern_column["AH"] = 33
        extern_column["Email & Administrative Software"] = 33
        extern_column["AI"] = 34
        extern_column["Many hosts are interested in knowing about what experiences educators have enjoyed outside the classroom."] = 34

        extern_column["AJ"] = 35
        extern_column["If you have a LinkedIn profile, please share:"] = 35
        extern_column["AK"] = 36
        extern_column["Phone number:"] = 36
        extern_column["AL"] = 37
        extern_column["Phone number:"] = 37
        extern_column["AM"] = 38
        extern_column["Host sites will be reaching out via phone calls, emails, and/or text messaging. What is the best time of day for them to reach you?"] = 38
        extern_column["AN"] = 39
        extern_column["Communication & Availability"] = 39

        extern_column["AO"] = 40
        extern_column["I feel comfortable and confident in telling my students about how STEM skills show up in multiple types of careers."] = 40
        extern_column["AP"] = 41
        extern_column["ZIP code where you live?"] = 41
        extern_column["AQ"] = 42
        extern_column["Open to teaching secondary school kids?"] = 42
        extern_column["AR"] = 43
        extern_column["Open to teaching adults?"] = 43

        extern_column["AS"] = 44
        extern_column["Open to being a camp counselor?"] = 44
        extern_column["AT"] = 45
        extern_column["Open to curriculum design?"] = 45
        # extern_column["AU"] = 46
        # extern_column["Question"] = 46
        extern_column["AU"] = 46
        extern_column["While the typical externship is $5000 for 200 hours, some hosts may have opportunities for 100 hour externships at a reduced stipend of $2500."] = 46
        extern_column["AV"] = 47
        extern_column["occasionally hosts do look for a specific skill"] = 47

        extern_column["AW"] = 48
        extern_column["Have you participated in the Externship Program before?"] = 48

        blanktuple = (("x","y"))
        blanklist = []
        if type(row_data_tuple) == type(blanktuple):

            self.set_ID(row_data_tuple[extern_column["ID"]].value)
            self.set_start_time(row_data_tuple[extern_column["B"]].value)
            self.set_completion_time(row_data_tuple[extern_column["C"]].value)
            self.set_email(row_data_tuple[extern_column["D"]].value)
            self.set_name(row_data_tuple[extern_column["E"]].value)

            self.set_who_are_you(row_data_tuple[extern_column["F"]].value)
            self.set_first_name(row_data_tuple[extern_column["G"]].value)
            self.set_last_name(row_data_tuple[extern_column["H"]].value)
            self.set_primary_email(row_data_tuple[extern_column["I"]].value)
            self.set_backup_email(row_data_tuple[extern_column["J"]].value)

            self.set_school_where_you_work(row_data_tuple[extern_column["K"]].value)
            self.set_district_where_you_work(row_data_tuple[extern_column["L"]].value)
            self.set_current_roles(row_data_tuple[extern_column["M"]].value)
            self.set_city_you_live_in(row_data_tuple[extern_column["N"]].value)
            self.set_why_part_of_program(row_data_tuple[extern_column["O"]].value)

            self.set_flavor_of_work(row_data_tuple[extern_column["P"]].value)
            self.set_elementary_level_instruction(row_data_tuple[extern_column["Q"]].value)
            self.set_open_to_curriculum_design(row_data_tuple[extern_column["AT"]].value) #was R before.
            self.set_particular_stem_fields(row_data_tuple[extern_column["T"]].value)
            self.set_what_work_locations(row_data_tuple[extern_column["U"]].value)

            self.set_open_to_travelling(row_data_tuple[extern_column["V"]].value)
            self.set_grade_levels(row_data_tuple[extern_column["W"]].value)
            self.set_stem_domains(row_data_tuple[extern_column["X"]].value)
            self.set_spreadsheet_software(row_data_tuple[extern_column["Y"]].value)
            self.set_word_processings_software(row_data_tuple[extern_column["Z"]].value)

            self.set_presentation_software(row_data_tuple[extern_column["AA"]].value)
            # Column AB - elementary level instruction goes here.  No data in chart.
            self.set_curriculum_design(row_data_tuple[extern_column["AC"]].value)
            self.set_project_management(row_data_tuple[extern_column["AD"]].value)
            self.set_secondary_level_instruction(row_data_tuple[extern_column["AE"]].value)

            self.set_adult_education_training(row_data_tuple[extern_column["AF"]].value)
            self.set_public_speaking(row_data_tuple[extern_column["AG"]].value)
            self.set_email_administrative_software(row_data_tuple[extern_column["AH"]].value)
            self.set_experiences_or_interests(row_data_tuple[extern_column["AI"]].value)
            self.set_linkedin_profile(row_data_tuple[extern_column["AJ"]].value)

            self.set_phone(row_data_tuple[extern_column["AK"]].value)
            self.set_phone(row_data_tuple[extern_column["AL"]].value)

            # best time of day to reach you (column AM) goes here - No data in chart.
            self.set_communication_and_availability(row_data_tuple[extern_column["AN"]].value)
            self.set_business_software_and_skills(row_data_tuple[extern_column["AW"]])
            self.set_comfortable_and_confident((row_data_tuple[extern_column["AO"]]))
            self.set_open_to(row_data_tuple[extern_column["U"]])

            self.set_zipcode_where_you_live(row_data_tuple[extern_column["AP"]])
            self.set_open_to_secondary_teaching(row_data_tuple[extern_column["AQ"]])
            self.set_open_to_adult_teaching(row_data_tuple[extern_column["AR"]])
            self.set_Open_to_camp_counselor(row_data_tuple[extern_column["AS"]].value)
            self.set_open_to_curriculum_design(row_data_tuple[extern_column["AT"]])

            #todo : Question (column AU) goes here.
            self.set_externship_durations(row_data_tuple[extern_column["AV"]].value)
            self.set_participated_before(row_data_tuple[extern_column["AX"]])

            #self.set_why_most_interesting(row_data_tuple[WHY_MOST_INTERESTING_COL].value)
            #self.set_open_to_teaching(row_data_tuple[OPEN_TO_TEACHING_COL].value)

            #self.set_group_presentation(row_data_tuple[GROUP_PRESENTATION_COL].value)
            self.set_zip(city_zip[self.city_you_live_in])
            self.set_skills()
            self.set_remote_only()

        if type(row_data_tuple) == type(blanklist):

            self.set_ID(row_data_tuple[extern_column["ID"]])
            self.set_start_time(row_data_tuple[extern_column["B"]])
            self.set_completion_time(row_data_tuple[extern_column["C"]])
            self.set_email(row_data_tuple[extern_column["D"]])
            self.set_name(row_data_tuple[extern_column["Name"]])

            self.set_who_are_you(row_data_tuple[extern_column["F"]])
            self.set_first_name(row_data_tuple[extern_column["G"]])
            self.set_last_name(row_data_tuple[extern_column["H"]])
            self.set_primary_email(row_data_tuple[extern_column["I"]])
            self.set_backup_email(row_data_tuple[extern_column["J"]])

            self.set_school_where_you_work(row_data_tuple[extern_column["K"]])
            self.set_district_where_you_work(row_data_tuple[extern_column["L"]])
            self.set_current_roles(row_data_tuple[extern_column["M"]])
            self.set_city_you_live_in(row_data_tuple[extern_column["N"]])
            self.set_why_part_of_program(row_data_tuple[extern_column["O"]])

            self.set_flavor_of_work(row_data_tuple[extern_column["P"]])
            self.set_elementary_level_instruction(row_data_tuple[extern_column["Q"]])
            self.set_open_to_curriculum_design(row_data_tuple[extern_column["AT"]]) #was R before.
            self.set_particular_stem_fields(row_data_tuple[extern_column["T"]])
            self.set_what_work_locations(row_data_tuple[extern_column["U"]])

            self.set_open_to_travelling(row_data_tuple[extern_column["V"]])
            self.set_grade_levels(row_data_tuple[extern_column["W"]])
            self.set_stem_domains(row_data_tuple[extern_column["X"]])
            self.set_spreadsheet_software(row_data_tuple[extern_column["Y"]])
            self.set_word_processings_software(row_data_tuple[extern_column["Z"]])

            self.set_presentation_software(row_data_tuple[extern_column["AA"]])
            # Column AB - elementary level instruction goes here.  No data in chart.
            self.set_curriculum_design(row_data_tuple[extern_column["AC"]])
            self.set_project_management(row_data_tuple[extern_column["AD"]])
            self.set_secondary_level_instruction(row_data_tuple[extern_column["AE"]])

            self.set_adult_education_training(row_data_tuple[extern_column["AF"]])
            self.set_public_speaking(row_data_tuple[extern_column["AG"]])
            self.set_email_administrative_software(row_data_tuple[extern_column["AH"]])
            self.set_experiences_or_interests(row_data_tuple[extern_column["AI"]])
            self.set_linkedin_profile(row_data_tuple[extern_column["AJ"]])

            self.set_phone(row_data_tuple[extern_column["AK"]])
            self.set_phone(row_data_tuple[extern_column["AL"]])

            # best time of day to reach you (column AM) goes here - No data in chart.
            self.set_communication_and_availability(row_data_tuple[extern_column["AN"]])
            self.set_business_software_and_skills(row_data_tuple[extern_column["AV"]])
            self.set_comfortable_and_confident((row_data_tuple[extern_column["AO"]]))
            self.set_open_to(row_data_tuple[extern_column["U"]])

            self.set_zipcode_where_you_live(row_data_tuple[extern_column["AP"]])
            self.set_open_to_secondary_teaching(row_data_tuple[extern_column["AQ"]])
            self.set_open_to_adult_teaching(row_data_tuple[extern_column["AR"]])
            self.set_Open_to_camp_counselor(row_data_tuple[extern_column["AS"]])
            self.set_open_to_curriculum_design(row_data_tuple[extern_column["AT"]])

            #todo : Question (column AU) goes here.
            self.set_externship_durations(row_data_tuple[extern_column["AU"]])
            self.set_participated_before(row_data_tuple[extern_column["AW"]])

            #self.set_why_most_interesting(row_data_tuple[WHY_MOST_INTERESTING_COL].value)
            #self.set_open_to_teaching(row_data_tuple[OPEN_TO_TEACHING_COL].value)

            #self.set_group_presentation(row_data_tuple[GROUP_PRESENTATION_COL].value)
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

    def set_phone(self, phone):
        self.phone = phone

    def set_communication_and_availability(self, communication_and_availability):
        self.communication_and_availability = communication_and_availability

    def set_business_software_and_skills(self, business_software_and_skills):
        self.business_software_and_skills = business_software_and_skills

    def set_open_to(self, open_to):
        self.open_to = open_to

    def set_open_to_secondary_teaching(self, open_to_secondary):
        self.open_to_secondary_teaching = open_to_secondary

    def set_open_to_adult_teaching(self, open_to_adult_teaching):
        self.open_to_adult_teaching = open_to_adult_teaching

    def set_externship_durations(self, externship_durations):
        self.externship_durations = externship_durations

    def set_comfortable_and_confident(self, comfortable_and_confident):
        self.comfortable_and_confident = comfortable_and_confident

    def set_zipcode_where_you_live(self, zipcode_where_you_live):
        self.zipcode_where_you_live = zipcode_where_you_live

    def set_participated_before(self, participated_before):
        self.participated_before = participated_before

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
        return self.first_name.strip()

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
        #return self.open_to_teaching
        return ""
        #todo : Decide if this can be completely refactored out.

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
        skills_lst = []
        out_txt = ""
        for skill in self.get_business_software_and_skills().split(";"):
            skills_lst.append(skill)

        skills_lst.remove("")

        for skill in skills_lst:
            out_txt = out_txt + f"\t* {skill}\n"

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

    def get_business_software_and_skills(self):
        return self.business_software_and_skills

    def get_phone(self):
        return self.phone

    def get_communication_and_availability(self):
        return self.communication_and_availability

    def get_open_to(self):
        return self.open_to

    def get_open_to_printable_list(self):
        out_text = ""
        selection_lst = self.get_open_to().split(";")
        selection_lst.remove("")
        for s in selection_lst:
            out_text = out_text + f"\t* {s}\n"
        return out_text

    def get_externship_durations_printable_list(self):
        out_text = ""
        selection_lst = self.get_.split(";")  # here.
        for s in selection_lst:
            out_text = out_text + f"\t* {s}"
        return out_text

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

    def get_open_to_secondary_teaching(self):
        return self.open_to_secondary_teaching

    def get_open_to_adult_teaching(self):
        return self.open_to_adult_teaching

    def get_externship_durations(self):
        return self.externship_durations

    def get_comfortable_and_confident(self):
        return self.comfortable_and_confident

    def get_zipcode_where_you_live(self):
        return self.zipcode_where_you_live

    def get_participated_before(self):
        return self.participated_before

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
        original_stdout = sys.stdout
        filename = f"{self.get_last_name()}_{self.get_first_name()}"
        #filepath = f"/home/jamie/Source/Python/skillMatch/data/Output/dossier/extern/{filename}.txt"
        filepath = f"/home/jamie/source/skillMatch/data/Output/dossier/extern/{filename}.txt"

        try:
            os.remove(filepath)
        except FileNotFoundError:
            pass

        log.debug(f"writing file : {filepath}")

        with open(filepath, 'a') as f:
            sys.stdout = f
            #sys.stdout = original_stdout #(uncomment this to print to the screen).

            print(f"Applicant : {self.get_printable_name()}")
            print(f"School (district) : {self.get_school_where_you_work()} ({self.get_district_where_you_work()})")
            print(f"Role(s) : {self.current_roles}")
            print(f"LinkedIn Profile : {self.get_linkedin_profile()}")
            print(f"")
            print(f"INTERESTS")
            print(f"Why they want to be a part of this program:")
            print(f"\t* {self.get_why_part_of_program()}")
            # print(f"This applicant likes work environments that are:")
            # print(f"{self.get_flavor_of_work_printable_list()}")
            print("STEM fields they are particularly interested in learning more about:")
            print(f"{self.get_particular_stem_fields_printable_list()}")
            print(f"EXPERIENCE")
            print(f"Grade Levels: ")    #From column X
            print(f"{self.get_grade_levels_printable_list()}")
            print("STEM Domain Experience")
            print(f"{self.get_stem_domains_printable_list()}")
            print("Business software & skills:")
            print(f"{self.get_business_software_skills_printable_list()}")

            print("Instructional work they are open to during externship:")
            # Uses colums Q, AQ, AR, AS and AT.
            print(f"Elementary teaching : {self.get_elementary_level_instruction()}") #Q
            print(f"Secondary Teaching : {self.get_open_to_secondary_teaching()}") #AQ
            print(f"Adult Teaching : {self.get_open_to_adult_teaching()}") #AR
            print(f"Camp counselor : {self.get_Open_to_camp_counselor()}") #AS
            print(f"Curriculum design : {self.get_open_to_curriculum_design()}") #AT

            print("Externship durations they are available for:")
            # uses colum AV
            #todo: need a printable function for this data.

            print("Other interesting experience:")
            print(f"{self.get_experiences_or_interests()}")
            print(f"")
            print(f"LOGISTICS")
            print(f"Residence : {self.get_city_you_live_in()}") # Column N
            print(f"Open to:")
            print(self.get_open_to_printable_list())
            print(f"CONTACT")
            print(f"\t* Primary Email : {self.get_primary_email()}") # I
            print(f"\t* Secondary Email : {self.get_backup_email()}") # J
            print(f"\t* Phone : {self.get_phone()}") # J
            print(f"\t* Communication & Availability : {self.get_communication_and_availability()}") # AN

        # Return standard out back to original configuration.
        sys.stdout = original_stdout

