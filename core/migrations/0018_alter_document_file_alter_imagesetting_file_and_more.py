# Generated by Django 4.1.5 on 2024-03-24 08:41

from django.db import migrations, models
import resume.custom_storage


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_project_options_project_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, default='', storage=resume.custom_storage.DocumentStorage(), upload_to='', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='imagesetting',
            name='file',
            field=models.ImageField(blank=True, default='', storage=resume.custom_storage.ImageSettingStorage(), upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='file',
            field=models.ImageField(blank=True, default='', storage=resume.custom_storage.ProjectSettingStorage(), upload_to='', verbose_name='Image'),
        ),
    ]
