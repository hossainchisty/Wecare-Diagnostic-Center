# Generated by Django 4.1 on 2023-02-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="password",
            field=models.CharField(max_length=100),
        ),
    ]