# Generated by Django 2.1.2 on 2018-10-05 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0002_auto_20180929_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
