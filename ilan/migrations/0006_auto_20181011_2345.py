# Generated by Django 2.1.2 on 2018-10-11 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0005_auto_20181011_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ilani', to=settings.AUTH_USER_MODEL),
        ),
    ]
