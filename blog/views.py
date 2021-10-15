from django.shortcuts import redirect, render
from .models import posts,comments
from .forms import postFrom, commentForm
from django.urls import reverse
# Create your views here.

def viewposts(request):
    post = posts.objects.all()

    return render(request,"post/page.html",{"posts":post})


def singlepost(request,id):
    SinglePost = posts.objects.get(id=id)
    my_Comments = comments.objects.filter(post=SinglePost)
    if request.method == 'POST':
        comment = commentForm(request.POST)
        if comment.is_valid():
            co = comment.save(commit=False)
            co.post = SinglePost
            co.author = request.user
            co.save()
            # return redirect(reverse('Blog:singlePost', post.id))
    else:
        comment = commentForm()
    return render(request,"post/singlepage.html",{"posts":SinglePost,'comment':comment,'comments':my_Comments})


def addPost(request):
    if request.method =='POST':
        form = postFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = postFrom()
    return render(request,'post/addpost.html',{'from':form})

def editPost(request,id):
    post = posts.objects.get(id=id)
    if request.method =='POST':
        form = postFrom(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('Blog:allPosts'))

    else:
        form = postFrom(instance=post)
    return render(request,'post/addpost.html',{'from':form})
    