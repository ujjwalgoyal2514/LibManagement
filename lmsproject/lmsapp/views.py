from django.shortcuts import render,redirect,reverse
from . models import Enquiry,Student,Login
from datetime import date 
from django.contrib import messages
from adminapp.models import Branch,Year,Program
from .smssender import sendsms
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,"index.html")

def aboutus(request):
    return render(request,"aboutus.html")

def registration(request):
    if request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        regdate=date.today()
        usertype='student'
        status='false'
        stu=Student(rollno=rollno,name=name,fname=fname,mname=mname,gender=gender,address=address,program=program,branch=branch,year=year,contactno=contactno,emailaddress=emailaddress,regdate=regdate,)
        log=Login(userid=rollno,password=password,usertype=usertype,status=status)
        stu.save()
        log.save()
        subject='Important Mail from SR Institute of Technology'
        msg=f'Hello {name} your registration is successful and your password is {password}'
        email_from=settings.EMAIL_HOST_USER
        send_mail(subject,msg,email_from,[emailaddress])
        messages.success(request,"Student Registration is Done")
    program=Program.objects.all()
    branch=Branch.objects.all()
    year=Year.objects.all()
    return render(request,"registration.html",locals())

def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        usertype=request.POST['usertype']
        try:
            obj=Login.objects.get(userid=userid,password=password,usertype=usertype)
            if obj.usertype=="student":
                request.session['rollno']=userid
                return redirect(reverse('studentapp:studentHome'))
                # messages.success(request,"Welcome Student")
            elif(obj.usertype=="admin"):
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
                # messages.success(request,"Welcome Admin")            # messages.success(request,'Valid User')
        except: 
            messages.success(request,'Invalid User')       
    return render(request,"login.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        sendsms(contactno)
        messages.success(request, 'Your Enquiry is submitted')
    return render(request,"contact.html")
