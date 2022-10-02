from tabnanny import verbose
from django.db import models
from django.forms import IntegerField
from django.conf import settings

# Create your models here.
	
class Task(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
	name = models.CharField(max_length=100)
	text =  models.CharField(max_length=200)
	create_date = models.DateTimeField(null = True,auto_now_add=True, blank=True)
	is_complete = models.BooleanField(default=False)
	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'

	def __str__(self):
		return '%s %s %s %s %s %s' % (self.id,self.username,self.name,self.text,self.create_date,self.is_complete)
	