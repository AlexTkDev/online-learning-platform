# Generated by Django 5.0.6 on 2024-08-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student'), ('Admin', 'Admin')], default='Student', max_length=50),
        ),
    ]
