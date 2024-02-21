from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
from . models import info

# Create your views here.
def home(request):
    return render(request, 'mac/mac.html')

def show_form(request):
    if request.method == 'POST':
        frm = StudentRegistration(request.POST)
        if frm.is_valid():
            fn = frm.cleaned_data['f_name']
            ln = frm.cleaned_data['last_name']
            pas = frm.cleaned_data['password']
            rpas = frm.cleaned_data['re_password']
            eml = frm.cleaned_data['email']
            btc = frm.cleaned_data['batch']

            hasan = info(f_name = fn, last_name = ln, password = pas, re_password = rpas, email = eml, batch = btc)
            hasan.save()
            


            return HttpResponseRedirect('/mac/successfully/')
    else:

        frm = StudentRegistration()
        print('GET method working')
    return render(request, 'mac/forms.html', {'form': frm})

def succes(request):
    return render(request, 'mac/succes.html')