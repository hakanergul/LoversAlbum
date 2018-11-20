# Generated by Django 2.1.2 on 2018-10-29 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ilan', '0025_ilan_yayinlandimi'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutlulukDile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='begeniler', to='ilan.Ilan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='begenileri', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='ilan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ilan_yorumlari', to='ilan.Ilan'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlari', to=settings.AUTH_USER_MODEL),
        ),
    ]
