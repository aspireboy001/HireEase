# Generated by Django 4.1.7 on 2023-04-29 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_company_username_remove_recruiter_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]