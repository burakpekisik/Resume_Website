# Generated by Django 4.1.5 on 2024-02-27 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_generalsetting_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsetting',
            name='parameter',
            field=models.CharField(blank=True, default='', max_length=3000, verbose_name='Parameter'),
        ),
    ]
