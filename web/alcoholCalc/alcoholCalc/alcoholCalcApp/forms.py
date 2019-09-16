from django import forms

class AlcForm(forms.Form):
    V = forms.FloatField(label="Mængde af alkohol")
    P = forms.FloatField(label="Procent af alkohol")
    
