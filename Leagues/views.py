from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts import models as  accounts_models
from posts import models as posts_models
from Leagues import models as Leagues_models
from posts import forms as posts_forms
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import F
from django.views.generic.base import TemplateView
from itertools import chain
from django.contrib import messages
from .forms import FreeLeagueChatForm
import os

#create the categories here.
def categories_creator():
    file_path = os.path.join('Leagues', 'categories.txt')
    file = open(file_path,'r+')
    for category in range(1,1000,5):
        file.write(str(category)+' - '+str(category+4)+'\n')
    file.close()


def freeleaaguedecider(member):
    file_path = os.path.join('Leagues', 'categories.txt')
    file = open(file_path,'r+')
    for category in file:
        if int(category.split()[0])<= member.profilestatus <=int(category.split()[2]):
            if Leagues_models.FreeLeague.objects.get_or_create(categoryname="Free League"+" "+(category)):
                Leagues_models.FreeLeague.objects.get(categoryname="Free League"+" "+(category)).members.add(member.username)
                Leagues_models.FreeLeague.objects.filter(categoryname="Free League"+" "+(category)).update(category=category)
                break




class league(TemplateView):
    template_name="league.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["MegaLeague"]=Leagues_models.MegaLeague.objects.filter(members=self.request.user)
        context["HotLeague"]=Leagues_models.HotLeague.objects.filter(members=self.request.user)
        context["DailyLeague"]=Leagues_models.DailyLeague.objects.filter(members=self.request.user)
        context["FreeLeague"]=self.request.user.FreeLeagueMembers.filter()
        context["resultleague"]=list(chain(context["FreeLeague"],context["MegaLeague"],context["HotLeague"],context["DailyLeague"]))
        return context




class joinleague(TemplateView):
    template_name="joinleague.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["DailyLeague"]=Leagues_models.DailyLeague.objects.filter(members=self.request.user)
        context["MegaLeague"]=Leagues_models.MegaLeague.objects.filter(members=self.request.user)
        context["HotLeague"]=Leagues_models.HotLeague.objects.filter(members=self.request.user)
        context["leagues"]={"Hot League":"2 PRC","Mega League":"5 PRC","Daily League":"2 PRC"}
        context["resultleague"]=list(x.__class__.__name__ for x in list(chain(context['DailyLeague'],context["MegaLeague"],context["HotLeague"])) )

        return context


def FreeLeague(request):
    users=accounts_models.Profile.objects.filter(username__FreeLeagueMembers__members=request.user).order_by("-leaguescore")
    previouswinners=Leagues_models.Winners.objects.filter(winnerleaguename=request.user.FreeLeagueMembers.get())    
    FreeLeagueChat=FreeLeagueChatForm()
    if request.method=="POST" and "text" in request.POST:
        league = Leagues_models.FreeLeague.objects.get(members=request.user)
        form =FreeLeagueChatForm(request.POST)
        if form.is_valid():
                comment = form.save(commit=False)
                comment.league = league
                comment.username=request.user
                comment.save()
                return redirect("FreeLeague")
    return render(request,"freeleague.html",{"users":users,"previouswinners":previouswinners,"FreeLeagueChatForm":FreeLeagueChatForm})




def HotLeagueWinners(request):
    requestusercategory=request.user.FreeLeagueMembers.get().category
    previouswinners=Leagues_models.Winners.objects.filter(winnerleaguename="Hot League",category=requestusercategory)
    return render(request,"previouswinners.html",{"previouswinners":previouswinners})



def HotLeague(request):
    if request.method=="POST":

        if request.user.Profile.piccredits>=2:
            requestusercategory=request.user.FreeLeagueMembers.get().category
            Leagues_models.HotLeague.objects.get_or_create(categoryname="Hot League"+" "+(requestusercategory))
            Leagues_models.HotLeague.objects.get(categoryname="Hot League"+" "+requestusercategory).members.add(request.user)
            Leagues_models.FreeLeague.objects.filter(categoryname="Free League"+" "+(requestusercategory)).update(category=requestusercategory)
            accounts_models.Profile.objects.filter(username=request.user).update(piccredits=F('piccredits')-2)
            return redirect("HotLeagueplayers")
        else:
            messages.warning(request,"You dont have enough credits to join")
        return redirect("joinleague")
    

def HotLeagueplayers(request):
    requestusercategory=request.user.FreeLeagueMembers.get().category
    users=accounts_models.Profile.objects.filter(username__HotLeagueMembers__members=request.user).order_by("-leaguescore")
    previouswinners=Leagues_models.Winners.objects.filter(winnerleaguename="Hot League",category=requestusercategory)
    return render(request,"HotLeagueplayers.html",{"users":users,"previouswinners":previouswinners})



def MegaLeague(request):
    if request.method=="POST":

        if request.user.Profile.piccredits>=5:
            requestusercategory=request.user.FreeLeagueMembers.get().category
            Leagues_models.HotLeague.objects.get_or_create(categoryname="Mega League"+" "+(requestusercategory))
            Leagues_models.HotLeague.objects.get(categoryname="Mega League"+" "+requestusercategory).members.add(request.user)
            Leagues_models.FreeLeague.objects.filter(categoryname="Mega League"+" "+(requestusercategory)).update(category=requestusercategory)
            accounts_models.Profile.objects.filter(username=request.user).update(piccredits=F('piccredits')-5)
            return redirect("MegaLeagueplayers")
        else:
            messages.warning(request,"You dont have enough credits to join")
        return redirect("joinleague")
    

def MegaLeagueplayers(request):
    requestusercategory=request.user.FreeLeagueMembers.get().category
    users=accounts_models.Profile.objects.filter(username__MegaLeagueMembers__members=request.user).order_by("-leaguescore")
    previouswinners=Leagues_models.Winners.objects.filter(winnerleaguename="Mega League",category=requestusercategory)
    return render(request,"Megaleagueplayers.html",{"users":users,"previouswinners":previouswinners})


def MegaLeagueWinners(request):
    requestusercategory=request.user.FreeLeagueMembers.get().category
    previouswinners=Leagues_models.Winners.objects.filter(winnerleaguename="Mega League",category=requestusercategory)
    return render(request,"previouswinners.html",{"previouswinners":previouswinners})


def DailyLeague(request):
    if request.method=="POST":
        if request.user.Profile.piccredits>=2:
            requestusercategory=request.user.FreeLeagueMembers.get().category
            Leagues_models.DailyLeague.objects.get_or_create(categoryname="Daily League"+" "+(requestusercategory))
            Leagues_models.DailyLeague.objects.get(categoryname="Daily League"+" "+requestusercategory).members.add(request.user)
            accounts_models.Profile.objects.filter(username=request.user).update(piccredits=F('piccredits')-2)
            return redirect("DailyLeagueplayers")
        else:
            messages.warning(request,"You dont have enough credits to join")
        return redirect("joinleague")

def DailyLeagueplayers(request):
    requestusercategory=request.user.FreeLeagueMembers.get().category
    users=accounts_models.Profile.objects.filter(username__DailyLeagueMembers__members=request.user).order_by("-leaguescore")
    previouswinners=Leagues_models.Winners.objects.filter(winnerleaguename="Daily League",category=requestusercategory)
    return render(request,"Dailyleagueplayers.html",{"users":users,"previouswinners":previouswinners})

def DailyLeagueWinners(request):
    requestusercategory=request.user.FreeLeagueMembers.get().category
    previouswinners=Leagues_models.Winners.objects.filter(winnerleaguename="Daily League",category=requestusercategory)
    return render(request,"previouswinners.html",{"previouswinners":previouswinners})

