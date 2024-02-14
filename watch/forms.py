from django import forms

class Student(forms.Form):
    Id = forms.IntegerField()
    First_Name = forms.CharField(label='Enter your first name', label_suffix=' ')
    Last_Name = forms.CharField(initial='Hasan', disabled= True)
    Email = forms.EmailField()
    Password = forms.CharField(widget=forms.PasswordInput)
    Text_Area = forms.CharField(widget=forms.Textarea)
    File = forms.CharField(widget=forms.FileInput)
    Checkbox = forms.CharField(widget=forms.CheckboxInput)