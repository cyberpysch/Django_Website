from django.shortcuts import render,HttpResponse
from .models import AdmissionEnquiry
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'AdmissionPortal/index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        For_choice=request.POST.get('For_choice','')
        course=request.POST.get('course','')
        university=request.POST.get('university','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip=request.POST.get('zip','')

        if len(name)<3 or len(email)<15 or len(phone)<6 or len(course)<2  or len(address)<15 or len(city)<3 :
            messages.error(request, "Please fill the form correctly")
        else:
            contact=AdmissionEnquiry(name=name,phone=phone,email=email,For_choice=For_choice,course=course,university=university,address=address,city=city,state=state,zip=zip)
            contact.save()
            messages.success(request, "Thanks for reach out us ,'We'll Contact you shortly!'")
    return render(request,'AdmissionPortal/contact.html')

def services(request):
    return render(request,'AdmissionPortal/services.html')



