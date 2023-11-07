from django.shortcuts import render
from studentprofile.models import studentsection
from home.views import loginportal

# Create your views here.
def index(request):
    
    try:
        allProfile=studentsection.objects.filter(all)
        print(allProfile)
    except Exception as e:
        allProfile=None
        print('Exception :',e)
    context={'allProfile': allProfile}
    return render(request,'studentprofile/index.html',context)