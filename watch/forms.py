from django import forms

class Student(forms.Form):
    Id = forms.IntegerField()
    First_Name = forms.CharField()
    Last_Name = forms.CharField()
    Email = forms.EmailField()
    Date_of_birth = forms.DateField()