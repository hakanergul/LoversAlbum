# Generated by Django 2.1.2 on 2018-12-22 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0047_auto_20181222_0250'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilan',
            name='arkaplan_resmi',
            field=models.ImageField(blank=True, upload_to='ilan_fotolari/'),
        ),
    ]