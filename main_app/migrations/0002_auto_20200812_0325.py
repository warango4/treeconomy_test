# Generated by Django 3.1 on 2020-08-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dessert',
            name='value',
            field=models.PositiveIntegerField(),
        ),
    ]
