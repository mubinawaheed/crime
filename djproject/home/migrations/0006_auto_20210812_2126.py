# Generated by Django 3.2.5 on 2021-08-12 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_prisonerrecord_crminalcnic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casesrecord',
            old_name='EVidence',
            new_name='Evidence',
        ),
        migrations.RenameField(
            model_name='work_force',
            old_name='officer_ID',
            new_name='officer',
        ),
        migrations.RemoveField(
            model_name='casesrecord',
            name='officer_ID',
        ),
        migrations.AddField(
            model_name='casesrecord',
            name='officer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.work_force'),
        ),
    ]
