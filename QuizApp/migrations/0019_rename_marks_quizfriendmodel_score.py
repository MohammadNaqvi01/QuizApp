# Generated by Django 3.2.5 on 2021-07-22 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0018_rename_unique_quizfriendmodel_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizfriendmodel',
            old_name='marks',
            new_name='score',
        ),
    ]
