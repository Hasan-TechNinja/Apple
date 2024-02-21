from typing import Any
from django import forms

class StudentRegistration(forms.Form):
    # first_name = forms.ChoiceField()
    f_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    batch = forms.IntegerField()

    def clean(self):
        clean_data = super().clean()
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['re_password']

        if password_match != re_password_match:
            raise forms.ValidationError("Password dose not match")