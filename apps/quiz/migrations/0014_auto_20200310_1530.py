# Generated by Django 3.0.4 on 2020-03-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='option',
        ),
        migrations.AddField(
            model_name='question',
            name='option1',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option2',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option3',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='option4',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
