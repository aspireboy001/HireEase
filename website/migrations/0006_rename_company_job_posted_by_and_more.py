# Generated by Django 4.1.7 on 2023-05-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_recruiter_last_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='company',
            new_name='posted_by',
        ),
        migrations.AlterField(
            model_name='job',
            name='eligibility_criteria',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='job',
            name='skills_required',
            field=models.CharField(max_length=500),
        ),
    ]