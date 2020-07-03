from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class PostDetail(models.Model):
	username=models.ForeignKey(User,null=True,related_name="PostDetail", on_delete=models.CASCADE)
	postpicture=models.ImageField(upload_to='postpic')
	time=models.DateTimeField(auto_now_add=True)
	comment=models.TextField(blank=True,null=True)
	def __str__(self):
		return self.username.username


	def timesince(self, now=None):
		"""
		Shortcut for the ``django.utils.timesince.timesince`` function of the
		current timestamp.
		"""
		from django.utils.timesince import timesince as timesince_
		return timesince_(self.time, now)


 


class Comment(models.Model):
	post = models.ForeignKey(PostDetail, on_delete=models.CASCADE, related_name='comments')
	username = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)

	def __str__(self):
		return self.username.username


	def timesince(self, now=None):
		"""
		Shortcut for the ``django.utils.timesince.timesince`` function of the
		current timestamp.
		"""
		from django.utils.timesince import timesince as timesince_
		return timesince_(self.created_date, now)
