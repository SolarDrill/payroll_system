# Generated by Django 4.2.6 on 2023-10-06 02:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("payroll_app", "0005_schedule_remove_employee_schedule_employee_schedule"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="schedule",
            new_name="schedules",
        ),
    ]
