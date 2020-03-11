# Generated by Django 3.0.4 on 2020-03-10 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_auto_20200310_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizmakers',
            name='quizques',
        ),
        migrations.AddField(
            model_name='quizmakers',
            name='quizques',
            field=models.ForeignKey(default=38, on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
            preserve_default=False,
        ),
    ]
