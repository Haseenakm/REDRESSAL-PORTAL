from django.shortcuts import render,redirect

from app1.models import tbl_account
from app1.models import tbl_parentreg
from app1.models import tbl_studentreg
from app1.models import tbl_login
from app1.models import tbl_idgen
from app1.models import tbl_complaint
from app1.models import tbl_complaint1

from app1.models import tbl_action
from app1.models import tbl_policeaction
from app1.models import tbl_welfareactn
from app1.models import tbl_notification
from app1.models import tbl_awareness


from django.http import HttpResponse
def index(request):  
    return render(request,"index.html")
def login(request):

    return render(request,"login.html")
def admin_header(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"admin_header.html")
def admin1(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"admin.html")
def police1(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"police.html")
def welfare1(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"welfare.html")
def counciler1(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"counciler.html")
def student1(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"student.html")
def parent1(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"parent.html")

def public_header(request):
    return render(request,"public_header.html")
def student_header(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"student_header.html")
def parent_header(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"parent_header.html")
def counciler_header(request): 
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        return render(request,"counciler_header.html")
def police_header(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"police_header.html")
def welfare_header(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:   
        return render(request,"welfare_header.html")
def parent_registration(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else: 
        data1=tbl_studentreg.objects.get(id=id) 
        data=tbl_idgen.objects.get(id=1)
        f=data.parent_id
        f=f+1
        f1="PARENT"+str(f)
        request.session['P_ID']=f
        return render(request,'parent_registration.html',{'ff':f1,'data':data1})
    
def complaint_registration(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:
        data=tbl_idgen.objects.get(id=1)
        f=data.complaint_id
        f=f+1
        f1="CMPLT"+str(f)
        request.session['C_ID']=f
        sid=request.session['uid']
        return render(request,'complaint_registration.html',{'ff':f1,'sid':sid})

def complaints(request):
    if request.method == "POST":
        data = tbl_complaint()
        data.complaint_id=request.POST.get('complaint_id')
        data.category=request.POST.get('category')
        data.student_id=request.POST.get('student_id')
        data.complaint=request.POST.get('complaint')
        data.complaint_dt=request.POST.get('complaint_dt')
        data.accused=request.POST.get('accused')
        data.accused_dt=request.POST.get('accused_dt')
        data.remarks=request.POST.get('remarks')
        data.status="pending"
        data.save()
        items=tbl_login()
        s=request.session['C_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.complaint_id=s
        data2.save()
       
    return redirect('/complaint_registration')
def complaint_registration1(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        data=tbl_idgen.objects.get(id=1)
        f=data.complaint_id
        f=f+1
        f1="COMPLT"+str(f)
        request.session['CM_ID']=f
        sid=request.session['uid']
        data=tbl_parentreg.objects.get(parent_id=sid)
        student_id=data.student_id
        return render(request,'complaint_registration1.html',{'ff':f1,'sid':student_id})
def complaints1(request):
    if request.method == "POST":
        data = tbl_complaint()
        data.complaint_id=request.POST.get('complaint_id')
        data.category=request.POST.get('category')
        data.student_id=request.POST.get('student_id')
        data.complaint=request.POST.get('complaint')
        data.complaint_dt=request.POST.get('complaint_dt')
        data.accused=request.POST.get('accused')
        data.accused_dt=request.POST.get('accused_dt')
        data.remarks=request.POST.get('remarks')
        data.status="pending"
        data.save()
        items=tbl_login()
        s=request.session['CM_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.complaint_id=s
        data2.save()
       
    return redirect('/complaint_registration1')

def complaint(request): 
    if 'uid' not in request.session:
            return render(request,"login.html")
    else: 
        items = tbl_complaint.objects.filter(status='pending') 
        return render(request,"complaint.html",{'ct':items})

def view_action(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        sid=request.session['uid']
        data=tbl_parentreg.objects.get(parent_id=sid)
        sid1=data.student_id
        items = tbl_complaint.objects.exclude(status="pending").exclude(status="adminverified").filter(student_id=sid1) 
        return render(request,"view_action.html",{'ct':items})

def view_action1(request,id,id1):
    if id1=="welfare_completed":

        items = tbl_welfareactn.objects.get(complaint_id=id)
        return render(request,"view_action1.html",{'ct':items})
    else:
        items=tbl_policeaction.objects.get(complaint_id=id)    
        return render(request,"view_action2.html",{'ct':items})
def studentview_action(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_complaint.objects.exclude(status="pending").exclude(status="adminverified").filter(student_id=request.session['uid']) 
        return render(request,"studentview_action.html",{'ct':items})

def studentview_action1(request,id,id1):
    if id1=="welfare_completed":

        items = tbl_welfareactn.objects.get(complaint_id=id)
        return render(request,"studentview_action1.html",{'ct':items})
    else:
        items=tbl_policeaction.objects.get(complaint_id=id)    
        return render(request,"studentview_action2.html",{'ct':items})
def counciler_viewaction(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_complaint.objects.exclude(status="pending").exclude(status="adminverified") 
        return render(request,"counciler_viewaction.html",{'ct':items})

def counciler_viewaction1(request,id,id1):
    if id1=="welfare_completed":

        items = tbl_welfareactn.objects.get(complaint_id=id)
        return render(request,"counciler_viewaction1.html",{'ct':items})
    else:
        items=tbl_policeaction.objects.get(complaint_id=id)    
        return render(request,"counciler_viewaction2.html",{'ct':items})
def admin_viewaction(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_complaint.objects.exclude(status="pending").exclude(status="adminverified") 
        return render(request,"admin_viewaction.html",{'ct':items})

def admin_viewaction1(request,id,id1):
    if id1=="welfare_completed":

        items = tbl_welfareactn.objects.get(complaint_id=id)
        return render(request,"admin_viewaction1.html",{'ct':items})
    else:
        items=tbl_policeaction.objects.get(complaint_id=id)    
        return render(request,"admin_viewaction2.html",{'ct':items})
def verify_action(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else: 
        items = tbl_complaint.objects.filter(status='counciler') 
        return render(request,"verify_action.html",{'ct':items})
def take_action(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_complaint.objects.get(id=id)
        data=tbl_idgen.objects.get(id=1)
        f=data.action_id
        f=f+1
        f1="ACTION"+str(f)
        request.session['AN_ID']=f
        return render(request,"take_action.html",{'ff':f1,'items':items})
def verify_action1(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_action.objects.get(complaint_id=id)
        return render(request,"verify_action1.html",{'ct':items})
def viewdetails_welfare(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_complaint.objects.get(complaint_id=id)
        return render(request,"viewdetails_welfare.html",{'ct':items})
def viewdetails_police(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_complaint.objects.get(complaint_id=id)
        return render(request,"viewdetails_police.html",{'ct':items})
def police_takeaction(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else: 
        data1=tbl_action.objects.get(complaint_id=id) 
        data=tbl_idgen.objects.get(id=1)
        f=data.policeaction_id
        f=f+1
        f1="POLICEACTION"+str(f)
        request.session['PA_ID']=f
        aid=request.session['uid']
        data=tbl_account.objects.get(account_id=aid)
        return render(request,"police_takeaction.html",{'ff':f1,'items':data1,'data':data})
def police_action(request):
    if request.method == "POST":
        data = tbl_policeaction()
        data.policeaction_id=request.POST.get('policeaction_id')
        data.account_id=request.POST.get('account_id')
        data.name=request.POST.get('name')
        data.complaint_id=request.POST.get('complaint_id')
        data.remarks=request.POST.get('remarks')
        data.action=request.POST.get('action')
        data.status="finished"
        data.save()
        s=request.session['PA_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.policeaction_id=s
        data2.save()
        data3=tbl_complaint.objects.get(complaint_id=request.POST.get("complaint_id"))
        data3.status="police_completed"
        data3.save()
        
        return redirect('/police_viewcomplaint')
def welfare_takeaction(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else: 
        data1=tbl_action.objects.get(complaint_id=id) 
        data=tbl_idgen.objects.get(id=1)
        f=data.welfareaction_id
        f=f+1
        f1="WELFAREACTION"+str(f)
        request.session['WF_ID']=f
        aid=request.session['uid']
        data=tbl_account.objects.get(account_id=aid)
        return render(request,"welfare_takeaction.html",{'ff':f1,'items':data1,'data':data})
def welfare_action(request):
    if request.method == "POST":
        data=tbl_welfareactn()
        data.welfareaction_id=request.POST.get('welfareaction_id')
        data.account_id=request.POST.get('account_id')
        data.name=request.POST.get('name')
        data.complaint_id=request.POST.get('complaint_id')
        data.remarks=request.POST.get('remarks')
        data.action=request.POST.get('action')
        data.status="finished"
        data.save()
        s=request.session['WF_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.welfare_id=s
        data2.save()
        data3=tbl_complaint.objects.get(complaint_id=request.POST.get("complaint_id"))
        data3.status="welfare_completed"
        data3.save()
        
        return redirect('/welfare_viewcomplaint')
            
def verify_action2(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_complaint.objects.get(complaint_id=request.POST.get('complaint_id'))
        items.status="adminverified"
        items.save()
        items1=tbl_action.objects.get(complaint_id=request.POST.get('complaint_id'))
        items1.status="adminverified"
        items1.save()
        return redirect('/verify_action')
def welfare_viewcomplaint(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else: 
        items = tbl_action.objects.filter(redirectedTo="welfare").filter(status="adminverified") 
        return render(request,"welfare_viewcomplaint.html",{'ct':items})
def police_viewcomplaint(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else: 
        items = tbl_action.objects.filter(redirectedTo="police").filter(status="adminverified") 
        return render(request,"police_viewcomplaint.html",{'ct':items})
def actions(request):
    if request.method == "POST":
        data = tbl_action()
        data.action_id=request.POST.get('action_id')
        data.complaint_id=request.POST.get('complaint_id')
        data.views=request.POST.get('views')
        data.suggestions=request.POST.get('suggestions')
        data.actiondetails=request.POST.get('actiondetails')
        data.redirectedTo=request.POST.get('redirectedTo')
        data.status="pending"
        data.save()
        s=request.session['AN_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.action_id=s
        data2.save()
        items=tbl_complaint.objects.get(complaint_id=request.POST.get('complaint_id'))
        items.status="counciler"
        items.save()
    return redirect('/complaint')
def add_account(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        data=tbl_idgen.objects.get(id=1)
        f=data.account_id
        f=f+1
        f1="ACCOUNT"+str(f)
        request.session['A_ID']=f
        return render(request,'add_account.html',{'ff':f1})
def student_registration(request): 
    data=tbl_idgen.objects.get(id=1)
    f=data.student_id
    f=f+1
    f1="STUDENT"+str(f)
    request.session['S_ID']=f
    return render(request,'student_registration.html',{'ff':f1})
def add_account1(request):
    if request.method == "POST":
        data = tbl_account()
        data.name=request.POST.get('name')
        data.role=request.POST.get('role')
        data.email=request.POST.get('email')
        data.phone=request.POST.get('phone')
        data.status="active"
        data.account_id=request.POST.get('account_id')
        data.save()

        s=request.session['A_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.account_id=s
        data2.save()
        data3=tbl_login()
        data3.user_id=request.POST.get('account_id')
        data3.password=request.POST.get('phone')
        data3.category=request.POST.get('role')
        data3.save()
        return redirect('/add_account')

    
def students(request):
    if request.method == "POST":
        data = tbl_studentreg()
        data.student_id=request.POST.get('student_id')
        data.reg_no=request.POST.get('reg_no')
        data.student_name=request.POST.get('student_name')
        data.course=request.POST.get('course')
        data.semester=request.POST.get('semester')
        data.address=request.POST.get('address')
        data.phone_no=request.POST.get('phone_no')
        data.email=request.POST.get('email')
        data.status="active"
        data.save()
        items=tbl_login()
        items.user_id=request.POST.get('student_id')
        items.password=request.POST.get('phone_no')
        items.category="student"
        items.save()
        s=request.session['S_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.student_id=s
        data2.save()
        return redirect('/student_registration')





def parents(request):
    if request.method == "POST":
        data = tbl_parentreg()
        
        data.parent_id=request.POST.get('parent_id')
        data.student_id=request.POST.get('student_id')
        data.reg_no=request.POST.get('reg_no')
        data.parent_name=request.POST.get('parent_name')
        data.address=request.POST.get('address')
        data.phone=request.POST.get('phone_no')
        data.email=request.POST.get('email')
        data.status="active"
        data.save()
        items=tbl_login()
        items.user_id=request.POST.get('parent_id')
        items.password=request.POST.get('phone_no')
        items.category="parent"
        items.save()
        s=request.session['P_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.parent_id=s
        data2.save()
       
    return redirect('/view_student')
def remove_account(request): 
    items = tbl_account.objects.all() 
    return render(request,"remove_account.html",{'ct':items})
def view_student(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else: 
        items = tbl_studentreg.objects.all() 
        return render(request,"view_student.html",{'items':items}) 
def view_notification(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_notification.objects.all() 
        return render(request,"view_notification.html",{'ct':items}) 
def view_awareness(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_awareness.objects.all() 
        return render(request,"view_awareness.html",{'ct':items})   
def remove_account1(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_account.objects.get(id=id)
        items.delete() 
        return redirect('/remove_account')
def add_notification(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        data=tbl_idgen.objects.get(id=1)
        f=data.notification_id
        f=f+1
        f1="NOTIFICATN"+str(f)
        request.session['N_ID']=f
        return render(request,'add_notification.html',{'ff':f1})

def add_notification1(request):
    
    if request.method == "POST":
        data = tbl_notification()
        data.notification_id=request.POST.get('notification_id')
        data.notification=request.POST.get('notification')
        data.date=request.POST.get('date')
        
        data.status="active"
        data.save()

        s=request.session['N_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.notification_id=s
        data2.save()
        
        return redirect('/add_notification')
def remove_notification(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_notification.objects.all() 
        return render(request,"remove_notification.html",{'ct':items})
def remove_notification1(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_notification.objects.get(id=id)
        items.delete() 
        return redirect('/remove_notification')
def remove_awareness(request):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_awareness.objects.all() 
        return render(request,"remove_awareness.html",{'ct':items})
def remove_awareness1(request,id):
    if 'uid' not in request.session:
            return render(request,"login.html")
    else:  
        items = tbl_awareness.objects.get(id=id)
        items.delete() 
        return redirect('/remove_awareness')
def add_awareness(request): 
    data=tbl_idgen.objects.get(id=1)
    f=data.awareness_id
    f=f+1
    f1="AWARENES"+str(f)
    request.session['AW_ID']=f
    return render(request,'add_awareness.html',{'ff':f1})

def add_awareness1(request):
    if request.method == "POST":
        data = tbl_awareness()
        data.awareness_id=request.POST.get('awareness_id')
        data.awareness=request.POST.get('awareness_news')
        data.date=request.POST.get('date')
        
        data.status="active"
        data.save()

        s=request.session['AW_ID']
        data2=tbl_idgen.objects.get(id=1)
        data2.awareness_id=s
        data2.save()
        
        return redirect('/add_awareness')

def logout(request): 
    del request.session['uid']
    return render(request,'login.html')
def logins(request):
    if request.method=='POST':
        data=tbl_login.objects.all()
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        flag=0
        for da in data:
            if Username==da.user_id and Password==da.password:
                type=da.category
                flag=1
                request.session['uid']=Username
                if type=="admin":
                    return redirect('/admin1')
                elif type=="police":
                    return redirect('/police1')
                elif type=="welfare":
                    return redirect('/welfare1')
                elif type=="student":
                    return redirect('/student1')
                elif type=="parent":
                    return redirect('/parent1')
                elif type=="counciler":
                    return redirect('/counciler1')
                
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("User doesn't exist") 
# Create your views here.
