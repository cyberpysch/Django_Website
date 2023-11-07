from django.shortcuts import render,HttpResponse,redirect
from blog.models import blogPost as bp
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

def index(request):
    return render(request,'home/index.html')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=bp.objects.none()
    else:
        allPostsTitle= bp.objects.filter(title__icontains=query)
        allPostsAuthor= bp.objects.filter(author__icontains=query)
        allPostsContent =bp.objects.filter(content__icontains=query)
        allPosts= allPostsTitle.union(allPostsContent, allPostsAuthor)

    if allPosts.count()==0 or len(query)==0:
        messages.warning(request, "No search results found. Please refine your query.")



    params={'allPosts': allPosts}
    return render(request,'home/search.html',params)

def loginportal(request):
    if request.method=='POST':
        username=request.POST['loginusername']
        loginPassword=request.POST['loginPassword']
        user=authenticate(username= username, password= loginPassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")
           
    return HttpResponse("Error 404 page not ?Found")

def signup(request):
    if request.method=="POST":
        FirstName=request.POST['FirstName']
        LastName=request.POST['LastName']
        username=request.POST['username']
        SignUpEmail=request.POST['SignUpEmail']
        SignUpPassword=request.POST['SignUpPassword']
        ConfirmSignUpPassword=request.POST['ConfirmSignUpPassword']

        #checks for parameter
        if len(FirstName)==0 or len(LastName)==0 or len(username)==0 or len(SignUpEmail)==0 or len(SignUpPassword)==0 or len(ConfirmSignUpPassword)==0:
            return redirect("/")
        if not username.isalnum():
            messages.error("username only contains letters and numbers")
            return redirect("/")
        if len(username)<8:
            messages.error(request,"Your username is too short")
            return redirect("/")
        elif len(username)>16:
            messages.error(request,"Your username is too long")
            return redirect("/")
        
        if SignUpPassword!=ConfirmSignUpPassword:
            messages.error(request,"Your Password does not match")
            return redirect("/")

        myuser = User.objects.create_user(username,SignUpEmail,SignUpPassword)
        myuser.first_name= FirstName
        myuser.last_name= LastName
        myuser.save()
        messages.success(request, " Your dakhilahub account has been successfully created")
        return redirect("/")

    else:
        return HttpResponse("Error 404 page not Found!")
    
def checklogout(request):
    
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("/")

