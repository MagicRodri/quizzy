# Generated by Django 4.1.3 on 2022-12-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_alter_option_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='options',
            field=models.ManyToManyField(to='quizzes.option'),
        ),
    ]