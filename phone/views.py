from django.shortcuts import render
from phone.models import Phone

# Create your views here.
def home(request):
    return render(request, "phone/phone.html")

def price(request):
    prs = Phone.objects.all()
    return render(request, 'phone/price.html', {'prc':prs} )