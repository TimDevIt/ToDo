from urllib import request
from wsgiref.headers import tspecials
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms import ModelForm, TextInput, Textarea
from .models import Task

class UserRegistrationForm(UserCreationForm):
   class Meta:
      model = User
      fields = ('username', 'first_name', 'email')

class UserLoginForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

class AddTaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ('name','text')
		labels = {
         'name': 'Задача:',
			'text': 'Описание:'
      }
		widgets = {
         'name': TextInput(attrs={'size': '40'}),
			'text': Textarea(attrs={'cols': 80, 'rows': 20}),
      }

class EditTaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ('name','text')
		labels = {
         'name': 'Задача:',
			'text': 'Описание:'
      }
		widgets = {
         'name': TextInput(attrs={'size': '40'}),
			'text': Textarea(attrs={'cols': 80, 'rows': 20}),
      }
		