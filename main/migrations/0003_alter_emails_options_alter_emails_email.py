# Generated by Django 4.0.4 on 2022-05-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_emails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emails',
            options={'verbose_name': 'Адрес электронной почты', 'verbose_name_plural': 'Адреса электронной почты'},
        ),
        migrations.AlterField(
            model_name='emails',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
    ]
