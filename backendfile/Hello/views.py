from django.shortcuts import render, HttpResponse
from .models import Registration
from datetime import datetime
from django.contrib import messages

def index(request):
    
    return render(request, 'index.html')
    

def hello(request):
    return render(request, 'basef.html')

def user(request):
    return render(request, "about.html")

def mainnet(request):
    if request.method == "POST":
        fn = request.POST.get("firstname")
        mn = request.POST.get("middlename")
        ln = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        gender = request.POST.get("gender")
        current_address = request.POST.get("current_address")
        password=request.POST.get('psw')
    
        
        registration = Registration(first_name=fn, last_name=ln, middle_name=mn, phone=phone, email=email, course=course, gender=gender, current_address=current_address,password=password,datetime=datetime.today())
        registration.save()
        messages.success(request, 'Your form has been submitted successfully')
    return render(request, "minus.html")



# Create your views here.
