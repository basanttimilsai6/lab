# Generated by Django 4.0.6 on 2023-10-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labreports', '0006_patient_nhpc'),
    ]

    operations = [
        migrations.AddField(
            model_name='hematology',
            name='test',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
