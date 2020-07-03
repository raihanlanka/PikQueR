from __future__ import absolute_import,unicode_literals
from celery import task
from .models import FreeLeague
from accounts import models as  accounts_models

from Leagues import models as Leagues_models
from django.db.models import Count
from django.db.models import F
from notifications.signals import notify
from .views import freeleaaguedecider



@task()
def task_number_one():
    print('___________one___________')

 

 
@task()
def leagueloader():
    Leagues_models.Winners.objects.filter(winnerleaguename__istartswith="Free League").delete()
    for eachleague in Leagues_models.FreeLeague.objects.all():
        winnerscount =sum(list(accounts_models.Profile.objects.filter(username__FreeLeagueMembers=eachleague).values("leaguescore").annotate(num_books=Count('leaguescore')).order_by("-leaguescore")[:3].values_list("num_books",flat=True)))
        winnersid=list(accounts_models.Profile.objects.filter(username__FreeLeagueMembers=eachleague).order_by("-leaguescore")[:winnerscount])
        for member in winnersid:
            Leagues_models.Winners.objects.create(winningmembers=member.username,winnerleaguename=eachleague,leaguescore=member.leaguescore)
        
        
        #distributing credits to winners
        amount=3
        samewinner=1
        rank=1
        for i in range(1,winnerscount+1):
            winningamount=amount/samewinner
            if winnerscount!=i:

                if winnersid[i-1].leaguescore==winnersid[i].leaguescore:
                    samewinner+=1
                else:
                    for k in range(i-samewinner,i):
                        winner=accounts_models.Profile.objects.filter(username=winnersid[k].username)
                        winner.update(piccredits=F('piccredits')+winningamount)
                        notify.send(winner.get().username, recipient=winner.get().username, verb="Free League Rank :"+str(rank)+", you Won"+str(winningamount)+"PRC")
                    amount-=1
                    samewinner=1
                    rank+=1

            else:
                for j in range(i-samewinner,i):
                    winner=accounts_models.Profile.objects.filter(username=winnersid[j].username)
                    winner.update(piccredits=F('piccredits')+winningamount)
                    notify.send(winner.get().username, recipient=winner.get().username, verb="Free League Rank :"+str(rank)+", you Won"+str(winningamount)+"PRC")

    Leagues_models.FreeLeague.objects.all().delete()


    users=accounts_models.Profile.objects.all()
    for member in users:
        freeleaaguedecider(member)
    print("Free League Loader done")





@task()
def HotLeagueLoader():
    Leagues_models.Winners.objects.filter(winnerleaguename__istartswith="Hot League").delete()

    for eachleague in Leagues_models.HotLeague.objects.all():
        totalmembers=eachleague.members.all().count()
        winnerscount =sum(list(accounts_models.Profile.objects.filter(username__HotLeagueMembers=eachleague).values("leaguescore").annotate(num_books=Count('leaguescore')).order_by("-leaguescore")[:3].values_list("num_books",flat=True)))
        winnersid=list(accounts_models.Profile.objects.filter(username__HotLeagueMembers=eachleague).order_by("-leaguescore")[:winnerscount])

        totalamount=totalmembers*2
        percent=.3
        samewinner=1
        rank=1
        for i in range(1,winnerscount+1):
            winningamount=(totalamount*percent)/samewinner
            if winnerscount!=i:

                if winnersid[i-1].leaguescore==winnersid[i].leaguescore:
                    samewinner+=1
                else:
                    for k in range(i-samewinner,i):
                        winner=accounts_models.Profile.objects.filter(username=winnersid[k].username)
                        winner.update(piccredits=F('piccredits')+winningamount)
                        notify.send(winner.get().username, recipient=winner.get().username, verb="Hot League Rank :"+str(rank)+", you Won"+str(winningamount)+"PRC")
                    percent-=.05
                    samewinner=1
                    rank+=1

            else:
                for j in range(i-samewinner,i):
                    winner=accounts_models.Profile.objects.filter(username=winnersid[j].username)
                    winner.update(piccredits=F('piccredits')+winningamount)
                    notify.send(winner.get().username, recipient=winner.get().username, verb="Hot League Rank :"+str(rank)+", you Won"+str(winningamount)+"PRC")
    
    Leagues_models.HotLeague.objects.all().delete()
    print("Hot League Loader done")




@task()
def MegaLeagueLoader():
    Leagues_models.Winners.objects.filter(winnerleaguename__istartswith="Mega League").delete()


    for eachleague in Leagues_models.MegaLeague.objects.all():
        totalmembers=eachleague.members.all().count()
        winnerscount =sum(list(accounts_models.Profile.objects.filter(username__MegaLeagueMembers=eachleague).values("leaguescore").annotate(num_books=Count('leaguescore')).order_by("-leaguescore")[:3].values_list("num_books",flat=True)))
        winnersid=list(accounts_models.Profile.objects.filter(username__MegaLeagueMembers=eachleague).order_by("-leaguescore")[:winnerscount])

        totalamount=totalmembers*5
        percent=.3
        samewinner=1
        rank=1
        for i in range(1,winnerscount+1):
            winningamount=(totalamount*percent)/samewinner
            if winnerscount!=i:

                if winnersid[i-1].leaguescore==winnersid[i].leaguescore:
                    samewinner+=1
                else:
                    for k in range(i-samewinner,i):
                        winner=accounts_models.Profile.objects.filter(username=winnersid[k].username)
                        winner.update(piccredits=F('piccredits')+winningamount)
                        notify.send(winner.get().username, recipient=winner.get().username, verb="Hot League Rank :"+str(rank)+", you Won"+str(winningamount)+"PRC")
                    percent-=.05
                    samewinner=1
                    rank+=1

            else:
                for j in range(i-samewinner,i):
                    winner=accounts_models.Profile.objects.filter(username=winnersid[j].username)
                    winner.update(piccredits=F('piccredits')+winningamount)
                    notify.send(winner.get().username, recipient=winner.get().username, verb="Hot League Rank :"+str(rank)+", you Won"+str(winningamount)+"PRC")
    
    Leagues_models.MegaLeague.objects.all().delete()
    print("Mega League Loader done")






@task()
def RandomLeagueloader(request):
    Leagues_models.Winners.objects.filter(winnerleaguename="Random League").delete()
    users=Leagues_models.RandomLeague.objects.all().order_by("?")
    if users.count() %2==0:
        winnercount=(users.count()*60)//100
    else:
        winnercount=((users.count()*60)//100)+1
    winners=list(users)[:winnercount]
    eachwinner=(users.count()*4*.75)/winnercount
    for member in winners:
        Leagues_models.Winners.objects.create(winningmembers=member.members,winnerleaguename="Random League",leaguescore=member.members.Profile.leaguescore)
        accounts_models.Profile.objects.filter(username=member.members).update(piccredits=F('piccredits')+eachwinner)
    Leagues_models.RandomLeague.objects.all().delete()
    print("Random League Loader done")



@task()
def DailyLeagueLoader():
    Leagues_models.Winners.objects.filter(winnerleaguename__istartswith="Daily League").delete()


    for eachleague in Leagues_models.DailyLeague.objects.all():
        totalmembers=eachleague.members.all().count()
        winnerscount =sum(list(accounts_models.Profile.objects.filter(username__DailyLeagueMembers=eachleague).values("leaguescore").annotate(num_books=Count('leaguescore')).order_by("-leaguescore")[:3].values_list("num_books",flat=True)))
        winnersid=list(accounts_models.Profile.objects.filter(username__DailyLeagueMembers=eachleague).order_by("-leaguescore")[:winnerscount])

        totalamount=totalmembers*2
        percent=.3
        samewinner=1
        rank=1
        for i in range(1,winnerscount+1):
            winningamount=(totalamount*percent)/samewinner
            if winnerscount!=i:

                if winnersid[i-1].leaguescore==winnersid[i].leaguescore:
                    samewinner+=1
                else:
                    for k in range(i-samewinner,i):
                        winner=accounts_models.Profile.objects.filter(username=winnersid[k].username)
                        winner.update(piccredits=F('piccredits')+winningamount)
                        notify.send(winner.get().username, recipient=winner.get().username, verb="Hot League Rank :"+str(rank)+", you Won"+str(winningamount)+"PRC")
                    percent-=.05
                    samewinner=1
                    rank+=1

            else:
                for j in range(i-samewinner,i):
                    winner=accounts_models.Profile.objects.filter(username=winnersid[j].username)
                    winner.update(piccredits=F('piccredits')+winningamount)
                    notify.send(winner.get().username, recipient=winner.get().username, verb="Hot League Rank :"+str(rank)+", you Won"+str(winningamount)+"PRC")
    
    Leagues_models.DailyLeague.objects.all().delete()
    print("Daily League Loader done")