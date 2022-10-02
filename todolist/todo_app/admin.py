from django.contrib import admin

from .models import Task 
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'name','text','create_date','is_complete')
	fields = ['id', 'username', 'name','text','create_date','is_complete']
	readonly_fields = ['id','create_date']

admin.site.register(Task,TaskAdmin)
