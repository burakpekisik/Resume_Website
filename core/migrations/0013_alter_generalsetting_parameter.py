# Generated by Django 4.1.5 on 2024-02-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_delete_personalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalsetting',
            name='parameter',
            field=models.CharField(blank=True, default='', max_length=1000, verbose_name='Parameter'),
        ),
    ]
