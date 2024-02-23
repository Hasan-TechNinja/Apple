from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from . forms import usercf
from django.http import HttpResponse

def userCreationForm(request):
    if request.method == "POST":
        userCF = usercf(request.POST)
        if userCF.is_valid():
            userCF.save()
            return HttpResponse("This form successfully submitted")
            # return render(request, '****************')
    else:
        userCF = usercf()
    return render(request, 'user/userCreation.html', {'form': userCF})
