# Generated by Django 2.2.10 on 2020-04-11 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0079_delete_indicatorcategory'),
    ]

    database_operations = [
        migrations.AlterModelTable('IndicatorSubcategory', 'profile_indicatorsubcategory'),  
    ]

    state_operations = [

    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
