# Generated by Django 4.0.4 on 2023-10-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartadvisor', '0011_college_university'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='number_of_required_optional_course',
            field=models.IntegerField(default=2),
        ),
    ]
