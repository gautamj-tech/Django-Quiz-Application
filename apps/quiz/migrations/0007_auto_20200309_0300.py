# Generated by Django 3.0.4 on 2020-03-08 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_quiztakers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuizTakers',
            new_name='QuizTaker',
        ),
    ]
