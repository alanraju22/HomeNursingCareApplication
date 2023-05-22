from urllib import request

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render, redirect



def index(request):
    return render(request,'HomePage.html')



def AdminHomePage(request):
    return render(request, 'AdminHomePage.html')

def logout(request):
    return render(request,'LogOut.html')

def login(request):
    return render(request,"login.html")


def reply_feedback_action(request):
     reply = request.POST['reply']
     id=  request.POST['fid']
     cursor = connection.cursor()
     cursor.execute ("update feedback set reply ='" + reply + "' where feedback_id='" + str(id) + "'")
     return HttpResponse("<script>alert('Reply Send');window.location='/view_feedback';</script>")



def view_feedback(request):
    cursor = connection.cursor()
    cursor.execute("select * from feedback  ")
    pin = cursor.fetchall()
    print(pin)
    return render(request,"ViewFeedback.html",{'data':pin})


def link_reply_feedback(request, id):
    return render(request, "reply_feedback.html", {'data': id})


def Addcategory(request):
    if request.method == "POST":
        plan_name = request.POST['name']
        try:
            l = int(plan_name)
            return HttpResponse("<script>alert('Invalid Plan');window.location='/AdminHomePage';</script>")
        except:
            cursor = connection.cursor()
            cursor.execute ("insert into care_plan values(null,'" + plan_name + "')")
            return HttpResponse("<script>alert('');window.location='/AdminHomePage';</script>")
    return render(request,"Addcategory.html")



def viewCategory(request):
    cursor = connection.cursor()
    cursor.execute("select * from care_plan")
    pin = cursor.fetchall()
    print(pin)
    return render(request,"viewCategory.html",{'data':pin})


def deleteCategory(request,id):
    cursor = connection.cursor()
    cursor.execute ("delete from care_plan where idcare_plan='"+str(id)+"'")
    return HttpResponse( "<script>alert('Deleted Succesfully');window.location='/viewCategory';</script>")


def editCategory(request,id):
    cursor = connection.cursor()
    cursor.execute("select * from care_plan where idcare_plan='"+str(id)+"'")
    pin = cursor.fetchall()
    print(pin)
    return render(request,"editCategory.html",{'data':pin})

def updatecategory(request,id):
    if request.method == "POST":
        plan_name = request.POST['name']
        cursor = connection.cursor()
        cursor.execute("update care_plan set plan_name='" + plan_name + "' where   idcare_plan  ='" + str(id) + "'")
        return HttpResponse("<script>alert('Updated');window.location='/viewCategory';</script>")
    return render(request,"editCategory.html")


def login1(request):
    if request.method == "POST":
        name = request.POST['un']
        password = request.POST['pass']
        request.session['lid']=name
        cursor = connection.cursor()
        cursor.execute ("select * from login where admin_id='" + name + "' and password='" + password + "'")
        print("select * from login where admin_id='" + name + "' and password='" + password + "'")
        pins = cursor.fetchone()
        flag='error'
        if pins == None:
            print("not admin")
            cursorF = connection.cursor()
            cursorF.execute("select * from food_inspector where insp_user_id='" + name + "' and password='" + password + "'")
            print("select * from food_inspector where insp_user_id='" + name + "' and password='" + password + "'")
            food = cursorF.fetchone()
            if food == None:
                    return redirect("/")
            else:
                flag = 'food'
                print("food insp")
        else:
            flag="admin"
            print("this is admin")
    print("flag is:"+flag)
    if flag=="admin":
        return redirect("/AdminHomePage")
    if flag == "error":
        return HttpResponse("<script>alert('invalid');window.location='login';</script>")

    return HttpResponse("<script>alert('invalid');window.location='login';</script>")


def registernurse(request):
    if request.method == "POST":
        name = request.POST['TxtName']
        address = request.POST['TxtAddress']
        phone = request.POST['TxtPhone']
        registration_no = request.POST['registration_no']
        nurse_id = request.POST['nurse_id']
        experience = request.POST['experience']
        password = request.POST['password']
        cursor = connection.cursor()
        cursor.execute ("insert into nurse_registration values(null,'" + name + "','" + address + "','" + phone + "','" + registration_no + "','" + nurse_id + "','" + password + "','pending','" + experience + "')")
        return HttpResponse("<script>alert('Nurse Registered');window.location='/AdminHomePage';</script>")
    return render(request,"registernurse.html")

def viewAllNewRequest(request):
    cursor = connection.cursor()
    cursor.execute("select * from nurse_registration where status='pending'")
    pin = cursor.fetchall()
    print(pin)
    return render(request,"viewAllNewRequest.html",{'data':pin})


def approve(request,id):
    cursor = connection.cursor()
    cursor.execute("update nurse_registration set status='approved' where idnurse_registration='" + str(id) + "'")
    return redirect("/viewAllNewRequest")

def Reject(request,id):
    cursor = connection.cursor()
    cursor.execute("update nurse_registration set status='rejected' where idnurse_registration='" + str(id) + "'")
    return redirect("/viewAllNewRequest")


def delete_nurse(request,id):
    cursor = connection.cursor()
    cursor.execute("delete from nurse_registration where idnurse_registration='" + str(id) + "' ")
    return HttpResponse("<script>alert('Nurse Deleted');window.location='/AdminHomePage';</script>")


def viewnurseApprove(request):
    cursor = connection.cursor()
    cursor.execute("select * from nurse_registration where status='approved'")
    pin = cursor.fetchall()
    return render(request,"viewnurseApprove.html",{'data':pin})


def patientenqueiry (request):
    cursor = connection.cursor()
    cursor.execute("SELECT patients.name,care_plan.plan_name,patients_connect.* FROM   patients_connect join patients join care_plan on patients_connect.idpatients=patients.idpatients and care_plan.idcare_plan=patients_connect.idcare_plan where patients_connect.status='Pending'")
    pin = cursor.fetchall()
    print(pin)
    return render(request,"patientenqueiry.html",{'data':pin})


def view_approved_patient_enqueiry (request):
    cursor = connection.cursor()
    cursor.execute("SELECT patients.name,care_plan.plan_name,patients_connect.* FROM   patients_connect join patients join care_plan on patients_connect.idpatients=patients.idpatients and care_plan.idcare_plan=patients_connect.idcare_plan where patients_connect.status='approve'")
    pin = cursor.fetchall()
    print(pin)
    return render(request,"ViewApprovedRequest.html",{'data':pin})



def reply(request,id):
    request.session['rid'] = id
    return render(request,'reply2.html',{'data':id})


def reply_amount(request,id):
    request.session['aid'] = id
    return render(request, "replyadmin.html",{'data':id})

def reply_admin_amount(request):
        amount = request.POST['amount']
        reply = request.POST['reply']

        try:
            l=int(reply)
            return HttpResponse("<script>alert('Invalid Reply');window.location='/patientenqueiry';</script>")
        except:
            aid=request.session['aid']
            cursor = connection.cursor()
            cursor.execute ("update patients_connect set amount='" + amount + "',status='approve',agency_reply='"+reply+"' where idpatients_connect='" + str(aid) + "'")
            return HttpResponse("<script>alert('Reply Send');window.location='/patientenqueiry';</script>")


def replyadmin2(request):
     reply = request.POST['reply']
     id=request.session['rid']
     cursor = connection.cursor()
     cursor.execute ("update patients_connect set agency_reply ='" + reply + "' where idpatients_connect='" + str(id) + "'")
     return HttpResponse("<script>alert('Reply Send');window.location='/patientenqueiry';</script>")


def nursequery(request):
    cursor = connection.cursor()
    cursor.execute("select * from nurse_query ")
    pin = cursor.fetchall()
    print(pin)
    return render(request,"nursequery.html",{'data':pin})


def replyquery(request):
    reply = request.POST['reply']
    qid = request.POST['qid']
    try:
        l = int(reply)
        return HttpResponse("<script>alert('Invalid Reply');window.location='/nursequery';</script>")
    except:
        cursor = connection.cursor()
        cursor.execute ("update nurse_query set reply='" + reply + "' where nurse_query_id='" + str(qid) + "'")
        return HttpResponse("<script>alert('Replied');window.location='/nursequery';</script>")


def link_reply_query(request,id):
    return render(request,'replyquery.html',{'data':id})




def viewComplient(request):
    cursor = connection.cursor()
    cursor.execute("select complaints.*, patients.* from complaints  join patients on complaints.patient_id = patients.idpatients ")
    pin = cursor.fetchall()
    print(pin)
    return render(request,"viewComplient.html",{'data':pin})

def replyC(request,id):
    request.session["cid"]=id
    if request.method == "POST":
        cid = request.session["cid"]
        reply = request.POST['reply']
        try:
            l = int(reply)
            return HttpResponse("<script>alert('Invalid Reply');window.location='/viewComplient';</script>")
        except:
            comp_id = request.POST['comp_id']
            cursor = connection.cursor()
            cursor.execute ("update complaints set reply='" + reply + "' where idcomplaints='" + str(cid) + "'")
            return HttpResponse("<script>alert('Reply Sended');window.location='/viewComplient';</script>")
    return render(request,"replyC.html")

def link_reply(request):
    return render(request, )

def selectpatient(request):
    cursor = connection.cursor()
    cursor.execute("select patients_connect.*, patients.*, care_plan.* from patients_connect join patients join care_plan on patients_connect.idpatients = patients.idpatients and patients_connect.idcare_plan=care_plan.idcare_plan where patients_connect.status='Paid' ")
    pin = cursor.fetchall()
    print(pin)
    return render(request, "selectpatient.html", {'data': pin})

def select_assigned_patient(request):
    cursor = connection.cursor()
    cursor.execute(" select patients_connect.*, patients.*, care_plan.* from patients_connect join patients join care_plan on patients_connect.idpatients = patients.idpatients and patients_connect.idcare_plan=care_plan.idcare_plan where patients_connect.status='Assigned'")
    pin = cursor.fetchall()
    print(pin)
    return render(request, "assigned_patient_list.html", {'data': pin})


def selectnurse(request,id,sid):
    request.session['cnid']=id
    request.session['pid']=sid
    print(id)
    print(sid)
    cursor = connection.cursor()
    cursor.execute("select * from nurse_registration ")
    pin = cursor.fetchall()
    print(pin)
    return render(request, "selectnurse.html", {'data': pin})


def assignnurse(request,nid):
    tid=request.session['pid']
    cnid=request.session['cnid']
    if request.method == "POST" :
        idpatient_connect = cnid
        idpatients =tid
        nurse_id = nid
        assign_date=request.POST['assign_date']
        cursor = connection.cursor()
        cursor.execute ("insert into work_assign values(null,'" + str(idpatient_connect) + "','" + nurse_id + "','" + assign_date + "','" + str(idpatients) + "')")
        cursor.execute("update patients_connect set status='assigned' where idpatients_connect= '" + str( idpatient_connect) + "' ")

        return HttpResponse("<script>alert('Work Assigned');window.location='/AdminHomePage';</script>")
    return render(request, "assignnurse.html")


def viewassigned(request):
    cursor = connection.cursor()
    cursor.execute("select * from work_assign ")
    pin = cursor.fetchall()
    print(pin)
    return render(request, "viewassigned.html", {'data': pin})


def view_nurse_details(request,id):
    cursor = connection.cursor()
    cursor.execute(" select distinct work_assign.nurse_id ,work_assign.assign_date,patients_connect.* from work_assign join patients_connect on patients_connect.idpatients_connect=work_assign.idpatient_connect where patients_connect.idpatients_connect='" +str(id)+"'")
    pin = cursor.fetchall()
    print(pin)
    return render(request, "view_all_nurse.html", {'data': pin})


def view_nurse_pro(request,id):
    cursor = connection.cursor()
    cursor.execute("select * from nurse_registration where nurse_id='"+str(id)+"' ")
    pin = cursor.fetchall()
    print(pin)
    return render(request, "ViewNurseProfile.html", {'data': pin})

