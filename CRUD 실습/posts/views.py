from django.shortcuts import render, HttpResponse,redirect
from .models import *

# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    context={
        "posts":posts
    }
    return render(request, 'posts_list.html', context)

def posts_read(request, pk) :
    post=Post.objects.get(id=pk)
    Post.objects.filter(id__lt=pk)

    previous_post_id=Post.objects.filter(id__lt=pk).order_by('-id')[0].id
    next_post_id=Post.objects.filter(id__gt=pk).order_by('id')[0].id
    comments=Comment.objects.filter(post_id=pk)
    context = {
        "post":post,
        "previous_post_id":previous_post_id,
        "next_post_id":next_post_id,
        "comments":comments,
    }
    return render(request, "posts_read.html", context)

def posts_create(request):
    if request.method == "POST":
        Post.objects.create(
            title = request.POST["title"],
            user=request.POST["user"],
            content=request.POST["content"],
        )
        return redirect("/posts")
    return render(request,"posts_create.html")

# def posts_create_final(request):
#     if request.method == "POST":
#         Post.objects.create(
#             title = request.POST["title"],
#             user=request.POST["user"],
#             content=request.POST["content"],
#         )
#     return redirect("/posts")

def posts_update(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.user = request.POST["user"]
        post.save()
        return redirect(f"/posts/{pk}")
    context = {
        "post":post
    }
    return render(request, "posts_update.html",context)

def posts_delete(request, pk):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()    
    return redirect("/posts")

def comments_create(request,post_id):
    Comment.objects.create(
        post_id = post_id,
        content = request.POST["content"]
    )
    return redirect(f"/posts/{post_id}")