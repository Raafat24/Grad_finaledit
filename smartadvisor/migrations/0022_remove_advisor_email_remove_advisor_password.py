# Generated by Django 4.0.4 on 2023-11-22 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartadvisor', '0021_advisor_email_advisor_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advisor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='advisor',
            name='password',
        ),
    ]
