# Generated by Django 3.2.3 on 2021-06-03 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0012_auto_20210603_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gif',
            name='uploader_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gifs.uploader'),
        ),
    ]
