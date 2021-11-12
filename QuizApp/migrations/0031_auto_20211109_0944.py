# Generated by Django 3.2.5 on 2021-11-09 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0030_alter_question_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizfriendmodel',
            name='category',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='quizfriendmodel',
            name='quest_id',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='quizfriendmodel',
            name='name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='quizfriendmodel',
            name='unique',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QuizApp.quizusermodel'),
        ),
        migrations.AlterField(
            model_name='quizusermodel',
            name='category',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='quizusermodel',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='quizusermodel',
            name='quest_id',
            field=models.CharField(max_length=10),
        ),
    ]
