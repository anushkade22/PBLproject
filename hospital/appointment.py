# import the standard Django Forms
# from built-in library
from django import forms

# creating a form
class InputForm(forms.Form):
    name = forms.CharField(max_length = 200)
    email = forms.CharField(max_length = 200)
    phone = forms.CharField(max_length=12)
    aadhar = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    message = forms.CharField(max_length=200)
    date = forms.DateField()
    age = forms.IntegerField()
    disease = forms.CharField(max_length=200)
    gender = forms.CharField(max_length=200)
    message = forms.CharField(max_length=200)
