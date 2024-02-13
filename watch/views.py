from django.shortcuts import render
from . forms import Student

# Create your views here.
def home(request):
    return render(request, 'watch/watch.html')

def Students(request):
    fm = Student()
    return render(request, 'watch/Student.html', {"form": fm})