# Generated by Django 3.2.5 on 2021-07-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0005_auto_20210718_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='nm',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='q1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='q2',
            field=models.CharField(max_length=10),
        ),
    ]
