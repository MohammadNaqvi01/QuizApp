# Generated by Django 3.2.5 on 2021-11-11 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0036_alter_quizfriendmodel_user_belong_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizfriendmodel',
            name='user_belong_to',
        ),
        migrations.AlterField(
            model_name='quizfriendmodel',
            name='unique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.quizusermodel'),
        ),
    ]
