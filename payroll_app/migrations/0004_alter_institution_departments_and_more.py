# Generated by Django 4.2.6 on 2023-10-06 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("payroll_app", "0003_employee_schedule_openposition"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="departments",
            field=models.ManyToManyField(blank=True, to="payroll_app.department"),
        ),
        migrations.AlterField(
            model_name="institution",
            name="employees",
            field=models.ManyToManyField(blank=True, to="payroll_app.employee"),
        ),
        migrations.AlterField(
            model_name="institution",
            name="positions",
            field=models.ManyToManyField(blank=True, to="payroll_app.position"),
        ),
        migrations.AlterField(
            model_name="openposition",
            name="department",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="payroll_app.department",
            ),
        ),
    ]
