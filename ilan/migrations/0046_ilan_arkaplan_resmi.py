# Generated by Django 2.1.2 on 2018-12-21 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0045_ilan_arkaplan_rengi'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilan',
            name='arkaplan_resmi',
            field=models.ImageField(blank=True, upload_to='ilan_fotolari/'),
        ),
    ]