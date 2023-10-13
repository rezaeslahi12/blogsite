
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.shortcuts import render
from .models import Post,Category
from django.http import HttpResponse
from django.template import loader

def index(request,category_id):
    cat = Category.objects.get(id=category_id)
    category_title = cat.title
    print(category_title)
    print('sssssssss')
    post_list = Post.objects.filter(maincategory = category_id).order_by("publish_date")
    print(post_list)
    context = {
        "post_list": post_list,
    }
    
    return render(request,"blog/index.html" ,context)

def home(request):
    Category_list = Category.objects.all()
    post_list = Post.objects.order_by("publish_date")

    context = {
        "Category_list": Category_list,
        "post_list": post_list
    }
    
    return render(request,"blog/home.html" ,context)

def detail(request, post_id):
    post_list = Post.objects.order_by("publish_date")
    post = Post.objects.get(id=post_id)
    likes_count = post.likes.count()
    context = {
        "post": post,
        "likes_count": likes_count,
        "post_list":post_list,
        "post_id":post_id
    }

    return render(request,"blog/detail.html" ,context)

def post_like(request,post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if user in post.likes.all():
        return HttpResponse("You Liked This Post Befor")
    post.likes.add(user)
    return redirect('detail', post_id)


def post_unlike(request,post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        return redirect('detail', post_id)
    return HttpResponse("You Did'nt Like This Post")














def results(request, post_id):
    response = "You're looking at the results of post %s."
    return HttpResponse(response % post_id)