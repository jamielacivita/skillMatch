import pickle

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

        self.curriculum_design_match = False
        self.instruction_adult_match = False
        self.instruction_elementary_match = False
        self.instruction_secondary_match = False
        self.project_management_match = False
        self.public_speaking_match = False
        self.software_email_match = False
        self.software_presentation_match = False
        self.software_spreadsheet_match = False
        self.software_wordprocessing_match = False

        #self.extern_zip = extern_obj.get_zip()
        #self.host_zip = host_obj.get_zip()
        self.distance = None

        self.match_score = 0

        ## Set Matching Values ##
        # check for curriculum_design_match
        if self.extern_obj.skills.curriculum_design and self.host_obj.skills.curriculum_design:
            self.curriculum_design_match = True
            self.match_score = self.match_score + 1

        # check for instruction_adult_match
        if self.extern_obj.skills.instruction_adult and self.host_obj.skills.instruction_adult:
            self.instruction_adult_match = True
            self.match_score = self.match_score + 1

        ## Calculate Distance ##
        #self.distance = distance_dict[(self.extern_zip,self.host_zip)]

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