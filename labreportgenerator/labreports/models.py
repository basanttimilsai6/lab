from django.db import models



class Hospital(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name



class Patient(models.Model):
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

    # AGE_CHOICES = (
    #     ('years', 'Years'),
    #     ('months', 'Months'),
    #     ('days', 'Days'),
    # )


    level = models.CharField(max_length=5, choices=LEVEL_CHOICES, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    age_time = models.CharField(max_length=10,choices=AGE_CHOICES,null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    refer_hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, blank=True)
    custom_date = models.CharField(max_length=10,null=True, blank=True)
    nhpc = models.CharField(max_length=5, choices=LEVEL_CHOICES, null=True, blank=True)


    def __str__(self):
        return f"Patient: {self.id}"


class Test(models.Model):
    RESULT_CHOICES = [
        ('POSITIVE', 'POSITIVE'),
        ('NEGATIVE', 'NEGATIVE'),
    ]
    RH_CHOICES = [
        ('POSITIVE', 'POSITIVE'),
        ('NEGATIVE', 'NEGATIVE'),
    ]
    ABO_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('O', 'O'),
        ('AB', 'AB'),
    ]
    bt = models.FloatField(max_length=10,null=True, blank=True,help_text="(2-7)Min)")
    ct = models.FloatField(max_length=10, null=True, blank=True, help_text="(5-11)Min")
    rdt_for_mp = models.CharField(max_length=10,null=True, blank=True,choices=RESULT_CHOICES)
    blood_group_abo_typing = models.CharField(max_length=10, null=True, blank=True, choices=ABO_CHOICES)
    blood_group_rh = models.CharField(max_length=10, null=True, blank=True, choices=RH_CHOICES)


    def __str__(self):
        return f"Extra: {self.id}"



class WidalTest(models.Model):
    RESULT_CHOICES = [
        ('NEGATIVE', 'NEGATIVE'),
        ('1:80', '1:80'),
        ('1:160', '1:160'),
        ('1:320', '1:320'),
    ]

    anti_o = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    anti_h = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    anti_ah = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    anti_bh = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Widal: {self.id}"


class Serology(models.Model):
    RESULT_CHOICES = [
        ('POSITIVE', 'POSITIVE'),
        ('NEGATIVE', 'NEGATIVE'),
    ]

    hbsag = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    hiv_1_2_ab = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    vdrl_rpr = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    hiv_i_ii = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    hcv = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    crp = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    aso = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    ra = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    typhoid_igg_igm = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    dengue_ns1_ag = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    dengue_igg_igm = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    scrub_typhus_igg_igm = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    h_pylori_igg_igm = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES,
        null=True,
        blank=True,
    )

    sputum_for_afb_i = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    sputum_for_afb_ii = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    mantoux = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    diameter_after_48_72_hrs = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Serology:{self.id}"


class Biochemistry(models.Model):
    sugar_f = models.FloatField(help_text="(70-110) mg/dl", null=True, blank=True)
    sugar_pp = models.FloatField(help_text="(70-140) mg/dl", null=True, blank=True)
    sugar_r = models.FloatField(help_text="(70-140) mg/dl", null=True, blank=True)
    serum_urea = models.FloatField(help_text="(10-45) mg/dl", null=True, blank=True)
    creatine = models.FloatField(help_text="(0.5-1.5) mg/dl", null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    uric_acid = models.FloatField(help_text="(2-7) mg/dl", null=True, blank=True)
    s_calcium = models.FloatField(help_text="(8.5-11) mg/dl", null=True, blank=True)

    def __str__(self):
        return f"Bio-C:{self.id}"

class Hematology(models.Model):
    HB = models.FloatField(help_text="(12-16) gm/dl", null=True, blank=True)
    total_count = models.FloatField(help_text="(4000-11000) /mm³", null=True, blank=True)
    neutrophils = models.FloatField(help_text="(45-70) %", null=True, blank=True)
    lymphocytes = models.FloatField(help_text="(20-40) %", null=True, blank=True)
    monocytes = models.FloatField(help_text="(2-10) %", null=True, blank=True)
    eosinophils = models.FloatField(help_text="(2-6) %", null=True, blank=True)
    basophils = models.FloatField(help_text="(0-1) %", null=True, blank=True)
    RBC = models.FloatField(help_text="(4.5-5) * 10⁵ /mm³", null=True, blank=True)
    platelets = models.FloatField(help_text="(1.5-3) * 10⁵ /mm³", null=True, blank=True)
    ESR = models.FloatField(help_text="(0-20) mm/hr", null=True, blank=True)
    PCV = models.FloatField(help_text="(36-54) %", null=True, blank=True)
    MCV = models.FloatField(help_text="(82-92) fl", null=True, blank=True)
    MCH = models.FloatField(help_text="(27-36) pg", null=True, blank=True)
    MCHC = models.FloatField(help_text="(32-36) %", null=True, blank=True)
    test=models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate LDL and VLDL cholesterol based on other values
        if self.neutrophils is not None and self.lymphocytes is not None and self.monocytes is not None and self.eosinophils is not None and self.basophils is not None:
            self.test = self.neutrophils + self.lymphocytes + self.monocytes + self.eosinophils + self.basophils
        super(Hematology, self).save(*args, **kwargs)
    

    def __str__(self):
        return f"Hematology: {self.id}"


class Urine(models.Model):
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

    color = models.CharField(max_length=20,choices=COLOR_CHOICES,null=True,blank=True)
    appearance = models.CharField(max_length=20,choices=APPEARANCE_CHOICES,null=True,blank=True)
    reaction = models.CharField(max_length=10,choices=REACTION_CHOICES,null=True,blank=True)
    sugar = models.CharField(max_length=10,choices=SUGAR_CHOICES,null=True,blank=True)
    protein = models.CharField(max_length=10,choices=PROTEIN_CHOICES,null=True,blank=True,)
    rbc = models.CharField(max_length=10,null=True,blank=True,help_text="/HPF")
    pus_cells = models.CharField(max_length=10,null=True,blank=True,help_text="/HPF")
    epithelial_cells = models.CharField(max_length=10,null=True,blank=True,help_text="/HPF")
    calcium_oxalates = models.CharField(max_length=10,null=True,blank=True,help_text="/HPF")
    crystals = models.CharField(max_length=10,null=True,blank=True,help_text="/HPF")
    casts = models.CharField(max_length=10,null=True,blank=True,help_text="/HPF")
    bacteria = models.CharField(max_length=10,null=True,blank=True,help_text="/HPF")
    others = models.CharField(max_length=10,null=True,blank=True,help_text="/HPF")

    def __str__(self):
        return f"Urine:{self.id}"



class LiverFunctionTest(models.Model):
    total_bilirubin = models.FloatField(help_text="(0.2-1) mg/dl", null=True, blank=True)
    direct = models.FloatField(help_text="Up to 0.4 mg/dl", null=True, blank=True)
    indirect = models.FloatField(help_text="Up to 0.4 mg/dl", null=True, blank=True)
    sgpt = models.FloatField(help_text="(3-35) U/L", null=True, blank=True)
    sgot = models.FloatField(help_text="(5-40) U/L", null=True, blank=True)
    alkaline_phosphatase = models.FloatField(help_text="<306 U/L", null=True, blank=True)
    total_protein = models.FloatField(help_text="(6-8) g/dl", null=True, blank=True)
    a_g_ratio = models.FloatField(help_text="(1.2-1.8) gm/dl", null=True, blank=True)
    serum_albumin = models.FloatField(help_text="(3.2-4.6) g/dl", null=True, blank=True)
    globulin=models.FloatField(help_text="(3.2-4.6) g/dl", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.total_bilirubin is not None and self.direct is not None:
            self.indirect = self.total_bilirubin - self.direct
        super(LiverFunctionTest, self).save(*args, **kwargs)

    def __str__(self):
        return f"Liver{self.id}"
    

class LipidProfile(models.Model):
    triglyceride = models.FloatField(help_text="(<200) mg/dL", null=True, blank=True)
    t_cholesterol = models.FloatField(help_text="(<200) mg/dL", null=True, blank=True)
    hdl_cholesterol = models.FloatField(help_text="(30-70) mg/dL", null=True, blank=True)
    ldl_cholesterol = models.FloatField(help_text="(up to 150) mg/dL", null=True, blank=True)
    vldl_cholesterol = models.FloatField(help_text="(3-32) mg/dL", null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate LDL and VLDL cholesterol based on other values
        if self.triglyceride is not None and self.t_cholesterol is not None and self.hdl_cholesterol is not None:
            self.vldl_cholesterol = self.triglyceride / 5
            new_vldl = self.vldl_cholesterol
            self.ldl_cholesterol = self.t_cholesterol-new_vldl - self.hdl_cholesterol
        super(LipidProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"Lipid:{self.id}"
    

class Stool(models.Model):
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

    color = models.CharField(
        max_length=50,
        blank=True,
        help_text="Stool color"
    )

    consistency = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        null=True,
        blank=True,
        help_text="Stool consistency (loose, solid, semi-solid)"
    )

    blood = models.CharField(
        max_length=50,
        choices=BLOOD_CHOICES,
        null=True,
        blank=True,
        help_text="Blood presence (Present or Absent)"
    )

    mucus = models.CharField(
        max_length=50,
        choices=MUCUS_CHOICES,
        null=True,
        blank=True,
        help_text="Mucus presence (Present or Absent)"
    )

    pus_cells = models.CharField(
        max_length=50,
        blank=True,
        help_text="/HPF"
    )

    rbc = models.CharField(
        max_length=50,
        blank=True,
        help_text="/HPF"
    )

    ova = models.CharField(
        max_length=50,
        blank=True,
        help_text="/HPF"
    )
    cyst = models.CharField(max_length=50,blank=True,help_text="/HPF")
    worm = models.CharField(max_length=50,blank=True,help_text="/HPF")
    fat_globules = models.CharField(max_length=50,blank=True,help_text="/HPF")
    yeast_cells = models.CharField(max_length=50,blank=True,help_text="/HPF")
    undigested_food_particles = models.CharField(max_length=50,blank=True,help_text="/HPF")
    others = models.CharField(max_length=50,blank=True,help_text="/HPF")

    def __str__(self):
        return f"Stool:{self.id}"
    

class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hematology = models.OneToOneField(Hematology, on_delete=models.CASCADE, blank=True, null=True)
    urine = models.OneToOneField(Urine, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.OneToOneField(Biochemistry, on_delete=models.CASCADE, blank=True, null=True)
    lipid = models.OneToOneField(LipidProfile, on_delete=models.CASCADE, blank=True, null=True)
    test = models.OneToOneField(Test, on_delete=models.CASCADE, blank=True, null=True)
    widal = models.OneToOneField(WidalTest, on_delete=models.CASCADE, blank=True, null=True)
    sero = models.OneToOneField(Serology, on_delete=models.CASCADE, blank=True, null=True)
    stool = models.OneToOneField(Stool, on_delete=models.CASCADE, blank=True, null=True)
    liver = models.OneToOneField(LiverFunctionTest, on_delete=models.CASCADE, blank=True, null=True)
    
    

    def __str__(self):
        return f"Report:{self.patient}"