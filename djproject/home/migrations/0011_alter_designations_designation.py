# Generated by Django 3.2.4 on 2021-09-08 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_suspectrecord_suspect_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designations',
            name='Designation',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
