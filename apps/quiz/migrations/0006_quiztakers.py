# Generated by Django 3.0.4 on 2020-03-08 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200309_0254'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizTakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiztakername', models.CharField(max_length=1000)),
                ('score', models.IntegerField(default=0)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
            ],
        ),
    ]
