from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import SignUpForm,ProfileForm
from accounts import models as  accounts_models
from posts import models as posts_models
from Leagues import models as Leagues_models
from posts import forms as posts_forms
from Leagues.views import freeleaaguedecider
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Count
from django.db.models import F
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.generic.edit import FormView
import datetime
from notifications.signals import notify
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse, reverse_lazy




def rankchecker(profilescore):
    profilescore=int(profilescore)
    constant=0
    for status in range(1,100):
        lowrange=constant
        constant=constant+40+(status*10)
        if lowrange<= profilescore <=constant and round(profilescore,1)==profilescore:
            return status



    


def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            accounts_models.fanandfanned.objects.create(fans=request.user).fanned.add(request.user)
            accounts_models.Profile.objects.create(username=request.user)
            freeleaaguedecider(request.user.Profile)
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            raw_password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                return redirect('Home')
    loginform = AuthenticationForm()
    return render(request, 'registration/login.html', {'loginform': loginform})




@login_required
def home(request):
    if request.user.PostDetail.count()>0:
        if (datetime.date.today()-request.user.PostDetail.last().time.date()).days>0:
            form = posts_forms.imageuploadform()
        else:
            form = posts_models.PostDetail.objects.none()
    else:
        form = posts_forms.imageuploadform()


    users=accounts_models.Profile.objects.filter(username__FreeLeagueMembers__members=request.user).order_by("-leaguescore")
    commentform1 = posts_forms.CommentForm()
    posts = posts_models.PostDetail.objects.filter(username__fanned__fans=request.user).order_by("-time")
    today = datetime.datetime.now()
    last_monday = today - datetime.timedelta(days=today.weekday())

    return render(request, 'home.html',{"userhome":request.user,"form":form,"posts":posts,"commentform1":commentform1,'users':users})




@login_required
def profile(request,username):

    
    userprofile=User.objects.get(username=username)
    posts=User.objects.get(username=username).PostDetail.all().order_by("-time")
    commentform1 = posts_forms.CommentForm()


    if request.method=='POST' and "fanrequest" in request.POST:
        requestperson=User.objects.get(username=request.POST.get("fanrequest"))
        if accounts_models.fanandfanned.objects.filter(fans=request.user,fanned=requestperson):          
            request.user.fans.get().fanned.remove(requestperson)
        else:     
            request.user.fans.get().fanned.add(requestperson) 
            notify.send(request.user, recipient=requestperson, verb='is now  Fan of You',description=request.user.Profile.profilepicture.url)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    return render(request, 'profile.html',{"userprofile":userprofile,"posts":posts,"commentform1":commentform1})



@login_required
def Logout(request):
    request.session.flush()
    return redirect('login')

@login_required
def search(request):
    allusers=User.objects.all().exclude(id=request.user.id)
    return render(request,"search.html",{"allusers":allusers})

@login_required
def PicQuaR(request):
    posts = posts_models.PostDetail.objects.all().order_by("-time")
    commentform1 = posts_forms.CommentForm()
    return render(request,"PicQuaR.html",{"posts":posts,"commentform1":commentform1})


@login_required
def Rankings(request):
    Rankings = accounts_models.Profile.objects.all().order_by("-profilescore")
    return render(request,"Rankings.html",{"Rankings":Rankings})


@login_required
def update_profile_pic(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.Profile)
        if profile_form.is_valid():
            image_form = profile_form.save(commit=False)
            image_form.profilepicture = request.FILES['image']
            image_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))














