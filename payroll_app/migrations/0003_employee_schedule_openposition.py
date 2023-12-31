# Generated by Django 4.2.6 on 2023-10-06 00:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("payroll_app", "0002_alter_department_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="schedule",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name="OpenPosition",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "id",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=200)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("telephone", models.CharField(blank=True, max_length=20, null=True)),
                ("email", models.EmailField(blank=True, max_length=200, null=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payroll_app.department",
                    ),
                ),
                (
                    "institution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payroll_app.institution",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
