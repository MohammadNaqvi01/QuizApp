# Generated by Django 3.2.5 on 2021-07-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0013_auto_20210718_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='nm',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='q1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='q2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
