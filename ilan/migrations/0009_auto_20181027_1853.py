# Generated by Django 2.1.2 on 2018-10-27 15:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0008_auto_20181027_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='metin',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
