# Generated by Django 4.0.6 on 2022-08-24 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0003_jobpost_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='content',
            field=models.TextField(verbose_name='채용내용'),
        ),
    ]