from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="mac"),
    path('show_form/', views.show_form, name = 'sform'),
]
