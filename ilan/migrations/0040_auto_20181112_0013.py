# Generated by Django 2.1.2 on 2018-11-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0039_ilan_ilan_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='ilan_foto',
            field=models.ImageField(default='350x150.png', upload_to='ilan_fotolari'),
        ),
    ]
