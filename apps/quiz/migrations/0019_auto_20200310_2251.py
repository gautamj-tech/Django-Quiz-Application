# Generated by Django 3.0.4 on 2020-03-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0018_auto_20200310_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmakers',
            name='quizques',
        ),
        migrations.AddField(
            model_name='quizmakers',
            name='quizques',
            field=models.ManyToManyField(blank=True, to='quiz.Question'),
        ),
    ]
