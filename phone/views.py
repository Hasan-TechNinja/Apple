from django.shortcuts import render
from phone.models import Phone, Student
from . forms import Teacher_registrations

# Create your views here.
def home(request):
    return render(request, "phone/phone.html")

def price(request):
    prs = Phone.objects.all()
    return render(request, 'phone/price.html', {'prc':prs} )

def student(request):
    st = Student.objects.all()
    return render(request, 'phone/student.html', {'std':st})

def teacher_reg(request):
    fm = Teacher_registrations()
    return render(request, "Teacher/registration.html", {'form': fm})