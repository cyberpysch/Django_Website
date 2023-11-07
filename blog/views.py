from django.shortcuts import render,redirect
from blog.models import blogPost as bp
#from blog.models import CommentSection as BC
from django.contrib import messages

# Create your views here.
def index(request):
    allPosts= bp.objects.all()
    context={'allPosts': allPosts}
    return render(request,'blog/index.html',context)

def blogPost(request,slug):
    post=bp.objects.filter(slug=slug).first()
    #comments= BC.objects.filter(post=post)
    context={"post":post,"user":request.user}
    return render(request,'blog/blogPost.html',context)

'''def blogComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment','')
        postSno =request.POST.get('postSno','')
        post= bp.objects.get(sno=postSno)
    

        blogComment=BC(comment= comment, post=post)
        print(blogComment,'this is comment')
        blogComment.save()
        messages.success(request, "Your comment has been posted successfully")
        
    return redirect(f"/blog/{post.slug}")'''