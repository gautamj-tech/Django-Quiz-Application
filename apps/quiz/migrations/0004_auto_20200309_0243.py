# Generated by Django 3.0.4 on 2020-03-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quizmaker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmaker',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]