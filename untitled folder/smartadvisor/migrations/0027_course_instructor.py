# Generated by Django 4.0.4 on 2023-11-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartadvisor', '0026_alter_course_code_alter_student_university_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.BooleanField(default=True),
        ),
    ]
