from email import message
from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from lmsapp.models import Student,Login,Enquiry 
from studentapp.models import StuResponse
from .models import Program,Branch,Year,BookStore,IssueBook
from django.contrib import  messages

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,'adminhome.html',{'adminid':adminid})
    except KeyError:
        return redirect('lmsapp:login')
def adminlogout(request):
    try:
        del request.session['adminid'] 
        return redirect('lmsapp:login')
    except KeyError:
        return redirect('lmsapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewstudents(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            student=Student.objects.all()
            
            return render(request,'viewstudents.html',{'adminid':adminid,'student':student})
    except KeyError:
        return redirect('lmsapp:login')
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewenquiry(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            enq=Enquiry.objects.all()
            student=Student.objects.all()
            return render(request,'viewenquiry.html',{'adminid':adminid,'enq':enq})
    except KeyError:
        return redirect('lmsapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewfeedback(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            feed=StuResponse.objects.filter(responsetype='feedback')
            return render(request,'viewfeedback.html',{'adminid':adminid,'feed':feed})
    except KeyError:
        return redirect('lmsapp:login')  
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewcomplain(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            complain=StuResponse.objects.filter(responsetype='complain')
            return render(request,'viewcomplain.html',{'adminid':adminid,'complain':complain})
    except KeyError:
        return redirect('lmsapp:login')   
# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def addbook(request):
    try:
        if request.session['adminid']!=None:
            if request.method=="POST":
                bookid=request.POST['bookid']
                bookid="VIT-"+bookid
                isbno=request.POST['isbno']
                program=request.POST['program']
                branch=request.POST['branch']
                year=request.POST['year']
                subject=request.POST['subject']
                bookname=request.POST['bookname']
                authorname=request.POST['authorname']
                qty=request.POST['qty']
                book=BookStore(bookid=bookid,isbno=isbno,program=program,branch=branch,year=year,subject=subject,bookname=bookname,authorname=authorname,qty=qty)
                book.save()
                messages.success(request,'Book details are Added')
                
            adminid=request.session['adminid']
            program=Program.objects.all()
            branch=Branch.objects.all()
            year=Year.objects.all()
            
            return render(request,'addbook.html',locals())
    except KeyError:
        return redirect('lmsapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewbooks(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            book=BookStore.objects.all()
            return render(request,'viewbooks.html',locals())
    except KeyError:
        return redirect('lmsapp:login')
def deletebook(request,bookid):
    BookStore.objects.get(bookid=bookid).delete()
    return redirect('adminapp:viewbooks')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def issuebook(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            book=BookStore.objects.all()
            return render(request,'issuebook.html',locals())
    except KeyError:
        return redirect('lmsapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def issuebookUI(request,bookid):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            book=BookStore.objects.get(bookid=bookid)
            return render(request,'issuebookUI.html',locals())
    except KeyError:
        return redirect('lmsapp:login')  
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def issue(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            bookid=request.POST['bookid']
            isbno=request.POST['isbno']
            program=request.POST['program']
            branch=request.POST['branch']
            subject=request.POST['subject']
            bookname=request.POST['bookname']
            authorname=request.POST['authorname']
            rollno=request.POST['rollno']
            issuedate=request.POST['issuedate']
            duedate=request.POST['duedate']
            stu=Student.objects.get(rollno=rollno)
            name=stu.name
            year=stu.year
            status='pending'
            ib=IssueBook(bookid=bookid,isbno=isbno,program=program,branch=branch,subject=subject,bookname=bookname,authorname=authorname,rollno=rollno,name=name,year=year,issuedate=issuedate,duedate=duedate,status=status)
            ib.save()
            BookStore.objects.filter(bookid=bookid).update(qty=0)
            return redirect('adminapp:issuebook')
    except KeyError:
        return redirect('lmsapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewissuedbook(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            issue=IssueBook.objects.filter(status="pending")
            return render(request,'viewissuedbook.html',locals())
    except KeyError:
        return redirect('lmsapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def ret(request,id):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            IssueBook.objects.filter(id=id).update(status="return")
            bookid=IssueBook.objects.get(id=id).bookid
            BookStore.objects.filter(bookid=bookid).update(qty=1)
            return redirect('adminapp:viewissuedbook')
    except KeyError:
        return redirect('lmsapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def returnbook(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            book=IssueBook.objects.filter(status="return")
            return render(request,'returnbook.html',locals())
    except KeyError:
        return redirect('lmsapp:login')