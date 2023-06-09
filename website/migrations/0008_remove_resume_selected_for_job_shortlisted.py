# Generated by Django 4.1.7 on 2023-05-04 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_remove_resume_selected_for_job_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='selected_for_job',
        ),
        migrations.CreateModel(
            name='shortlisted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.job')),
                ('resume_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.resume')),
            ],
        ),
    ]
