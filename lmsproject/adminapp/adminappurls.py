from django.urls import path
from . import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('viewstudents/',views.viewstudents,name='viewstudents'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('viewcomplain/',views.viewcomplain,name='viewcomplain'),
    path('addbook/',views.addbook,name='addbook'),
    path('viewbooks/',views.viewbooks,name='viewbooks'),
    path('issuebook/',views.issuebook,name='issuebook'),
    path('deletebook/<bookid>',views.deletebook,name='deletebook'),
    path('issuebookUI/<bookid>',views.issuebookUI,name='issuebookUI'),
    path('viewissuedbook/',views.viewissuedbook,name='viewissuedbook'),
    path('issue/',views.issue,name='issue'),
    path('ret/<id>',views.ret,name='ret'),
    path('returnbook/',views.returnbook,name='returnbook'),
]