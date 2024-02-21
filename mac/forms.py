from django import forms

class StudentRegistration(forms.Form):
    first_name = forms.ChoiceField()
    last_name = forms.CharField()
    email = forms.EmailField()
    batch = forms.IntegerField()