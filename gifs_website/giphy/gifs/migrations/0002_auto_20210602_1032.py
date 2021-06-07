# Generated by Django 3.2.3 on 2021-06-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gif',
            name='categories',
            field=models.ManyToManyField(to='gifs.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='gifs',
            field=models.ManyToManyField(to='gifs.Gif'),
        ),
    ]
