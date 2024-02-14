from django.shortcuts import render
from . forms import Student

# Create your views here.
def home(request):
    return render(request, 'watch/watch.html')

def Students(request):
    fm = Student()
    # fm.order_fields(field_order=['Id', 'First_name', 'Last_name', 'Email', 'Date_of_birth'])
    return render(request, 'watch/Student.html', {"form": fm})