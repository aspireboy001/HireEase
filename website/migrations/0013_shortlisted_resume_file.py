# Generated by Django 4.2.1 on 2023-05-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_shortlisted_contact_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortlisted',
            name='resume_file',
            field=models.FileField(blank=True, null=True, upload_to='shortlisted_resumes/'),
        ),
    ]
