# Generated by Django 2.2.10 on 2020-03-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_choroplethmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choroplethmethod',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]