from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='phone'),
    path('price/', views.price, name='price'),
    path('student/', views.student, name = 'student'),
]
