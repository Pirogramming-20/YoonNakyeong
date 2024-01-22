from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm, CommentForm


# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts':posts,
    }
    return render(request, 'posts/post_list.html',ctx)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    else:  # This covers the GET request
        form = PostForm()

    ctx = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', ctx)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def comment_ajax(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = request.POST.get('post_id')
            comment.save()
            return JsonResponse({'comment': comment.comment, 'comment_id': comment.id}, status=200)
        else:
            return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def comment_delete(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({'status': 'ok'}, status=200)
        except Comment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '댓글을 찾을 수 없습니다.'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': '잘못된 요청입니다.'}, status=400)
    
@csrf_exempt
def like_ajax(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
            post.like+=1
            post.save()
            like = post.like 
            return JsonResponse({'likes': like})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)