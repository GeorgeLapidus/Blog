# Generated by Django 4.0.4 on 2022-06-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_answercomment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.CharField(max_length=200, verbose_name='Пользователь'),
        ),
    ]