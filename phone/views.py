from django.shortcuts import render
from phone.models import Phone, Student
from . forms import Student_registrations
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, "phone/phone.html")

def price(request):
    prs = Phone.objects.all()
    return render(request, 'phone/price.html', {'prc':prs} )

def student(request):
    st = Student.objects.all()
    return render(request, 'phone/student.html', {'std':st})

def student_reg(request):
    if request.method == 'POST':
        frm = Student_registrations(request.POST)
        if frm.is_valid():
            print("Post method")
            return HttpResponseRedirect('/successfully/')
    else:
        frm = Student_registrations()
        return render(request, 'courses/form.html', {'form': frm})

    # return render(request, "Teacher/registration.html", {'form': fm})
def success(request):
    return render(request, 'courses/submit.html')