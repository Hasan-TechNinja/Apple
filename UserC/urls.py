from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usercf/', views.userCreationForm, name = 'userCF'),
    path('', views.login_form, name = 'login'),
    path('success/', views.s_login, name = 'success'),
    path('logout/', views.logout_form, name = 'logout'),

]
