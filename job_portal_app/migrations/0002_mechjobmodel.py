# Generated by Django 4.2 on 2024-12-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mechJobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Package', models.IntegerField()),
                ('Experiance', models.FloatField()),
                ('Opnnings', models.IntegerField()),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
    ]
