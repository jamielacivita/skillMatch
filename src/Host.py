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
        self.specific_educator = None
        self.skills = None
        self.experience = None
        self.type_of_person = None
        self.remote = None
        self.zip = None

        ID_COL = 0
        START_TIME_COL = 1
        COMPLETION_TIME_COL = 2
        EMAIL_COL = 3
        NAME_COL = 4

        ZIP_COL = 40

        self.set_id(row_data_tuple[ID_COL].value)
        self.set_start_time(row_data_tuple[START_TIME_COL].value)
        self.set_completion_time(row_data_tuple[COMPLETION_TIME_COL].value)
        self.set_email(row_data_tuple[EMAIL_COL].value)
        self.set_name(row_data_tuple[NAME_COL].value)
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

    ###


    def set_specific_educator(self, specific_educator):
        self.specific_educator = specific_educator

    def get_specific_educator(self):
        return self.specific_educator
    def set_skills(self,skills):
        return self.skills

    def get_skills(self):
        return self.skills
    def set_experience(self,experience):
        self.experience = experience

    def get_experience(self):
        return self.experience
    def set_type_of_person(self,type_of_person):
        self.type_of_person = type_of_person

    def get_type_of_person(self):
        return self.type_of_person
    def set_remote(self,remote):
        self.remote = remote

    def get_remote(self):
        return self.remote
    def set_zip(self,zip):
        self.zip = zip

    def get_zip(self):
        return self.zip

    def __str__(self):
        return f"ID: {self.get_id()} : zip: {self.get_zip()}"
