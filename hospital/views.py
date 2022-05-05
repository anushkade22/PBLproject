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

hospitals = hospitalCollection.get()
hospitalList=[]
for hospital in hospitals:
    print(hospital.to_dict())
    hospitalList.append(hospital.to_dict())
    
def home(request):
       
    return render(request,'hospital/home.html')

def bedManagement(request):
    location = request.POST.get('location')

    return render(request,'hospital/bedavail.html',{'title':'Bed-availability' , "hospitals":hospitalList, "location": location})

def donation(request):
    return render(request,'hospital/donate.html',{'title':'Donation' ,  "hospitals":hospitalList})

def appointment(request):
    if request.method == "POST":
        myform = InputForm()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        aadhar = request.POST.get('aadhar')
        address = request.POST.get('address')
        date = request.POST.get('date')
        age = request.POST.get('age')
        disease = request.POST.get('disease')
        gender = request.POST.get('gender')
        message = request.POST.get('message')
        myform.name = name
        myform.email = email
        myform.phone = phone
        myform.aadhar = aadhar
        myform.address = address
        myform.date = date
        myform.age = age
        myform.disease = disease
        myform.gender = gender
        myform.message = message
        print(myform.name)
        context ={
            'myform':myform,
            'name' : myform.name
        }
        
    else:
        myform = InputForm()
        context ={
            'myform':myform,
            'name' : ""
        }
    
    
    return render(request,'hospital/appointment.html',context)