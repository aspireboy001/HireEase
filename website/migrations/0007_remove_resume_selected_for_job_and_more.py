# Generated by Django 4.1.7 on 2023-05-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_company_job_posted_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='selected_for_job',
        ),
        migrations.AddField(
            model_name='resume',
            name='selected_for_job',
            field=models.ManyToManyField(to='website.job'),
        ),
    ]
