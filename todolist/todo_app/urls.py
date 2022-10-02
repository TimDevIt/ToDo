from django.contrib import admin
from django.urls import path, include
from . import views 
from django.contrib.auth import views as authViews
urlpatterns = [
   path('',views.index,name='home'),
   path('desk/',views.desk,name='desk'),
   path('register/',views.register,name='register'),
   path('login/',views.user_login,name='login'),
   path('logout/', authViews.LogoutView.as_view(next_page='home'), name='logout'),  
	path('add_task/',views.add_task,name='add_task'),
   path('delete_task/',views.delete_task,name='delete_task'),
   path('edit_task/<int:task_id>/',views.edit_task,name='edit_task')
]