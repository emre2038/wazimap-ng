# Generated by Django 2.2.8 on 2020-01-20 16:21

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boundaries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=5)),
                ('code', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=100)),
                ('long_name', models.CharField(max_length=200)),
                ('province_code', models.CharField(max_length=50)),
                ('pr_code_st', models.CharField(max_length=1)),
                ('province', models.CharField(max_length=50)),
                ('area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=-1)),
            ],
        ),
    ]
