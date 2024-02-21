from django import forms

class Student_registrations(forms.Form):
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)
    Re_Password = forms.CharField(widget=forms.PasswordInput)