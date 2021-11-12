# Generated by Django 3.2.5 on 2021-11-11 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0034_auto_20211109_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizfriendmodel',
            name='user_belong_to',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='QuizApp.quizusermodel'),
        ),
        migrations.AlterField(
            model_name='quizfriendmodel',
            name='unique',
            field=models.CharField(default='1', max_length=50),
        ),
    ]