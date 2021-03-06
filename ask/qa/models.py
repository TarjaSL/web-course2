from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField(default=1)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User, related_name='likes_set')
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return '/quest/%d/' % self.pk
	class Meta:
		db_table = 'question'		

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
	def __unicode__(self):
		return self.title
	def get_absolute_url(self):
		return '/ans/%d/' % self.pk
	class Meta:
		db_table = 'answer'	