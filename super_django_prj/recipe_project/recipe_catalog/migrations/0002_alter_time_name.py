# Generated by Django 4.2.16 on 2024-11-15 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='name',
            field=models.TimeField(),
        ),
    ]
