from django import forms

class AlcForm(forms.Form):
    V = forms.FloatField(label="Mængde af alkohol i liter:")
    P = forms.FloatField(label="Procent af alkohol:")


class CharmeIndexForm(forms.Form):
    sex = forms.ChoiceField(choices=[("male", "Mand"), ("female", "Kvinde")], label="Køn:")
    drinks = forms.IntegerField(label="Antal genstande:")
    mass = forms.FloatField(label="Vægt:")
    hours = forms.IntegerField(label="Antal timer:")
    minutes = forms.IntegerField(label="Antal minutter:", required=False)
