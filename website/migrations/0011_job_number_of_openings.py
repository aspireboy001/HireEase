# Generated by Django 4.1.7 on 2023-05-05 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_shortlisted_resume_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='number_of_openings',
            field=models.IntegerField(default=0),
        ),
    ]
