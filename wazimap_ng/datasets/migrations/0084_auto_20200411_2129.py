# Generated by Django 2.2.10 on 2020-04-11 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0083_auto_20200411_2133'),
        ('profile', '0015_auto_20200411_2129'),
        ('points', '0013_auto_20200411_2129'),
    ]

    state_operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
