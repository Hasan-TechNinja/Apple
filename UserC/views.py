from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from . forms import usercf
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect

def userCreationForm(request):
    if request.method == "POST":
        userCF = usercf(request.POST)
        if userCF.is_valid():
            userCF.save()
            return HttpResponseRedirect('/')
            # return render(request, 'user/login.html')
    else:
        userCF = usercf()
    return render(request, 'user/userCreation.html', {'form': userCF})

def login_form(request):
    if request.method == 'POST':
        frm = AuthenticationForm(request=request, data = request.POST)
        if frm.is_valid():
            uname = frm.cleaned_data['username']
            upas = frm.cleaned_data['password']
            user = authenticate(username = uname, password = upas)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/success/')
    else:
        frm = AuthenticationForm
        # return HttpResponse('Password dose not matched')
    return render(request, 'user/login.html', {'form': frm})

def s_login(request):
    # return HttpResponse('password dose not matched')
    return render(request, 'home/home.html')

def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/')