from AttributeSet import AttributeSet
import Skills as Skills
import sys
import re


import logging
log = logging.getLogger(__name__)


class Host(AttributeSet):
    def __init__(self, row_data_tuple):

        self.id = None
        self.start_time = None
        self.completion_time = None
        self.email = None
        self.name = None

        self.last_modified_time = None
        self.completed_work_proposal = None
        self.first_name = None
        self.last_name = None
        self.email_address = None

        self.organization_name = None
        self.location_of_organization = None
        self.overview_of_organization = None
        self.title_role = None
        self.specific_educator = None

        self.primary_contact = None
        self.poc_first_name = None
        self.poc_last_name = None
        self.poc_email = None
        self.poc_title_role = None

        self.why_part = None
        self.hours_per_week = None
        self.continuing_relationship = None
        self.how_many_externs = None
        self.project_name = None

        self.project_objectives = None
        self.description = None
        self.meaningful_learning = None
        self.network_growth = None
        self.professional_level_work = None

        self.set_up_success = None
        self.what_type_learning = None
        self.learn_the_things = None
        self.business_education_skills = None
        self.looking_for_experience = None

        self.type_of_person = None
        self.report_to_name = None
        self.report_to_email = None
        self.other_teams = None
        self.work_done_remotely = None

        self.zip = None
        self.travel_rerquired = None
        self.travel_rerquired_description = None
        self.how_hours_spent = None
        self.onboarding_and_training = None

        self.who_responsible_onboarding = None
        self.how_many_hours_onboarding = None
        self.anything_else = None
        self.min_externs = None
        self.max_externs = None

        #append a skills object to hold data for skills matches.
        self.skills = Skills.Skills()




        ID_COL = 0                              ## A
        START_TIME_COL = 1                      ## B
        COMPLETION_TIME_COL = 2                 ## C
        EMAIL_COL = 3                           ## D
        NAME_COL = 4                            ## E
        LAST_MODIFIED_TIME_COL = 5              ## F
        COMPLETED_WORK_PROPOSAL_COL = 6         ## G
        FIRST_NAME_COL = 7                      ## H
        LAST_NAME_COL = 8                       ## I
        EMAIL_ADDRESS_COL = 9                   ## J
        ORGANIZATION_NAME_COL = 10              ## K
        LOCATION_OF_ORGANIZATION_COL = 11       ## L
        OVERVIEW_OF_ORGANIZATION_COL = 12       ## M
        TITLE_ROLE_COL = 13                     ## N
        SPECIFIC_EDUCATOR_COL = 14              ## O
        PRIMARY_CONTACT_COL = 15                ## P
        POC_FIRST_NAME_COL = 16                 ## Q
        POC_LAST_NAME_COL  = 17                 ## R
        POC_EMAIL_COL = 18                      ## S
        POC_TITLE_ROLE_COL = 19                 ## T
        WHY_PART_COL = 20                       ## U
        HOURS_PER_WEEK_COL = 21                 ## V
        CONTINUING_RELATIONSHIP_COL = 22        ## W
        HOW_MANY_EXTERNS_COL = 23               ## X
        PROJECT_NAME_COL = 24                   ## y
        PROJECT_OBJECTIVES_COL = 25             ## Z
        DESCRIPTION_COL = 26                    ## AA
        MEANINGFUL_LEARNING_COL = 27            ## AB
        NETWORK_GROWTH_COL = 28                 ## AC
        PROFESSIONAL_LEVEL_WORK_COL = 29        ## AD
        SET_UP_SUCCESS_COL = 30                 ## AE
        WHAT_TYPE_LEARNING_COL = 31             ## AF
        LEARN_THE_THINGS_COL = 32               ## AG
        BUSINESS_EDUCATION_SKILLS_COL = 33      ## AH
        LOOKING_FOR_EXPERIENCE_COL = 34         ## AI
        TYPE_OF_PERSON_COL = 35                 ## AJ
        REPORT_TO_NAME_COL = 36                 ## AK
        REPORT_TO_EMAIL_COL = 37                ## AL
        OTHER_TEAMS_COL = 38                    ## AM
        WORK_DONE_REMOTELY_COL = 39             ## AN
        ZIP_COL = 40                            ## AO
        TRAVEL_RERQUIRED_COL = 41               ## AP
        TRAVEL_RERQUIRED_DESCRIPTION_COL = 42   ## AQ
        HOW_HOURS_SPENT_COL = 43                ## AR
        ONBOARDING_AND_TRAINING_COL = 44        ## AS
        WHO_RESPONSIBLE_ONBOARDING_COL = 45     ## AT
        HOW_MANY_HOURS_ONBOARDING_COL = 46      ## AU
        ANYTHING_ELSE_COL = 47                  ## AV
        MIN_EXTERNS = 48                        ## AW
        MAX_EXTERNS = 49                        ## Ax


        self.set_id(row_data_tuple[ID_COL].value)
        self.set_start_time(row_data_tuple[START_TIME_COL].value)
        self.set_completion_time(row_data_tuple[COMPLETION_TIME_COL].value)
        self.set_email(row_data_tuple[EMAIL_COL].value)
        self.set_name(row_data_tuple[NAME_COL].value)
        self.set_last_modified_time(row_data_tuple[LAST_MODIFIED_TIME_COL].value)
        self.set_completed_work_proposal(row_data_tuple[COMPLETED_WORK_PROPOSAL_COL].value)
        self.set_first_name(row_data_tuple[FIRST_NAME_COL].value)
        self.set_last_name(row_data_tuple[LAST_NAME_COL].value)
        self.set_email_address(row_data_tuple[EMAIL_ADDRESS_COL].value)
        self.set_organization_name(row_data_tuple[ORGANIZATION_NAME_COL].value)
        self.set_location_of_organization(row_data_tuple[LOCATION_OF_ORGANIZATION_COL].value)
        self.set_overview_of_organization(row_data_tuple[OVERVIEW_OF_ORGANIZATION_COL].value)
        self.set_title_role(row_data_tuple[TITLE_ROLE_COL].value)
        self.set_specific_educator(row_data_tuple[SPECIFIC_EDUCATOR_COL].value)
        self.set_primary_contact(row_data_tuple[PRIMARY_CONTACT_COL].value)
        self.set_poc_first_name(row_data_tuple[POC_FIRST_NAME_COL].value)
        self.set_poc_last_name(row_data_tuple[POC_LAST_NAME_COL].value)
        self.set_poc_email(row_data_tuple[POC_EMAIL_COL].value)
        self.set_poc_title_role(row_data_tuple[POC_TITLE_ROLE_COL].value)
        self.set_why_part(row_data_tuple[WHY_PART_COL].value)
        self.set_hours_per_week(row_data_tuple[HOURS_PER_WEEK_COL].value)
        self.set_continuing_relationship(row_data_tuple[CONTINUING_RELATIONSHIP_COL].value)
        self.set_how_many_externs(row_data_tuple[HOW_MANY_EXTERNS_COL].value)
        self.set_project_name(row_data_tuple[PROJECT_NAME_COL].value)
        self.set_project_objectives(row_data_tuple[PROJECT_OBJECTIVES_COL].value)
        self.set_description(row_data_tuple[DESCRIPTION_COL].value)
        self.set_meaningful_learning(row_data_tuple[MEANINGFUL_LEARNING_COL].value)
        self.set_network_growth(row_data_tuple[NETWORK_GROWTH_COL].value)
        self.set_professional_level_work(row_data_tuple[PROFESSIONAL_LEVEL_WORK_COL].value)
        self.set_set_up_success(row_data_tuple[SET_UP_SUCCESS_COL].value)
        self.set_what_type_learning(row_data_tuple[WHAT_TYPE_LEARNING_COL].value)
        self.set_learn_the_things(row_data_tuple[LEARN_THE_THINGS_COL].value)
        self.set_business_education_skills(row_data_tuple[BUSINESS_EDUCATION_SKILLS_COL].value)
        self.set_looking_for_experience(row_data_tuple[LOOKING_FOR_EXPERIENCE_COL].value)
        self.set_type_of_person(row_data_tuple[TYPE_OF_PERSON_COL].value)
        self.set_report_to_name(row_data_tuple[REPORT_TO_NAME_COL].value)
        self.set_report_to_email(row_data_tuple[REPORT_TO_EMAIL_COL].value)
        self.set_other_teams(row_data_tuple[OTHER_TEAMS_COL].value)
        self.set_work_done_remotely(row_data_tuple[WORK_DONE_REMOTELY_COL].value)
        self.set_travel_rerquired(row_data_tuple[TRAVEL_RERQUIRED_COL].value)
        self.set_travel_rerquired_description(row_data_tuple[TRAVEL_RERQUIRED_DESCRIPTION_COL].value)
        self.set_how_hours_spent(row_data_tuple[HOW_HOURS_SPENT_COL].value)
        self.set_onboarding_and_training(row_data_tuple[ONBOARDING_AND_TRAINING_COL].value)
        self.set_who_responsible_onboarding(row_data_tuple[WHO_RESPONSIBLE_ONBOARDING_COL].value)
        self.set_how_many_hours_onboarding(row_data_tuple[HOW_MANY_HOURS_ONBOARDING_COL].value)
        self.set_anything_else(row_data_tuple[ANYTHING_ELSE_COL].value)
        self.set_zip(row_data_tuple[ZIP_COL].value)
        self.set_min_externs(row_data_tuple[MIN_EXTERNS].value)
        self.set_max_externs(row_data_tuple[MAX_EXTERNS].value)

        self.set_skills()





    def set_id(self, id):
        self.id = id
        if not isinstance(self.id, int):
            print("Warning!")

    def get_id(self):
        return self.id

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_start_time(self):
        return self.start_time

    def set_completion_time(self, completion_time):
        self.completion_time = completion_time

    def get_completion_time(self):
        return self.completion_time

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_name(self, start_name):
        self.start_name = start_name

    def get_name(self):
        return self.name

    def set_last_modified_time(self, last_modified_time):
        self.last_modified_time = last_modified_time

    def get_last_modified_time(self):
        return self.last_modified_time

    def set_completed_work_proposal(self, completed_work_proposal):
        self.completed_work_proposal = completed_work_proposal

    def get_completed_work_proposal(self):
        return self.completed_work_proposal

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_email_address(self, email_address):
        self.email_address = email_address

    def get_email_address(self):
        return self.email_address


    def set_organization_name(self, organization_name):
        self.organization_name = organization_name

    def get_organization_name(self):
        return self.organization_name

    def get_organization_name_filesafe(self):
        id = self.get_id()
        name = re.sub(r'\W+', '', self.organization_name)
        return f"{id}_{name}"


    def set_location_of_organization(self, location_of_organization):
        self.location_of_organization = location_of_organization

    def get_location_of_organization(self):
        return self.location_of_organization

    def set_specific_educator(self, specific_educator):
        self.specific_educator = specific_educator

    def get_specific_educator(self):
        return self.specific_educator

    def set_overview_of_organization(self, overview_of_organization):
        self.overview_of_organization = overview_of_organization

    def get_overview_of_organization(self):
        return self.overview_of_organization

    def set_title_role(self, title_role):
        self.title_role = title_role

    def get_title_role(self):
        return self.title_role

    def set_primary_contact(self, primary_contact):
        self.primary_contact = primary_contact

    def get_primary_contact(self):
        return self.primary_contact

    def set_poc_first_name(self, poc_first_name):
        self.poc_first_name = poc_first_name

    def get_poc_first_name(self):
        return self.poc_first_name

    def set_poc_last_name(self, poc_last_name):
        self.poc_last_name = poc_last_name

    def get_poc_last_name(self):
        return self.poc_last_name

    def set_poc_email(self, poc_email):
        self.poc_email = poc_email

    def get_poc_email(self):
        return self.poc_email

    def set_poc_title_role(self, poc_title_role):
        self.poc_title_role = poc_title_role

    def get_poc_title_role(self):
        return self.poc_title_role

    def set_why_part(self, why_part):
        self.why_part = why_part

    def get_why_part(self):
        return self.why_part

    def set_hours_per_week(self, hours_per_week):
        self.hours_per_week = hours_per_week

    def get_hours_per_week(self):
        return self.hours_per_week

    def set_continuing_relationship(self, continuing_relationship):
        self.continuing_relationship = continuing_relationship

    def get_continuing_relationship(self):
        return self.continuing_relationship

    def set_how_many_externs(self, how_many_externs):
        self.how_many_externs = how_many_externs

    def get_how_many_externs(self):
        return self.how_many_externs

    def set_min_externs(self, min_externs):
        self.min_externs = min_externs

    def get_min_externs(self):
        return self.min_externs

    def set_max_externs(self, max_externs):
        self.max_externs = max_externs

    def get_max_externs(self):
        return self.max_externs


    def set_skills(self):

        host_list = self.get_looking_for_experience()
        host_list = host_list.upper()

        if "No, experience in a specific STEM domain isn't necessary".upper() in host_list:
            self.skills.set_stemexp_na(True)
            #log.debug(f"host {self.get_id()} matched on set_stemexp_na")

        if "Life science / biology".upper() in host_list:
            self.skills.set_stemexp_lifesci(True)
            #log.debug("host matched on set_stemexp_lifesci")

        if "Chemistry".upper() in host_list:
            self.skills.set_stemexp_chem(True)
            #log.debug("host matched on set_stemexp_chem")

        if "Physics".upper() in host_list:
            self.skills.set_stemexp_phys(True)
            #log.debug("host matched on set_stemexp_phys")

        if "Math".upper() in host_list:
            self.skills.set_stemexp_math(True)
            #log.debug("host matched on set_stemexp_math")

        if "Computer Science".upper() in host_list:
            self.skills.set_stemexp_compsci(True)
            #log.debug("host matched on set_stemexp_compsci")

        if "Information & communication technology".upper() in host_list:
            self.skills.set_stemexp_it(True)
            #log.debug("host matched on set_stemexp_it")

        if "Agriculture, Food, Natural Resources".upper() in host_list:
            self.skills.set_stemexp_ag(True)
            #log.debug("host matched on set_stemexp_ag")

        if "Engineering & Technology".upper() in host_list:
            self.skills.set_stemexp_eng(True)
            #log.debug("host matched on set_stemexp_eng")

        if "Health Professions".upper() in host_list:
            self.skills.set_stemexp_health(True)
            #log.debug("host matched on set_stemexp_health")

        if "Trades & Industry".upper() in host_list:
            self.skills.set_stemexp_trade(True)
            #log.debug("host matched on set_stemexp_trade")

        if "Earth & Environmental".upper() in host_list:
            self.skills.set_stemexp_env(True)
            #log.debug("host matched on set_stemexp_env")

        ## Business Skill Section ##
        host_list_business = self.get_business_education_skills()
        host_list_business = host_list_business.upper()

        #skills_biz_na
        if "No specific skills needed".upper() in host_list_business:
            self.skills.set_skills_biz_na(True)
        else:
            self.skills.set_skills_biz_na(False)

        #skills_biz_sheets
        if "Spreadsheet Software".upper() in host_list_business:
            self.skills.set_skills_biz_sheets(True)
        else:
            self.skills.set_skills_biz_sheets(False)

        #skills_biz_word
        if "Word Processing Software".upper() in host_list_business:
            self.skills.set_skills_biz_word(True)
        else:
            self.skills.set_skills_biz_word(False)

        #skills_biz_slides
        if "Presentation Software".upper() in host_list_business:
            self.skills.set_skills_biz_slides(True)
        else:
            self.skills.set_skills_biz_slides(False)

        #skills_biz_pm
        if "Project Management".upper() in host_list_business:
            self.skills.set_skills_biz_pm(True)
        else:
            self.skills.set_skills_biz_pm(False)

        #skills_biz_speaking
        if "Public Speaking".upper() in host_list_business:
            self.skills.set_skills_biz_speaking(True)
        else:
            self.skills.set_skills_biz_speaking(False)

        #skills_biz_email
        if "Administrative Software".upper() in host_list_business:
            self.skills.set_skills_biz_email(True)
        else:
            self.skills.set_skills_biz_email(False)


        #skills_ed_secondary
        if "Secondary-Level Instruction".upper() in host_list_business:
            self.skills.set_skills_ed_secondary(True)
        else:
            self.skills.set_skills_ed_secondary(False)

        #skills_ed_adult
        if "Adult Education".upper() in host_list_business:
            self.skills.set_skills_ed_adult(True)
        else:
            self.skills.set_skills_ed_adult(False)

        #skills_ed_elem
        if "Elementary-Level Instruction".upper() in host_list_business:
            self.skills.set_skills_ed_elem(True)
        else:
            self.skills.set_skills_ed_elem(False)

        #skills_ed_curriculum
        if "Curriculum Design".upper() in host_list_business:
            self.skills.set_skills_ed_curriculum(True)
        else:
            self.skills.set_skills_ed_curriculum(False)

        #skills_other - Not performing any matching on this property.


        ### Set this Host's Work Style Match Skills

        host_list_workstyle = self.get_type_of_person()
        host_list_workstyle = host_list_workstyle.upper()

        # style_driven : Self driven
        if "Self driven".upper() in host_list_workstyle:
            self.skills.set_style_driven(True)
        else:
            self.skills.set_style_driven(False)

        #style_collab : Collaborator
        if "Collaborator".upper() in host_list_workstyle:
            self.skills.set_style_collab(True)
        else:
            self.skills.set_style_collab(False)

        #style_creative : Creative
        if "Creative".upper() in host_list_workstyle:
            self.skills.set_style_creative(True)
        else:
            self.skills.set_style_creative(False)

        #style_investigate : Investigator
        if "Investigator".upper() in host_list_workstyle:
            self.skills.set_style_investigate(True)
        else:
            self.skills.set_style_investigate(False)

        #style_task : Task oriented
        if "Task oriented".upper() in host_list_workstyle:
            self.skills.set_style_task(True)
        else:
            self.skills.set_style_task(False)

        #style_ambiguity : Comfortable with ambiguity
        if "Comfortable with ambiguity".upper() in host_list_workstyle:
            self.skills.set_style_ambiguity(True)
        else:
            self.skills.set_style_ambiguity(False)

        #style_organized : Organized
        if "Organized".upper() in host_list_workstyle:
            self.skills.set_style_organized(True)
        else:
            self.skills.set_style_organized(False)

        #style_direction : Takes direction well
        if "Takes direction well".upper() in host_list_workstyle:
            self.skills.set_style_direction(True)
        else:
            self.skills.set_style_direction(False)

        #style_networker : Networker
        if "Networker".upper() in host_list_workstyle:
            self.skills.set_style_networker(True)
        else:
            self.skills.set_style_networker(False)

        #style_structured : Structured
        if "Structured".upper() in host_list_workstyle:
            self.skills.set_style_structured(True)
        else:
            self.skills.set_style_structured(False)

        #style_teamlead : Team driver
        if "Team driver".upper() in host_list_workstyle:
            self.skills.set_style_teamlead(True)
        else:
            self.skills.set_style_teamlead(False)

        #style_other -- don't match on this.

        return self.skills

    def get_skills(self):
        return self.skills
    def set_looking_for_experience(self,looking_for_experience):
        self.looking_for_experience = looking_for_experience

    def get_looking_for_experience(self):
        return self.looking_for_experience

    def get_looking_for_experience_printable_list(self):
        out_txt = ""
        lfe_lst = self.get_looking_for_experience().split(";")
        for l in lfe_lst[0:-1]:
            out_txt = out_txt + f"\t* {l}\n"
        return out_txt

    def set_type_of_person(self,type_of_person):
        self.type_of_person = type_of_person

    def get_type_of_person(self):
        return self.type_of_person
    def set_work_done_remotely(self,work_done_remotely):
        self.work_done_remotely = work_done_remotely

    def get_work_done_remotely(self):
        return self.work_done_remotely
    def set_zip(self, zip):
        if self.get_id() == 5:
            self.zip = "83301"
        elif self.get_id() == 16:
            self.zip = "83201"
        elif self.get_id() == 31:
            self.zip = "83301"
        elif self.get_id() == 32:
            self.zip = "83647"
        elif self.get_id() == 36:
            self.zip = "83702"
        elif self.get_id() == 41:
            self.zip = "83702"
        else:
            self.zip = zip

    def get_zip(self):
        return self.zip

    def set_project_name(self, project_name):
        self.project_name = project_name

    def get_project_name(self):
        return self.project_name

    def set_project_objectives(self, project_objectives):
        self.project_objectives = project_objectives

    def get_project_objectives(self):
        return self.project_objectives

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_meaningful_learning(self, meaningful_learning):
        self.meaningful_learning = meaningful_learning

    def get_meaningful_learning(self):
        return self.meaningful_learning

    def set_network_growth(self, network_growth):
        self.network_growth = network_growth

    def get_network_growth(self):
        return self.network_growth

    def set_professional_level_work(self, professional_level_work):
        self.professional_level_work = professional_level_work

    def get_professional_level_work(self):
        return self.professional_level_work

    def set_set_up_success(self, set_up_success):
        self.set_up_success = set_up_success

    def get_set_up_success(self):
        return self.set_up_success

    def set_what_type_learning(self, what_type_learning):
        self.what_type_learning = what_type_learning

    def get_what_type_learning(self):
        return self.what_type_learning

    def set_learn_the_things(self, learn_the_things):
        self.learn_the_things = learn_the_things

    def get_learn_the_things(self):
        return self.learn_the_things

    def set_business_education_skills(self, business_education_skills):
        self.business_education_skills = business_education_skills

    def get_business_education_skills(self):
        return self.business_education_skills

    def set_looking_for_experience(self, looking_for_experience):
        self.looking_for_experience = looking_for_experience

    def get_looking_for_experience(self):
        return self.looking_for_experience

    def set_best_suited(self, best_suited):
        self.best_suited = best_suited

    def get_best_suited(self):
        return self.best_suited

    def set_report_to_name(self, report_to_name):
        self.report_to_name = report_to_name

    def get_report_to_name(self):
        return self.report_to_name

    def set_report_to_email(self, report_to_email):
        self.report_to_email = report_to_email

    def get_report_to_email(self):
        return self.report_to_email

    def set_other_teams(self, other_teams):
        self.other_teams = other_teams

    def get_other_teams(self):
        return self.other_teams

    def set_work_done_remotely(self, work_done_remotely):
        self.work_done_remotely = work_done_remotely

    def get_work_done_remotely(self):
        return self.work_done_remotely

    def set_travel_rerquired(self, travel_rerquired):
        self.travel_rerquired = travel_rerquired

    def get_travel_rerquired(self):
        return self.travel_rerquired

    def set_travel_rerquired_description(self, travel_rerquired_description):
        self.travel_rerquired_description = travel_rerquired_description

    def get_travel_rerquired_description(self):
        return self.travel_rerquired_description

    def set_how_hours_spent(self, how_hours_spent):
        self.how_hours_spent = how_hours_spent

    def get_how_hours_spent(self):
        return self.how_hours_spent

    def set_onboarding_and_training(self, onboarding_and_training):
        self.onboarding_and_training = onboarding_and_training

    def get_onboarding_and_training(self):
        return self.onboarding_and_training

    def set_who_responsible_onboarding(self, who_responsible_onboarding):
        self.who_responsible_onboarding = who_responsible_onboarding

    def get_who_responsible_onboarding(self):
        return self.who_responsible_onboarding

    def set_how_many_hours_onboarding(self, how_many_hours_onboarding):
        self.how_many_hours_onboarding = how_many_hours_onboarding

    def get_how_many_hours_onboarding(self):
        return self.how_many_hours_onboarding

    def set_anything_else(self, anything_else):
        self.anything_else = anything_else

    def get_anything_else(self):
        return self.anything_else

    def get_no_skills_needed(self):
        if (self.skills.stemexp_na):
            return True
        else:
            return False

    def __str__(self):
        out_str = ""
        out_str = out_str + f"ID: {self.get_id()}\n"
        out_str = out_str + f"Start Time: {self.get_start_time()}\n"
        out_str = out_str + f"Completion Time: {self.get_completion_time()}\n"
        out_str = out_str + f"email: {self.get_email()}\n"
        out_str = out_str + f"name: {self.get_name()}\n"

        out_str = out_str + f"last modified time: {self.get_last_modified_time()}\n"
        out_str = out_str + f"completed work proposal: {self.get_completed_work_proposal()}\n"
        out_str = out_str + f"first name: {self.get_first_name()}\n"
        out_str = out_str + f"last name: {self.get_last_name()}\n"
        out_str = out_str + f"email address: {self.get_email_address()}\n"

        out_str = out_str + f"organization name: {self.get_organization_name()}\n"
        out_str = out_str + f"location of orgnization: {self.get_location_of_organization()}\n"
        out_str = out_str + f"overivew of orgnization: {self.get_overview_of_organization()}\n"
        out_str = out_str + f"title role: {self.get_title_role()}\n"
        out_str = out_str + f"specific educator: {self.get_specific_educator()}\n"

        out_str = out_str + f"prinary contact: {self.get_primary_contact()}\n"
        out_str = out_str + f"poc first name: {self.get_poc_first_name()}\n"
        out_str = out_str + f"poc last name: {self.get_poc_last_name()}\n"
        out_str = out_str + f"poc e-mail: {self.get_poc_email()}\n"
        out_str = out_str + f"poc title role: {self.get_poc_title_role()}\n"

        out_str = out_str + f"why orgnization: {self.get_why_part()}\n"
        out_str = out_str + f"hours per week: {self.get_hours_per_week()}\n"
        out_str = out_str + f"continuing relationship: {self.get_continuing_relationship()}\n"
        out_str = out_str + f"how many externs: {self.get_how_many_externs()}\n"
        out_str = out_str + f"project name: {self.get_project_name()}\n"

        out_str = out_str + f"project objectives: {self.get_project_objectives()}\n"
        out_str = out_str + f"description: {self.get_description()}\n"
        out_str = out_str + f"meangful learning: {self.get_meaningful_learning()}\n"
        out_str = out_str + f"network growth: {self.get_network_growth()}\n"
        out_str = out_str + f"professional level work: {self.get_professional_level_work()}\n"

        out_str = out_str + f"set up sucess: {self.get_set_up_success()}\n"
        out_str = out_str + f"what type learning: {self.get_what_type_learning()}\n"
        out_str = out_str + f"learn the things: {self.get_learn_the_things()}\n"
        out_str = out_str + f"business education skills: {self.get_business_education_skills()}\n"
        out_str = out_str + f"looking for experience: {self.get_looking_for_experience()}\n"

        out_str = out_str + f"type of person: {self.get_type_of_person()}\n"
        out_str = out_str + f"report to name: {self.get_report_to_name()}\n"
        out_str = out_str + f"report to email: {self.get_report_to_email()}\n"
        out_str = out_str + f"get other teams: {self.get_other_teams()}\n"
        out_str = out_str + f"work done remotely: {self.get_work_done_remotely()}\n"

        out_str = out_str + f"zip: {self.get_zip()}\n"
        out_str = out_str + f"travel required: {self.get_travel_rerquired()}\n"
        out_str = out_str + f"travel required description: {self.get_travel_rerquired_description()}\n"
        out_str = out_str + f"how hours spent: {self.get_how_hours_spent()}\n"
        out_str = out_str + f"get onboarding and training: {self.get_onboarding_and_training()}\n"

        out_str = out_str + f"who responsible for onboarding: {self.get_who_responsible_onboarding()}\n"
        out_str = out_str + f"how many hours onborading: {self.get_how_many_hours_onboarding()}\n"
        out_str = out_str + f"anything else :  {self.get_anything_else()}\n"

        out_str = out_str + f"{self.skills}"

        return out_str

    def save_dossier(self, to_file=False):
        origional_stdout = sys.stdout
        filename = f"{self.get_organization_name_filesafe()}"
        # filepath = f"/home/jamie/PycharmProjects/skillMatch/data/dossier/{filename}.txt"
        filepath = f"/home/jamie/Source/Python/skillMatch/data/dossier{filename}.txt"
        with open(filepath, 'a') as f:
            sys.stdout = f
            #sys.stdout = origional_stdout #(uncomment this to print to the screen).

            print(f"Organization: {self.get_organization_name()}")
            print(f"Contact: {self.get_last_name()}, {self.get_first_name()}")
            print(f"Email: {self.get_email_address()}")
            print(f"Location: {self.get_location_of_organization()}")
            print(f"Remote Possible: {self.get_work_done_remotely()}")
            print(f"")

            print(f"ABOUT THE ORGANIZATION:")
            print(f"{self.get_overview_of_organization()}")
            print(f"")

            print(f"ABOUT THE PROJECT")
            print(f"Name")
            print(f"\t* {self.get_project_name()}")
            print(f"")

            print(f"Objectives")
            print(f"\t* {self.get_project_objectives()}")
            print(f"")

            print(f"Description and day-to-day tasks:")
            print(f"\t* {self.get_description().strip()}")
            print(f"")

            print(f"Meaningful learning about STEM careers:")
            print(f"\t* {self.get_meaningful_learning()}")
            print(f"")

            print(f"Network growth:")
            print(f"\t* {self.get_network_growth()}")
            print(f"")

            print(f"Skills desired:")
            print(f"\t* {self.get_business_education_skills()}")
            print(f"")

            print(f"STEM domain experience desired:")
            print(f"\t* {self.get_looking_for_experience()}")
            print(f"\n")
        # Return standard out back to origonal configuration.
        sys.stdout = origional_stdout