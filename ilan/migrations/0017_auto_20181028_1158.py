# Generated by Django 2.1.2 on 2018-10-28 08:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0016_auto_20181028_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='metin',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
