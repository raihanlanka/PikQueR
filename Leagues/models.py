from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  


class FreeLeague(models.Model):
	categoryname= models.CharField(max_length=200,null=True)
	members=models.ManyToManyField(User, related_name='FreeLeagueMembers',blank=True)
	category=models.CharField(max_length=20,null=True)
	time = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.categoryname


class MegaLeague(models.Model):
	categoryname= models.CharField(max_length=200,null=True)
	members=models.ManyToManyField(User, related_name='MegaLeagueMembers',blank=True)
	time = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.categoryname


class HotLeague(models.Model):
	categoryname= models.CharField(max_length=200,null=True)
	members=models.ManyToManyField(User, related_name='HotLeagueMembers',blank=True)
	time = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.categoryname


class DailyLeague(models.Model):
	categoryname= models.CharField(max_length=200,null=True)
	members=models.ManyToManyField(User, related_name='DailyLeagueMembers',blank=True)
	time = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.categoryname

class Winners(models.Model):
	winnerleaguename=models.CharField(max_length=200,null=True)
	winningmembers=models.ForeignKey(User, related_name='winner',on_delete=models.CASCADE,null=True,blank=True)
	category=models.CharField(max_length=20,null=True)
	leaguescore=models.DecimalField(default=0,decimal_places=3,max_digits=19)
	def __str__(self):
		return str(self.winnerleaguename)


class FreeLeagueChat(models.Model):
    league = models.ForeignKey(FreeLeague, on_delete=models.CASCADE, related_name='FreeLeagueChat')
    username = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username.username
