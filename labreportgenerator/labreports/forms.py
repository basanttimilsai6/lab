from django import forms
from .models import *

import re
class CForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class UrineForm(forms.ModelForm):
    class Meta:
        model = Urine
        fields = '__all__'


    COLOR_CHOICES = [
        ('', ''),
        ('L.YELLOW', 'L.YELLOW'),
        ('D.YELLOW', 'D.YELLOW'),
        ('WATERY', 'WATERY'),
        ('YELLOWISH', 'YELLOWISH'),
        ('REDDISH', 'REDDISH'),
    ]

    APPEARANCE_CHOICES = [
        ('', ''),
        ('CLEAR', 'CLEAR'),
        ('S.TURBID', 'S.TURBID'),
        ('TURBID', 'TURBID'),
        ('CLOUDY', 'CLOUDY'),
    ]

    REACTION_CHOICES = [
        ('', ''),
        ('ACIDIC', 'ACIDIC'),
        ('ALKALINE', 'ALKALINE'),
    ]

    SUGAR_CHOICES = [
        ('', ''),
        ('NIL', 'NIL'),
        ('TRACE', 'TRACE'),
        ('1+', '1+'),
        ('2+', '2+'),
        ('3+', '3+'),
        ('4+', '4+'),
    ]

    PROTEIN_CHOICES = [
        ('', ''),
        ('NIL', 'NIL'),
        ('TRACE', 'TRACE'),
        ('1+', '1+'),
        ('2+', '2+'),
        ('3+', '3+'),
        ('4+', '4+'),
    ]

    color = forms.ChoiceField(label="Color", choices=COLOR_CHOICES, required=False)
    appearance = forms.ChoiceField(label="Appearance", choices=APPEARANCE_CHOICES, required=False)
    reaction = forms.ChoiceField(label="Reaction", choices=REACTION_CHOICES, required=False)
    sugar = forms.ChoiceField(label="Sugar", choices=SUGAR_CHOICES, required=False)
    protein = forms.ChoiceField(label="Protein", choices=PROTEIN_CHOICES, required=False)
    rbc = forms.CharField(label="RBC", max_length=10, required=False, help_text="/HPF")
    pus_cells = forms.CharField(label="PUS CELLS", max_length=10, required=False, help_text="/HPF")
    epithelial_cells = forms.CharField(label="Epithelial Cells", max_length=10, required=False, help_text="/HPF")
    calcium_oxalates = forms.CharField(label="Calcium Oxalates", max_length=10, required=False, help_text="/HPF")
    crystals = forms.CharField(label="Crystals", max_length=10, required=False, help_text="/HPF")
    casts = forms.CharField(label="Casts", max_length=10, required=False, help_text="/HPF")
    bacteria = forms.CharField(label="Bacteria", max_length=10, required=False, help_text="/HPF")
    others = forms.CharField(label="Others", max_length=10, required=False, help_text="/HPF")



class LipidProfileForm(forms.ModelForm):
    triglyceride = forms.FloatField(label="Triglyceride", help_text="(<200) mg/dL",required=False)
    t_cholesterol = forms.FloatField(label="T. Cholesterol",help_text="(<200) mg/dL",required=False)
    hdl_cholesterol = forms.FloatField(label="HDL-Cholesterol",help_text="(30-70) mg/dL",required=False)

    class Meta:
        model = LipidProfile
        fields = '__all__'



class LiverFunctionTestForm(forms.ModelForm):
    total_bilirubin = forms.FloatField(label="Total Bilirubin",help_text="(0.2-1) mg/dl",required=False)
    direct = forms.FloatField(label="Direct",help_text="Up to 0.4 mg/dl",required=False)
    sgpt = forms.FloatField(label="SGPT (ALT)",help_text="(3-35) U/L",required=False)
    sgot = forms.FloatField(label="SGOT (AST)",help_text="(5-40) U/L",required=False)
    alkaline_phosphatase = forms.FloatField(label="Alkaline Phosphatase",help_text="<306 U/L",required=False)
    total_protein = forms.FloatField(label="Total Protein",help_text="(6-8) g/dl",required=False)
    a_g_ratio = forms.FloatField(label="A/G Ratio",help_text="(1.2-1.8) gm/dl",required=False)
    serum_albumin = forms.FloatField(label="Serum Albumin",help_text="(3.2-4.6) g/dl",required=False)
    globulin = forms.FloatField(label="Globulin",help_text="(3.2-4.6) g/dl",required=False)

    class Meta:
        model = LiverFunctionTest
        fields = '__all__'

class BiochemistryForm(forms.ModelForm):

    class Meta:
        model = Biochemistry
        fields = '__all__'
    
    sugar_f = forms.FloatField(label="Sugar (F)",help_text="(70-110) mg/dl",required=False)
    sugar_pp = forms.FloatField(label="Sugar (PP)",help_text="(70-140) mg/dl",required=False)
    sugar_r = forms.FloatField(label="Sugar (R)",help_text="(70-140) mg/dl",required=False)
    serum_urea = forms.FloatField(label="Serum Urea",help_text="(10-45) mg/dl",required=False)
    creatine = forms.FloatField(label="Creatine",help_text="(0.5-1.5) mg/dl",required=False)
    sodium = forms.FloatField(label="SODIUM",help_text="(0.5-1.5) mg/dl",required=False)
    potassium = forms.FloatField(label="POTASSIUM",help_text="(0.5-1.5) mg/dl",required=False)
    uric_acid = forms.FloatField(label="Uric Acid",help_text="(2-7) mg/dl",required=False)
    s_calcium = forms.FloatField(label="S. Calcium",help_text="(8.5-11) mg/dl",required=False)

    



class HematologyForm(forms.ModelForm):
    class Meta:
        model = Hematology
        fields = '__all__'

    HB = forms.FloatField(label="Hemoglobin (gm/dl)",help_text="(12-16) gm/dl",required=False)
    total_count = forms.FloatField(label="Total Count (/mm³)",help_text="(4000-11000) /mm³",required=False)
    neutrophils = forms.FloatField(label="Neutrophils (%)",help_text="(45-70) %",required=False)
    lymphocytes = forms.FloatField(label="Lymphocytes (%)",help_text="(20-40) %",required=False)
    monocytes = forms.FloatField(label="Monocytes (%)",help_text="(2-10) %",required=False)
    eosinophils = forms.FloatField(label="Eosinophils (%)",help_text="(2-6) %",required=False)
    basophils = forms.FloatField(label="Basophils (%)",help_text="(0-1) %",required=False)
    RBC = forms.FloatField(label="Red Blood Cell Count (/mm³)",help_text="(4.5-5) * 10^5 /mm³",required=False)
    platelets = forms.FloatField(label="Platelet Count (/mm³)",help_text="(1.5-3) * 10^5 /mm³",required=False)
    ESR = forms.FloatField(label="ESR (mm/hr)",help_text="(0-20) mm/hr",required=False)
    PCV = forms.FloatField(label="PCV (%)",help_text="(36-54) %",required=False)
    MCV = forms.FloatField(label="MCV (fl)",help_text="(82-92) fl",required=False)
    MCH = forms.FloatField(label="MCH (pg)",help_text="(27-36) pg",required=False)
    MCHC = forms.FloatField(label="MCHC (%)",help_text="(32-36) %",required=False)






class PatientForm(forms.ModelForm):
    LEVEL_CHOICES = [
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Ms.', 'Ms.'),
        ('Miss', 'Miss'),
    ]

    SEX_CHOICES = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHERS', 'OTHERS'),
    ]

    AGE_CHOICES = [
        ('YRS', 'YRS'),
        ('MONTHS', 'MONTHS'),
        ('DAYS', 'DAYS'),
    ]

    level = forms.ChoiceField(
        label="Level",
        choices=LEVEL_CHOICES,
        required=False
    )

    name = forms.CharField(
        label="Name",
        max_length=255,
        required=False
    )

    sex = forms.ChoiceField(
        label="Sex",
        choices=SEX_CHOICES,
        required=False
    )

    age = forms.IntegerField(
        label="Age",
        required=False
    )

    age_time = forms.ChoiceField(
        label="Age Time",
        choices=AGE_CHOICES,
        required=False
    )

    custom_date = forms.CharField(
        max_length=10,
        label='Date',
        widget=forms.TextInput(attrs={'placeholder': 'XXXX/XX/XX'}),
    )

    address = forms.CharField(
        label="Address",
        max_length=255,
        required=False
    )

    email = forms.EmailField(
        label="Email",
        required=False
    )

    phone = forms.CharField(
        label="Phone",
        max_length=15,
        required=False
    )

    nhpc = forms.CharField(
        label="NHPC NO:",
        max_length=10,
        required=False
    )

    date_pattern = re.compile(r'^\d{4}/\d{2}/\d{2}$')
    def clean_custom_date(self):
        custom_date = self.cleaned_data.get('custom_date')
        if not self.date_pattern.match(custom_date):
            raise forms.ValidationError("Invalid date format. Please use the format XXXX/XX/XX.")
        return custom_date

    class Meta:
        model = Patient
        fields = '__all__'



class SerologyForm(forms.ModelForm):
    RESULT_CHOICES = [
        ('', ''),
        ('POSITIVE', 'POSITIVE'),
        ('NEGATIVE', 'NEGATIVE'),
    ]

    hbsag = forms.ChoiceField(
        label="HBsAg",
        choices=RESULT_CHOICES,
        required=False
    )

    hiv_1_2_ab = forms.ChoiceField(
        label="HIV 1/2 AB",
        choices=RESULT_CHOICES,
        required=False
    )

    vdrl_rpr = forms.ChoiceField(
        label="VDRL/RPR",
        choices=RESULT_CHOICES,
        required=False
    )

    hiv_i_ii = forms.ChoiceField(
        label="HIV I/II",
        choices=RESULT_CHOICES,
        required=False
    )

    hcv = forms.ChoiceField(
        label="HCV",
        choices=RESULT_CHOICES,
        required=False
    )

    crp = forms.ChoiceField(
        label="CRP",
        choices=RESULT_CHOICES,
        required=False
    )

    aso = forms.ChoiceField(
        label="ASO",
        choices=RESULT_CHOICES,
        required=False
    )

    ra = forms.ChoiceField(
        label="RA",
        choices=RESULT_CHOICES,
        required=False
    )

    typhoid_igg_igm = forms.ChoiceField(
        label="Typhoid IgG/IgM",
        choices=RESULT_CHOICES,
        required=False
    )

    dengue_ns1_ag = forms.ChoiceField(
        label="Dengue NS1 Ag",
        choices=RESULT_CHOICES,
        required=False
    )

    dengue_igg_igm = forms.ChoiceField(
        label="Dengue IgG/IgM",
        choices=RESULT_CHOICES,
        required=False
    )

    scrub_typhus_igg_igm = forms.ChoiceField(
        label="Scrub Typhus IgG/IgM",
        choices=RESULT_CHOICES,
        required=False
    )

    h_pylori_igg_igm = forms.ChoiceField(
        label="H. Pylori IgG/IgM",
        choices=RESULT_CHOICES,
        required=False
    )

    sputum_for_afb_i = forms.CharField(
        label="Sputum For AFB I",
        max_length=10,
        required=False
    )

    sputum_for_afb_ii = forms.CharField(
        label="Sputum For AFB II",
        max_length=10,
        required=False
    )

    mantoux = forms.CharField(
        label="Mantoux",
        max_length=10,
        required=False
    )

    diameter_after_48_72_hrs = forms.CharField(
        label="Diameter after 48-72 hrs",
        max_length=10,
        required=False
    )

    class Meta:
        model = Serology
        fields = '__all__'




class WidalTestForm(forms.ModelForm):
    RESULT_CHOICES = [
        ('', ''),
        ('NEGATIVE', 'NEGATIVE'),
        ('1:80', '1:80'),
        ('1:160', '1:160'),
        ('1:320', '1:320'),
    ]

    anti_o = forms.ChoiceField(
        label="S.TYPHI 'O'",
        choices=RESULT_CHOICES,
        required=False
    )

    anti_h = forms.ChoiceField(
        label="S.TYPHI 'H'",
        choices=RESULT_CHOICES,
        required=False
    )

    anti_ah = forms.ChoiceField(
        label="S.PARATYPHI 'AH'",
        choices=RESULT_CHOICES,
        required=False
    )

    anti_bh = forms.ChoiceField(
        label="S.PARATYPHI 'BH'",
        choices=RESULT_CHOICES,
        required=False
    )

    class Meta:
        model = WidalTest
        fields = '__all__'



class StoolForm(forms.ModelForm):
    COLOR_CHOICES = [
        ('', ''),
        ('LOOSE', 'LOOSE'),
        ('SOLID', 'SOLID'),
        ('SEMI-SOLID', 'SEMI-SOLID'),
    ]

    BLOOD_CHOICES = [
        ('', ''),
        ('PRESENT', 'PRESENT'),
        ('ABSENT', 'ABSENT'),
    ]

    MUCUS_CHOICES = [
        ('', ''),
        ('PRESENT', 'PRESENT'),
        ('ABSENT', 'ABSENT'),
    ]

    color = forms.CharField(label="Color",max_length=50,required=False)
    consistency = forms.ChoiceField(label="Consistency",choices=COLOR_CHOICES,required=False)
    blood = forms.ChoiceField(label="Blood",choices=BLOOD_CHOICES,required=False)
    mucus = forms.ChoiceField(label="Mucus",choices=MUCUS_CHOICES,required=False)
    pus_cells = forms.CharField(label="Pus Cells",max_length=50,required=False,help_text="/HPF")
    rbc = forms.CharField(label="RBC",max_length=50,required=False,help_text="/HPF")
    ova = forms.CharField(label="Ova",max_length=50,required=False,help_text="/HPF")
    cyst = forms.CharField(label="Cyst",max_length=50,required=False,help_text="/HPF")
    worm = forms.CharField(label="Worm",max_length=50,required=False,help_text="/HPF")
    fat_globules = forms.CharField(label="Fat Globules",max_length=50,required=False,help_text="/HPF")
    yeast_cells = forms.CharField(label="Yeast Cells",max_length=50,required=False,help_text="/HPF")
    undigested_food_particles = forms.CharField(label="Undigested Food Particles",max_length=50,required=False,help_text="/HPF")
    others = forms.CharField(label="Others",max_length=50,required=False,help_text="/HPF")

    class Meta:
        model = Stool
        fields = '__all__'



class TestForm(forms.ModelForm):
    RESULT_CHOICES = [
        ('', ''),
        ('POSITIVE', 'POSITIVE'),
        ('NEGATIVE', 'NEGATIVE'),
    ]
    RH_CHOICES = [
        ('', ''),
        ('POSITIVE', 'POSITIVE'),
        ('NEGATIVE', 'NEGATIVE'),
    ]
    ABO_CHOICES = [
        ('', ''),
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB'),
    ]

    bt = forms.FloatField(label="BT",required=False,help_text="(2-7) Min")
    ct = forms.FloatField(label="CT",required=False,help_text="(5-11) Min")
    rdt_for_mp = forms.ChoiceField(label="RDT for MP",choices=RESULT_CHOICES,required=False,)
    blood_group_abo_typing = forms.ChoiceField(label="Blood Group ABO Typing",choices=ABO_CHOICES,required=False,)
    blood_group_rh = forms.ChoiceField(label="Blood Group RH",choices=RH_CHOICES,required=False,)

    class Meta:
        model = Test
        fields = '__all__'