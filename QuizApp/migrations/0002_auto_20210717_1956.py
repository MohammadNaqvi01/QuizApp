# Generated by Django 3.2.5 on 2021-07-17 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='q1',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='q2',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]