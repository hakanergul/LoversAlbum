from django.contrib import admin
from django.db import models
# from .forms import IlanAdminForm
from ilan.models import Ilan, Comment
# Register your models here.

admin.site.register(Ilan)
admin.site.register(Comment)

