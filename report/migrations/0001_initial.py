# Generated by Django 4.1 on 2023-02-05 14:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("doctor", "0002_alter_doctor_password"),
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lab",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ("title", models.CharField(max_length=30)),
                ("report", models.TextField()),
                ("price", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ("commission", models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ("date", models.DateField(default="2023-02-05")),
                (
                    "report_status",
                    models.CharField(
                        choices=[
                            ("sample collected", "Sample Collected"),
                            ("completed", "Completed"),
                            ("delivered", "Delivered"),
                        ],
                        max_length=30,
                    ),
                ),
                ("patient", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="patient.patient")),
                (
                    "referred_by_doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doctor.doctor", verbose_name="Refd By Doctor"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
    ]
