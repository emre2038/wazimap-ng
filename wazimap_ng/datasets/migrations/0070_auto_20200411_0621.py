# Generated by Django 2.2.10 on 2020-04-11 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0069_auto_20200410_2016'),
    ]

    database_operations = [
        migrations.AlterModelTable('ProfileHighlight', 'profile_profilehighlight')
    ]

    state_operations = [
        migrations.DeleteModel('ProfileHighlight')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
