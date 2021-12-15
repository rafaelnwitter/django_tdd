# Generated by Django 4.0 on 2021-12-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='domestico',
            field=models.CharField(default='N/A', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='nome_animal',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='predador',
            field=models.CharField(default='N/A', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='venenoso',
            field=models.CharField(default='N/A', max_length=5),
            preserve_default=False,
        ),
    ]
