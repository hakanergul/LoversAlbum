from django import forms
from django.contrib.auth import get_user_model
from ilan.models import Ilan, Comment
from django.conf import settings

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class IlanForm(forms.ModelForm):
    metin = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Ilan
        fields = ['baslik', 'metin', 'ilan_foto']

class IlanAdminForm(forms.ModelForm):
    metin = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Ilan
        fields = ['baslik', 'metin', 'ilan_foto']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['yorum_metni']

