from AttributeSet import AttributeSet


import logging
log = logging.getLogger(__name__)

class HostOld(AttributeSet):
    def __init__(self, selections_lst = None):

        if selections_lst:
            self.name = selections_lst[0]
            self.zip = selections_lst[1]
            self.skill01 = selections_lst[2]
            self.skill02 = selections_lst[3]
            self.skill03 = selections_lst[4]
            self.skill04 = selections_lst[5]
            self.skill05 = selections_lst[6]
            self.attitude01 = selections_lst[7]
            self.attitude02 = selections_lst[8]
            self.attitude03 = selections_lst[9]
            self.attitude04 = selections_lst[10]
            self.attitude05 = selections_lst[11]

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
        self.specific_educator = None
        self.skills = None
        self.looking_for_experience = None
        self.type_of_person = None
        self.work_done_remotely = None

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
        self.best_suited = None
        self.report_to_name = None
        self.report_to_email = None
        self.other_teams = None
        self.work_done_remotely = None
        self.travel_rerquired = None
        self.travel_rerquired_description = None
        self.how_hours_spent = None
        self.onboarding_and_training = None
        self.who_responsible_onboarding = None
        self.how_many_hours_onboarding = None
        self.anything_else = None

        self.zip = None

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
        BEST_SUITED_COL = 35                    ## AJ
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


        self.set_id(row_data_tuple[ID_COL].value)
        self.set_start_time(row_data_tuple[START_TIME_COL].value)
        self.set_completion_time(row_data_tuple[COMPLETION_TIME_COL].value)
        self.set_email(row_data_tuple[EMAIL_COL].value)
        self.set_name(row_data_tuple[NAME_COL].value)
        self.set_last_modified_time(LAST_MODIFIED_TIME_COL)
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
        self.set_best_suited(row_data_tuple[BEST_SUITED_COL].value)
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
        return self.last_name


    def set_email_address(self, email_address):
        self.email_address = email_address

    def get_email_address(self):
        return self.email_address


    def set_organization_name(self, organization_name):
        self.organization_name = organization_name

    def get_organization_name(self):
        return self.organization_name


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

    def set_skills(self,skills):
        return self.skills

    def get_skills(self):
        return self.skills
    def set_looking_for_experience(self,looking_for_experience):
        self.looking_for_experience = looking_for_experience

    def get_looking_for_experience(self):
        return self.looking_for_experience
    def set_type_of_person(self,type_of_person):
        self.type_of_person = type_of_person

    def get_type_of_person(self):
        return self.type_of_person
    def set_work_done_remotely(self,work_done_remotely):
        self.work_done_remotely = work_done_remotely

    def get_work_done_remotely(self):
        return self.work_done_remotely
    def set_zip(self,zip):
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

    def __str__(self):
        return f"ID: {self.get_id()} : zip: {self.get_zip()}"
