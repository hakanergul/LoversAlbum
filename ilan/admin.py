from django.contrib import admin
from django.db import models
from django import forms
# from .forms import IlanAdminForm
from ilan.models import Ilan, Comment
# Register your models here.

class IlanAdmin (admin.ModelAdmin):

    class Media:
        js = ('ckeditor/ckeditor/ckeditor.js','ckeditor/ckeditor/config.js')


admin.site.register(Ilan, IlanAdmin)
admin.site.register(Comment)

