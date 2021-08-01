# Generated by Django 3.2.5 on 2021-07-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0015_alter_quizmodel_nm'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='unique',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='nm',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='q1',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='quizmodel',
            name='q2',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]