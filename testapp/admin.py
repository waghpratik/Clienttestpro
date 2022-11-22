from django.contrib import admin
from . models import Project_model,userpro

# Register your models here.

@admin.register(Project_model)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','desc']


@admin.register(userpro)
class BlogAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name']