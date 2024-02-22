from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def userCreationForm(request):
    userC = UserCreationForm()
    return render(request, 'user/userCreation.html', {'form': userC})