# Generated by Django 2.1.2 on 2018-11-05 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0033_auto_20181105_0429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ilan',
            name='mutluluk_dileyenler',
        ),
        migrations.AddField(
            model_name='ilan',
            name='mutluluk_dile',
            field=models.ManyToManyField(related_name='mutluluk_dilenen_ilan', to='ilan.MutlulukDile'),
        ),
    ]
