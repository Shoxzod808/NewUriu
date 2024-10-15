from django import forms
from .models import Contact

class QabulForm(forms.Form):
    full_name = forms.CharField(label="To'liq ismi", max_length=255)
    passport = forms.CharField(label='Passport seriyasi', max_length=20)
    viloyat = forms.CharField(label='Viloyat', max_length=255)
    tuman = forms.CharField(label='Tuman', max_length=255)
    mfy = forms.CharField(label='MFY', max_length=255)
    kucha = forms.CharField(label='Kucha', max_length=255)
    uy = forms.CharField(label='Uy', max_length=255)
    phone_number = forms.CharField(label='Telefon raqami', max_length=15)
    
    birthday = forms.DateField(label="Tug'gilgan kuni", widget=forms.DateInput(attrs={'type': 'date'}))
    school = forms.CharField(label='Tugatgan ta’lim muassasasi', max_length=255)
    attestat = forms.CharField(label="Diplom yoki attestat raqami: № ", max_length=255)
    languages = forms.CharField(label="Qaysi chet til(lar)ini o‘qigan", max_length=255)
    father = forms.CharField(label="Otasi", max_length=255)
    father_address = forms.CharField(label="Doimiy yashash manzili", max_length=255)
    father_job = forms.CharField(label="Doimiy ish joyi", max_length=255)
    father_phone_number = forms.CharField(label="Telefon raqami", max_length=15)
    
    mother = forms.CharField(label="Onasi", max_length=255)
    mother_address = forms.CharField(label="Doimiy yashash manzili", max_length=255)
    mother_job = forms.CharField(label="Doimiy ish joyi", max_length=255)
    mother_phone_number = forms.CharField(label="Telefon raqami", max_length=15)
    directions = forms.ChoiceField(
        label="Yo'nalish", 
        choices=[
            ("60110400 - Boshlang'ich ta'lim", "60110400 - Boshlang'ich ta'lim"),
            ("60220300 - Tarix", "60220300 - Tarix"),
            ("60230100 - Filoligiya va tillarni o'qitish(o'zbek tili)", "60230100 - Filoligiya va tillarni o'qitish(o'zbek tili)"),
            ("60230100 - Filoligiya va tillarni o'qitish(Ingliz tili)", "60230100 - Filoligiya va tillarni o'qitish(Ingliz tili)"),
            ("60230100 - Filoligiya va tillarni o'qitish(Rus tili)", "60230100 - Filoligiya va tillarni o'qitish(Rus tili)"),
            ("60410600 - Bank ishi", "60410600 - Bank ishi"),
            ("60410200 - Buxgalteriya hisobi", "60410200 - Buxgalteriya hisobi"),
            ("60610100 - Axborot tizimlari va texnologiyalar", "60610100 - Axborot tizimlari va texnologiyalar"),
            ("60410100 - Iqtisodiyot", "60410100 - Iqtisodiyot"),
            ("60310300 - Psixologiya", "60310300 - Psixologiya"),
            ("70220301 - Tarix", "70220301 -  Tarix"),
            ("70230101 - Lingvistika(o'zbek tili)", "70230101 -  Lingvistika(o'zbek tili)"),
            ("70230101 - Lingvistika(ingliz tili)", "70230101 -  Lingvistika(ingliz tili)"),
            ("70230101 - Lingvistika(rus tili)", "70230101 -  Lingvistika(rus tili)"),
        ],
    )
    education_type = forms.ChoiceField(
        label="Ta'lim shakli",
        choices=[
            ('Kunduzgi', 'Kunduzgi'),
            ('Sirtqi', 'Sirtqi'),
        ]
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone', 'directions', 'education_type']