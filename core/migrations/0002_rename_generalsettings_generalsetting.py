# Generated by Django 4.1.5 on 2023-02-23 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralSettings',
            new_name='GeneralSetting',
        ),
    ]
