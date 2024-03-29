# Generated by Django 4.1.5 on 2024-02-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('info_name', models.CharField(blank=True, default='', help_text='This is personal info name of the variable.', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('parameter', models.CharField(blank=True, default='', max_length=254, verbose_name='Parameter')),
            ],
            options={
                'verbose_name': 'Personal Information',
                'verbose_name_plural': 'Personal Informations',
                'ordering': ('info_name',),
            },
        ),
    ]
