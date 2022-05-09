from django.shortcuts import render
from django.http import HttpResponse
#import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
from .appointment import InputForm

cred = credentials.Certificate("hospital-sdk.json")
firebase_admin.initialize_app(cred)
db= firestore.client()

hospitalCollection = db.collection('hospitals')
userInfo = db.collection('user_info')

    
def home(request):
       
    return render(request,'hospital/home.html')

def bedManagement(request):
    location = request.POST.get('location')
    hospitals = hospitalCollection.get()
    hospitalList=[]
    for hospital in hospitals:
        hospitalList.append(hospital.to_dict())
    return render(request,'hospital/bedavail.html',{'title':'Bed-availability' , "hospitals":hospitalList, "location": location})

def donation(request):
    location = request.POST.get('location')
    return render(request,'hospital/donate.html',{'title':'Donation' ,  "location": location})

def appointment(request):
    hospitals = hospitalCollection.get()
    hospitalList=[]
    for hospital in hospitals:
        hospitalList.append(hospital.to_dict())
    hemail = request.GET.get('hemail')
    #docs = hospitalCollection.where('email', u'==', hemail).stream()
    flag = False
    updated = False
    print(flag)
    if request.method == "POST":
        myform = InputForm()
        myform.name = request.POST.get('name')
        myform.email = request.POST.get('email')
        myform.phone = request.POST.get('phone')
        myform.aadhar = request.POST.get('aadhar')
        myform.address = request.POST.get('address')
        myform.date = request.POST.get('date')
        myform.age = request.POST.get('age')
        myform.disease = request.POST.get('disease')
        myform.gender = request.POST.get('gender')
        myform.message = request.POST.get('message')
        print(myform.name + "" +myform.email)
        for user in userInfo.where('email', '==', myform.email).stream():
            #bedAvail =user.to_dict()['email'];
            flag = True
        
        if not flag: 
            updated = True
            #doc_ref = userInfo.document(myform.email)
            #doc_ref.set({
            doc_ref = userInfo.add({
                'name' : myform.name,
                'email': myform.email,
                'phone': myform.phone,
                'aadhar': myform.aadhar,
                'address': myform.address,
                'date': myform.date,
                'age': myform.age,
                'disease': myform.disease,
                'gender': myform.gender,
                'message': myform.message,
                'hemail': hemail
            })
            for hospital in hospitalCollection.where('email', '==', hemail).stream():
                bedAvail =hospital.to_dict()['bedavail'];
                hospital_ref = hospitalCollection.document(hospital.id)
                hospital_ref.update({u'bedavail': bedAvail-1})
        context ={
            'myform':myform,
            'name' : myform.name,
            'email': myform.email,
            'phone': myform.phone,
            'aadhar': myform.aadhar,
            'address': myform.address,
            'date': myform.date,
            'age': myform.age,
            'disease': myform.disease,
            'gender': myform.gender,
            'message': myform.message,
            'updated':updated,
            'exists':flag
        }
    else:
        myform = InputForm()
        context ={
            'myform':myform,
            'name' : ""
        }
    
    
    return render(request,'hospital/appointment.html',context)