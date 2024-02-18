from django import forms

class Teacher_registrations(forms.Form):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    Email = forms.EmailField()
    Pas = forms.PasswordInput()
    v_Pas = forms.PasswordInput()