# Generated by Django 2.0.4 on 2018-05-06 11:58

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('sems', '0002_auto_20180506_1157'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Programs',
            new_name='Program',
        ),
    ]
