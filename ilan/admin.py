from django.contrib import admin
from .forms import IlanAdminForm
from ilan.models import Ilan, Comment
# Register your models here.

class IlanAdmin (admin.ModelAdmin):
    form = IlanAdminForm
    class Media:
        js = ('ckeditor/ckeditor/ckeditor.js',)

admin.site.register(Ilan, IlanAdmin)
admin.site.register(Comment)

