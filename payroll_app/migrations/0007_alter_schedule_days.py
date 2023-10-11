# Generated by Django 4.2.6 on 2023-10-06 02:54

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("payroll_app", "0006_rename_schedule_employee_schedules"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="days",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    (0, "Domingo"),
                    (1, "Lunes"),
                    (2, "Martes"),
                    (3, "Miercoles"),
                    (4, "Jueves"),
                    (5, "Viernes"),
                    (6, "Sabado"),
                ],
                max_length=100,
                verbose_name="Dia de la semana",
            ),
        ),
    ]