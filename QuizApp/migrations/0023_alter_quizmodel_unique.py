# Generated by Django 3.2.5 on 2021-07-28 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0022_quizfriendmodel_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='unique',
            field=models.CharField(default=1, max_length=10),
        ),
    ]