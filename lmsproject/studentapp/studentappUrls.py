from django.urls import path
from . import views

urlpatterns=[
    
    path('studenthome/',views.studentHome,name='studentHome'),
    path('studentlogout/',views.studentlogout,name='studentlogout'),
    path('response/',views.response,name='response'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('viewstudentbook/',views.viewstudentbook,name="viewstudentbook"),
]