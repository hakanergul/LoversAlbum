# Generated by Django 2.1.2 on 2018-10-28 08:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0015_auto_20181027_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='metin',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
