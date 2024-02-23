from AttributeSet import AttributeSet
import Skills as Skills

import logging
log = logging.getLogger(__name__)
print(log)
class Extern(AttributeSet):
    def __init__(self, row_data_tuple):

        self.ID = None
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
        self.flavor_of_work = None
        self.why_most_interesting = None
        self.open_to_teaching = None
        self.open_to_curriculum_design = None
        self.Open_to_camp_counselor = None
        self.particular_stem_fields = None
        self.what_work_locations = None
        self.open_to_travelling = None
        self.grade_levels = None
        self.stem_domains = None
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

        #append a skills object to hold data for skills matches.
        self.skills = Skills.Skills()

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

        ## Run the function to set the skills.
        self.set_skills()
    def set_skills(self):
        # curriculum_design (AD)
        if self.curriculum_design == "Beginner":
            self.skills.set_curriculum_design(True)
        if self.curriculum_design == "Intermediate":
            self.skills.set_curriculum_design(True)
        if self.curriculum_design == "Expert":
            self.skills.set_curriculum_design(True)
        else:
            pass

        # instruction_adult (AJ)
        if self.adult_education_training == "Beginner":
            self.skills.set_instruction_adult(True)
        if self.adult_education_training == "Intermediate":
            self.skills.set_instruction_adult(True)
        if self.adult_education_training == "Expert":
            self.skills.set_instruction_adult(True)
        else:
            pass

        # instruction_elementary (AC)
        if self.elementary_level_instruction == "Beginner":
            self.skills.set_instruction_elementary(True)
        if self.elementary_level_instruction == "Intermediate":
            self.skills.set_instruction_elementary(True)
        if self.elementary_level_instruction == "Expert":
            self.skills.set_instruction_elementary(True)
        else:
            pass


        # instruction_secondary (AF)
        if self.secondary_level_instruction == "Beginner":
            self.skills.set_instruction_secondary(True)
        if self.secondary_level_instruction == "Intermediate":
            self.skills.set_instruction_secondary(True)
        if self.secondary_level_instruction == "Expert":
            self.skills.set_instruction_secondary(True)
        else:
            pass

        # project_management (AE)
        if self.project_management == "Beginner":
            self.skills.set_project_management(True)
        if self.project_management == "Intermediate":
            self.skills.set_project_management(True)
        if self.project_management == "Expert":
            self.skills.set_project_management(True)
        else:
            pass

        # public_speaking (AK)
        if self.public_speaking == "Beginner":
            self.skills.set_public_speaking(True)
        if self.public_speaking == "Intermediate":
            self.skills.set_public_speaking(True)
        if self.public_speaking == "Expert":
            self.skills.set_public_speaking(True)
        else:
            pass

        # software_email (AL)
        if self.email_administrative_software == "Beginner":
            self.skills.set_software_email(True)
        if self.email_administrative_software == "Intermediate":
            self.skills.set_software_email(True)
        if self.email_administrative_software == "Expert":
            self.skills.set_software_email(True)
        else:
            pass



        # software_presentation (AB)
        if self.presentation_software == "Beginner":
            self.skills.set_software_presentation(True)
        if self.presentation_software == "Intermediate":
            self.skills.set_software_presentation(True)
        if self.presentation_software == "Expert":
            self.skills.set_software_presentation(True)
        else:
            pass

        # software_spreadsheet (Z)
        if self.spreadsheet_software == "Beginner":
            self.skills.set_software_spreadsheet(True)
        if self.spreadsheet_software == "Intermediate":
            self.skills.set_software_spreadsheet(True)
        if self.spreadsheet_software == "Expert":
            self.skills.set_software_spreadsheet(True)
        else:
            pass


        # software_wordprocessing (AA)
        if self.word_processings_software == "Beginner":
            self.skills.set_software_wordprocessing(True)
        if self.word_processings_software == "Intermediate":
            self.skills.set_software_wordprocessing(True)
        if self.word_processings_software == "Expert":
            self.skills.set_software_wordprocessing(True)
        else:
            pass


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

    def get_ID(self):
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

    def get_what_work_locations(self):
        return self.what_work_locations

    def get_open_to_travelling(self):
        return self.open_to_travelling

    def get_grade_levels(self):
        return self.grade_levels

    def get_stem_domains(self):
        return self.stem_domains

    def get_spreadsheet_software(self):
        return self.spreadsheet_software

    def get_word_processings_software(self):
        return self.word_processings_software

    def get_presentation_software(self):
        return self.presentation_software

    def get_elementary_level_instruction(self):
         return self.elementary_level_instruction

    def get_curriculum_design(self):
        return self.curriculum_design

    def get_project_management(self):
        return self.project_management

    def get_secondary_level_instruction(self):
        return self.secondary_level_instruction

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
