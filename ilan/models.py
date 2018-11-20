from django.db import models
from django.urls.base import reverse
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

class Ilan(models.Model):
    baslik = models.CharField(max_length=30)
    metin =  RichTextUploadingField()
    ilan_foto = models.ImageField(upload_to='ilan_fotolari', default='350x150.png')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mutluluk_dileyenler = models.ManyToManyField(settings.AUTH_USER_MODEL, blank= True, related_name = 'mutluluk_dilenen_ilan')
    goruntulenme = models.PositiveIntegerField(default = 0)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    yayinlandimi = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("ilan:ilan_goster", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.olusturma_tarihi)

    def __unicode__(self):
        return self.metin


class Comment(models.Model):
    ilan = models.ForeignKey(Ilan, on_delete=models.CASCADE, related_name='yorumlar')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='yorumlari')
    yorum_metni = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return str(self.ilan.baslik)+ " -> " +str(self.user)
