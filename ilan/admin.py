from django.contrib import admin
from django.db import models
from django import forms
# from .forms import IlanAdminForm
from ilan.models import Ilan, Comment
from django_summernote.admin import SummernoteModelAdmin

class IlanAdmin (SummernoteModelAdmin):
    summernote_fields = ('metin', )

admin.site.register(Ilan, IlanAdmin)
admin.site.register(Comment)

