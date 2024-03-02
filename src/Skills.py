class Skills():
    def __init__(self, selections_lst = None):

        ## STEM experience match
        self.stemexp_na = None
        self.stemexp_lifesci = None
        self.stemexp_chem = None
        self.stemexp_phys = None
        self.stemexp_math = None
        self.stemexp_compsci = None
        self.stemexp_it = None
        self.stemexp_ag = None
        self.stemexp_eng = None
        self.stemexp_health = None
        self.stemexp_trade = None
        self.stemexp_env = None
        self.stemexp_other = None
        self.stemexp_notes = None

        ## Biz skills Match
        self.skills_biz_na = None
        self.skills_biz_sheets = None
        self.skills_biz_word = None
        self.skills_biz_slides = None
        self.skills_biz_pm = None
        self.skills_biz_speaking = None
        self.skills_biz_email = None
        self.skills_ed_secondary = None
        self.skills_ed_adult = None
        self.skills_ed_elem = None
        self.skills_ed_curriculum = None
        self.skills_other = None
        self.skills_biz_notes = None

        ## Work Style Match
        self.style_driven = None
        self.style_collab = None
        self.style_creative = None
        self.style_investigate = None
        self.style_task = None
        self.style_ambiguity = None
        self.style_organized = None
        self.style_direction = None
        self.style_networker = None
        self.style_structured = None
        self.style_teamlead = None
        self.style_other = None
        self.style_notes = None

    def set_stemexp_na(self, stemexp_na):
        self.stemexp_na = stemexp_na
        return None

    def set_stemexp_lifesci(self, stemexp_lifesci):
        self.stemexp_lifesci = stemexp_lifesci
        return None

    def get_stemexp_lifesci(self):
        return self.stemexp_lifesci

    def set_stemexp_chem(self, stemexp_chem):
        self.stemexp_chem = stemexp_chem
        return None

    def get_stemexp_chem(self):
        return self.stemexp_chem


    def set_stemexp_phys(self, stemexp_phys):
        self.stemexp_phys = stemexp_phys
        return None

    def get_stemexp_phys(self):
        return self.stemexp_phys

    def set_stemexp_math(self, stemexp_math):
        self.stemexp_math = stemexp_math
        return None

    def get_stemexp_math(self):
        return self.stemexp_math

    def set_stemexp_compsci(self, stemexp_compsci):
        self.stemexp_compsci = stemexp_compsci
        return None

    def get_stemexp_compsci(self):
        return self.stemexp_compsci

    def set_stemexp_it(self, stemexp_it):
        self.stemexp_it = stemexp_it
        return None

    def get_stemexp_it(self):
        return self.stemexp_it

    def set_stemexp_ag(self, stemexp_ag):
        self.stemexp_ag = stemexp_ag
        return None

    def get_stemexp_ag(self):
        return self.stemexp_ag

    def set_stemexp_eng(self, stemexp_eng):
        self.stemexp_eng = stemexp_eng
        return None

    def get_stemexp_eng(self):
        return self.stemexp_ag

    def set_stemexp_health(self, stemexp_health):
        self.stemexp_health = stemexp_health
        return None

    def get_stemexp_health(self):
        return self.stemexp_health

    def set_stemexp_trade(self, stemexp_trade):
        self.stemexp_trade = stemexp_trade
        return None

    def get_stemexp_trade(self):
        return self.stemexp_trade

    def set_stemexp_env(self, stemexp_env):
        self.stemexp_env = stemexp_env
        return None

    def get_stemexp_env(self):
        return self.stemexp_env

    def set_stemexp_other(self, stemexp_other):
        self.stemexp_other = stemexp_other
        return None

    def get_stemexp_other(self):
        return self.stemexp_other

    def set_stemexp_notes(self, stemexp_notes):
        if self.stemexp_notes is None:
            self.stemexp_notes = ""
        self.stemexp_notes = self.stemexp_notes + ":" + stemexp_notes
        return None

    def get_stemexp_notes(self):
        if self.stemexp_notes is None:
            return self.stemexp_notes
        else:
            return self.stemexp_notes[1:]


    def set_skills_biz_na(self, skills_biz_na):
        self.skills_biz_na = skills_biz_na
        return None

    def get_skills_biz_na(self):
        return self.skills_biz_na

    def set_skills_biz_sheets(self, skills_biz_sheets):
        self.skills_biz_sheets = skills_biz_sheets
        return None

    def get_skills_biz_sheets(self):
        return self.skills_biz_sheets

    def set_skills_biz_word(self, skills_biz_word):
        self.skills_biz_word = skills_biz_word
        return None

    def get_skills_biz_word(self):
        return self.skills_biz_word

    def set_skills_biz_slides(self, skills_biz_slides):
        self.skills_biz_slides = skills_biz_slides
        return None

    def get_skills_biz_slides(self):
        return self.skills_biz_slides

    def set_skills_biz_pm(self, skills_biz_pm):
        self.skills_biz_pm = skills_biz_pm
        return None

    def get_skills_biz_pm(self):
        return self.skills_biz_pm

    def set_skills_biz_speaking(self,skills_biz_speaking):
        self.skills_biz_speaking = skills_biz_speaking
        return None

    def get_skills_biz_speaking(self):
        return self.skills_biz_speaking

    def set_skills_biz_email(self, skills_biz_email):
        self.skills_biz_email = skills_biz_email
        return None

    def get_skills_biz_email(self):
        return self.skills_biz_email


    def set_skills_ed_secondary(self, skills_ed_secondary):
        self.skills_ed_secondary = skills_ed_secondary
        return None

    def get_skills_ed_secondary(self):
        return self.skills_ed_secondary

    def set_skills_ed_adult(self, skills_ed_adult):
        self.skills_ed_adult =skills_ed_adult
        return None

    def get_skills_ed_adult(self):
        return self.skills_ed_adult

    def set_skills_ed_elem(self, skills_ed_elem):
        self.skills_ed_elem = skills_ed_elem
        return None

    def get_skills_ed_elem(self):
        return self.skills_ed_elem

    def set_skills_ed_curriculum(self, skills_ed_curriculum):
        self.skills_ed_curriculum = skills_ed_curriculum
        return None

    def get_skills_ed_curriculum(self):
        return self.skills_ed_curriculum

    def set_skills_other(self, skills_other):
        self.skills_other = skills_other
        return None

    def get_skills_other(self):
        return self.skills_other

    def set_skills_biz_notes(self, skills_biz_notes):
        if self.skills_biz_notes is None:
            self.skills_biz_notes = ""
        self.skills_biz_notes = self.skills_biz_notes + ":" + skills_biz_notes
        return None


    def get_skills_biz_notes(self):
        if self.skills_biz_notes is None:
            return self.skills_biz_notes
        else:
            return self.skills_biz_notes[1:]

    def set_style_driven(self, style_driven):
        self.style_driven = style_driven

    def get_style_driven(self):
        return self.style_driven

    def set_style_collab(self, style_collab):
        self.style_collab = style_collab

    def get_style_collab(self):
        return self.style_collab

    def set_style_creative(self, style_creative):
        self.style_creative = style_creative

    def get_style_creative(self):
        return self.style_creative

    def set_style_investigate(self, style_investigate):
        self.style_investigate = style_investigate

    def get_style_investigate(self):
        return self.style_investigate

    def set_style_task(self, style_task):
        self.style_task = style_task

    def get_style_task(self):
        return self.style_task

    def set_style_ambiguity(self, style_ambiguity):
        self.style_ambiguity = style_ambiguity

    def get_style_ambiguity(self):
        return self.style_ambiguity

    def set_style_organized(self, style_organized):
        self.style_organized = style_organized

    def get_style_organized(self):
        return self.style_organized

    def set_style_direction(self, style_direction):
        self.style_direction = style_direction

    def get_style_direction(self):
        return self.style_direction

    def set_style_networker(self, style_networker):
        self.style_networker = style_networker

    def get_style_networker(self):
        return self.style_networker

    def set_style_structured(self, style_structured):
        self.style_structured = style_structured

    def get_style_structured(self):
        return self.style_structured

    def set_style_teamlead(self, style_teamlead):
        self.style_teamlead = style_teamlead

    def get_style_teamlead(self):
        return self.style_teamlead

    def set_style_other(self, style_other):
        self.style_other = style_other

    def get_style_other(self):
        return self.style_other

    def set_style_notes(self, style_notes):
        if self.style_notes is None:
            self.style_notes = ""
        self.style_notes = self.style_notes + ":" + style_notes
        return None

    def get_style_notes(self):
        if self.style_notes is None:
            return self.style_notes
        else:
            return self.style_notes[1:]

    def __str__(self):
        out_str = ""
        out_str = out_str + f"{self.stemexp_na}"
        out_str = out_str + f"{self.stemexp_lifesci}"
        out_str = out_str + f"{self.stemexp_chem}"
        out_str = out_str + f"{self.stemexp_phys}"
        out_str = out_str + f"{self.stemexp_math}"
        out_str = out_str + f"{self.stemexp_compsci}"
        out_str = out_str + f"{self.stemexp_it}"
        out_str = out_str + f"{self.stemexp_ag}"
        out_str = out_str + f"{self.stemexp_eng}"
        out_str = out_str + f"{self.stemexp_health}"
        out_str = out_str + f"{self.stemexp_trade}"
        out_str = out_str + f"{self.stemexp_env}"
        out_str = out_str + f"{self.stemexp_other}"


        out_str = out_str + f"{self.skills_biz_na}"
        out_str = out_str + f"{self.skills_biz_sheets}"
        out_str = out_str + f"{self.skills_biz_word}"
        out_str = out_str + f"{self.skills_biz_slides}"
        out_str = out_str + f"{self.skills_biz_pm}"
        out_str = out_str + f"{self.skills_biz_speaking}"
        out_str = out_str + f"{self.skills_biz_email}"
        out_str = out_str + f"{self.skills_ed_secondary}"
        out_str = out_str + f"{self.skills_ed_adult}"
        out_str = out_str + f"{self.skills_ed_elem}"
        out_str = out_str + f"{self.skills_ed_curriculum}"
        out_str = out_str + f"{self.skills_other}"


        out_str = out_str + f"{self.style_driven}"
        out_str = out_str + f"{self.style_collab}"
        out_str = out_str + f"{self.style_creative}"
        out_str = out_str + f"{self.style_investigate}"
        out_str = out_str + f"{self.style_task}"
        out_str = out_str + f"{self.style_ambiguity}"
        out_str = out_str + f"{self.style_organized}"
        out_str = out_str + f"{self.style_direction}"
        out_str = out_str + f"{self.style_networker}"
        out_str = out_str + f"{self.style_structured}"
        out_str = out_str + f"{self.style_teamlead}"
        out_str = out_str + f"{self.style_other}"

        return out_str




