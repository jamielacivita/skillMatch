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


