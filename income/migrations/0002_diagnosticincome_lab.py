# Generated by Django 4.1.6 on 2023-03-01 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("laboratory", "0003_reporttestinglist_reportlistcart_labcart"),
        ("income", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="diagnosticincome",
            name="lab",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="laboratory.lab",
            ),
        ),
    ]
