# Generated by Django 4.0.6 on 2022-08-24 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='jopposition',
            new_name='jobposition',
        ),
    ]