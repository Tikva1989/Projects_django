# Generated by Django 3.2.3 on 2021-06-03 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0005_auto_20210602_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploader',
            name='emp_image',
        ),
        migrations.AddField(
            model_name='uploader',
            name='uploader_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/'),
            preserve_default=False,
        ),
    ]