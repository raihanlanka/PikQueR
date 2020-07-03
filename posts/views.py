from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts import models as  accounts_models
from posts import models as posts_models
from Leagues import models as Leagues_models
from posts import forms as posts_forms
from .forms import imageuploadform,CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Count
from django.db.models import F
from django.http import HttpResponseRedirect
from notifications.signals import notify
from notifications.models import Notification

# Create your views here.

def Uploadpic(request):
    if request.method =="POST":
        form = imageuploadform(request.POST, request.FILES)     
        if form.is_valid():
            uplpadpic=posts_models.PostDetail.objects.create(username=request.user,postpicture=form.cleaned_data['postpicture'])
    return redirect('Home')



def Ratings(request,postid):    
    picdetails=posts_models.PostDetail.objects.get(id=postid)
    return render(request, 'Ratings.html',{'picdetails':picdetails})





def Comments(request,postid):    
    picdetails=posts_models.PostDetail.objects.get(id=postid)
    return render(request, 'Comments.html',{'picdetails':picdetails})


def addcomment(request):
    if request.method=="POST" and "text" in request.POST:
        post = posts_models.PostDetail.objects.get(id=request.POST.get("postid"))
        form = posts_forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.username=request.user
            comment.save()
            notify.send(request.user, recipient=post.username, verb='commented :' +comment.text,description=post.postpicture.url)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_post(request):
    print('____++',request.POST)
    if request.method=="POST":
        post = posts_models.PostDetail.objects.get(id=request.POST.get("postid"))
        if request.user == post.username:
            post.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

