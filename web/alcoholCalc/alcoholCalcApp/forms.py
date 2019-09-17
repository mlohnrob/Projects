from django import forms


class AlcForm(forms.Form):
    volume = forms.FloatField(label="Mængde af alkohol i liter:")
    percent = forms.FloatField(label="Procent af alkohol:")


class burningRateForm(forms.Form):
    mass = forms.FloatField(label="Din Vægt:")
    numOfDrinks = forms.IntegerField(label="Antal genstande drukket:", required=False)


class CharmeIndexForm(forms.Form):
    sex = forms.ChoiceField(choices=[("male", "Mand"), ("female", "Kvinde")], label="Køn:")
    drinks = forms.IntegerField(label="Antal genstande:")
    mass = forms.FloatField(label="Din vægt:")
    hours = forms.IntegerField(label="Antal timer:")
    minutes = forms.IntegerField(label="Antal minutter:", required=False)


class CreateUserForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput())


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput())
