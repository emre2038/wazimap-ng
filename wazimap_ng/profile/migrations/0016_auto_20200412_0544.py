# Generated by Django 2.2.10 on 2020-04-12 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0015_auto_20200411_2129'),
        ('points', '0013_auto_20200411_2129'),
    ]

    operations = [
    ]


    database_operations = [
        migrations.AlterModelTable('Licence', 'datasets_licence'),  
    ]

    state_operations = [

    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
