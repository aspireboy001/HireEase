# Generated by Django 4.2.1 on 2023-05-29 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_delete_shortlisted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortlisted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_score', models.DecimalField(decimal_places=5, default=0, max_digits=7)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('resume_file', models.FileField(blank=True, null=True, upload_to='shortlisted_resumes/')),
                ('Interview_Person', models.CharField(blank=True, max_length=100)),
                ('Date', models.DateField(blank=True)),
                ('Time', models.TimeField(blank=True)),
                ('Status', models.CharField(blank=True, max_length=100)),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.job')),
                ('resume_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.resume')),
            ],
        ),
    ]