from django.shortcuts import render
from phone.models import Phone, Student

# Create your views here.
def home(request):
    return render(request, "phone/phone.html")

def price(request):
    prs = Phone.objects.all()
    return render(request, 'phone/price.html', {'prc':prs} )

def student(request):
    st = Student.objects.all()
    return render(request, 'phone/student.html', {'std':st})