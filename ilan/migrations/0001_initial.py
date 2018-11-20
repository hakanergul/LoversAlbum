# Generated by Django 2.1.1 on 2018-09-29 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ilan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=40)),
                ('metin', models.TextField()),
                ('olusturma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('gosterim_sayisi', models.IntegerField(default=0)),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
