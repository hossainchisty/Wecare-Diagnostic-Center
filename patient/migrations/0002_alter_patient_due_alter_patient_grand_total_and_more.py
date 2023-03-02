# Generated by Django 4.0.10 on 2023-03-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='due',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='grand_total',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='paid_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=15, null=True),
        ),
    ]
