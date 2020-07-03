from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  



# Create your models here.
class Profile(models.Model):
	username=models.OneToOneField(User,null=True,related_name='Profile',on_delete=models.CASCADE,unique=True)
	profilepicture=models.ImageField(upload_to='profilepic',default='facebook-default-no-profile-pic1.jpg')
	profilestatus = models.IntegerField(default=1,null=True)
	profilescore = models.DecimalField(default=10,decimal_places=3,max_digits=8)
	piccredits=models.DecimalField(default=2,decimal_places=1,max_digits=6)
	leaguescore=models.DecimalField(default=0,decimal_places=3,max_digits=6)
	dailyleaguescore=models.DecimalField(default=0,decimal_places=3,max_digits=6)
	def __str__(self):
		return self.username.username


class fanandfanned(models.Model):
	fans= models.ForeignKey(User, related_name='fans',on_delete=models.CASCADE,null=True)
	fanned = models.ManyToManyField(User, related_name='fanned',blank=True)
	def __str__(self):
		return self.fans.username







