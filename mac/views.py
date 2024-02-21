from django.shortcuts import render
from . forms import StudentRegistration

# Create your views here.
def home(request):
    return render(request, 'mac/mac.html')

def show_form(request):
    frm = StudentRegistration()
    return render(request, 'courses/forms.html', {'form': frm})