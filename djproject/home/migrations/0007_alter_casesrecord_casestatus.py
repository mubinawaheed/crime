# Generated by Django 3.2.5 on 2021-08-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210812_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casesrecord',
            name='CaseStatus',
            field=models.BooleanField(default=0),
        ),
    ]