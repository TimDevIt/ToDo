
from datetime import timezone,datetime
from urllib import request
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from .forms import EditTaskForm, UserRegistrationForm,UserLoginForm,AddTaskForm
from .models import Task
# Create your views here.

def index(request):
	return render(request,'todo_app/index.html')

def desk(request):
	if request.user.is_authenticated:
		user_id = request.user.id
		task_list = Task.objects.filter(username = user_id)
		context = {'task_list' : task_list}
		return render(request, 'todo_app/desk.html', context)
	return render(request,'todo_app/desk.html')

def add_task(request):
	form = AddTaskForm()
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = AddTaskForm(request.POST)
			if form.is_valid():
				task = form.save()
				task.username = request.user
				task.created_date = datetime.now()
				task.is_complete = False
				task.save()
				return redirect('desk')
	else:
		form = AddTaskForm()
	return render(request,'todo_app/add_task.html',{'form': form})	

def edit_task(request,task_id):
	if request.user.is_authenticated:
		user = request.user.id
		task = Task.objects.get(id = task_id,username = user)
		form = AddTaskForm(instance=task)
		if request.method == 'POST':
			form = AddTaskForm(request.POST)
			if form.is_valid():
				new_task = form.save()
				task.name = new_task.name
				task.text = new_task.text
				task.save(update_fields=["name","text"])
				return redirect('desk')
	else:
		return HttpResponse("Вы не вошли в систему(");
	return render(request,'todo_app/edit_task.html',{'form': form})	

def delete_task(request):
	if request.user.is_authenticated:
		if request.method == 'GET':
			task_id = request.GET.get('task_id',None)
			Task.objects.get(id = task_id,username=request.user.id).delete()
			data = {
				'deleted' : True,
			}
			return JsonResponse(data);

def register(request):
	form = UserRegistrationForm()
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('desk')
	else:
		form = UserRegistrationForm()
	
	return render(request,'todo_app/register.html',{'form': form})

def user_login(request):
	if not request.user.is_authenticated:
		if request.method == 'POST':
			form = UserLoginForm(request=request,data=request.POST)
			if form.is_valid():
				uname = form.cleaned_data['username']
				upass = form.cleaned_data.get('password')
				user = authenticate(username=uname, password=upass)
				if user is not None:
					login(request,user)
					return redirect('desk')
		else:
			form = UserLoginForm()
	else:
		return redirect('desk')
	return render(request,'todo_app/login.html',{'form': form})

def logout_view(request):
    logout(request)




