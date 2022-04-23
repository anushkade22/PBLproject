from django.shortcuts import render
from django.http import HttpResponse
#import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("hospital-sdk.json")
firebase_admin.initialize_app(cred)
db= firestore.client()

hospitalCollection = db.collection('hospitals')

def home(request):
    return render(request,'hospital/home.html')
# Create your views here.

def bedManagement(request):
    hospitals = hospitalCollection.get()
    hospitalList=[]
    for hospital in hospitals:
        print(hospital.to_dict())
        hospitalList.append(hospital.to_dict())
    return render(request,'hospital/bedavail.html',{'title':'Bed-availability' , "hospitals":hospitalList})

def donation(request):
    return render(request,'hospital/donate.html',{'title':'Donation'})

def appointment(request):
    return render(request,'hospital/appointment.html',{'title':'Appointment'})