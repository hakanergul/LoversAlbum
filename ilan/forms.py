from django import forms
from django.contrib.auth import get_user_model
from ilan.models import Ilan, Comment
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from tinymce.models import HTMLField

class IlanForm(forms.ModelForm):
    metin = HTMLField()
    class Meta:
        model = Ilan
        fields = ['baslik', 'metin', 'ilan_foto', 'ilan_fon_muzik', 'arkaplan_rengi', 'arkaplan_resmi']
        labels = {
            'baslik': _('Başlık'),
            'metin': _('İlan Metni'),
            'ilan_foto': _('İlan Görseli'),
            'ilan_fon_muzik': _('Fon Müziği'),
            'arkaplan_rengi': _('Arkaplan Rengi'),
            'arkaplan_resmi': _('Arkaplan Resmi'),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['yorum_metni']

