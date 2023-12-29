from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('contact/',views.contact,name='contact'),

]