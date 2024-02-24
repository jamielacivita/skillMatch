class Skills():
    def __init__(self, selections_lst = None):
        self.curriculum_design = False          #AD
        self.instruction_adult = False          #AJ
        self.instruction_elementary = False     #AC
        self.instruction_secondary = False      #AF
        self.project_management = False         #AE
        self.public_speaking = False            #AK
        self.software_email = False             #AL
        self.software_presentation = False      #AB
        self.software_spreadsheet = False       ##Z
        self.software_wordprocessing = False    #AA

    def __str__(self):
        out_str = ""

        out_str = out_str + f"curriculum_design :       {self.curriculum_design}\n"
        out_str = out_str + f"instruction_adult :       {self.instruction_adult}\n"
        out_str = out_str + f"instruction_elementary :  {self.instruction_elementary}\n"
        out_str = out_str + f"instruction_secondary :   {self.instruction_secondary}\n"
        out_str = out_str + f"project_management :      {self.project_management}\n"
        out_str = out_str + f"public_speaking :         {self.public_speaking}\n"
        out_str = out_str + f"software_email :          {self.software_email}\n"
        out_str = out_str + f"software_presentation :   {self.software_presentation}\n"
        out_str = out_str + f"software_spreadsheet :    {self.software_spreadsheet}\n"
        out_str = out_str + f"software_wordprocessing : {self.software_wordprocessing}\n"

        return out_str

    def set_curriculum_design(self, value):
        if ((value == True) or (value == False)):
            self.curriculum_design = value
            return self.curriculum_design
        else:
            self.curriculum_design = "ERROR!"
            return None

    def set_instruction_adult(self, value):
        if ((value == True) or (value == False)):
            self.instruction_adult = value
            return self.instruction_adult
        else:
            self.instruction_adult = "ERROR!"
            return None


    def set_instruction_elementary(self, value):
        if ((value == True) or (value == False)):
            self.instruction_elementary = value
            return self.instruction_elementary
        else:
            self.instruction_elementary = "ERROR!"
            return None

    def set_instruction_secondary(self, value):
        if ((value == True) or (value == False)):
            self.instruction_secondary = value
            return self.instruction_secondary
        else:
            self.instruction_secondary = "ERROR!"
            return None


    def set_project_management(self, value):
        if ((value == True) or (value == False)):
            self.project_management = value
            return self.project_management
        else:
            self.project_management = "ERROR!"
            return None


    def set_public_speaking(self, value):
        if ((value == True) or (value == False)):
            self.public_speaking = value
            return self.public_speaking
        else:
            self.public_speaking = "ERROR!"
            return None


    def set_software_email(self, value):
        if ((value == True) or (value == False)):
            self.software_email = value
            return self.software_email
        else:
            self.software_email = "ERROR!"
            return None


    def set_software_presentation(self, value):
        if ((value == True) or (value == False)):
            self.software_presentation = value
            return self.software_presentation
        else:
            self.software_presentation = "ERROR!"
            return None


    def set_software_spreadsheet(self, value):
        if ((value == True) or (value == False)):
            self.software_spreadsheet = value
            return self.software_spreadsheet
        else:
            self.software_spreadsheet = "ERROR!"
            return None


    def set_software_wordprocessing(self, value):
        if ((value == True) or (value == False)):
            self.software_wordprocessing = value
            return self.software_wordprocessing
        else:
            self.software_wordprocessing = "ERROR!"
            return None