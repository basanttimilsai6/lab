# Generated by Django 4.0.6 on 2023-10-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labreports', '0005_alter_test_bt_alter_test_ct'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='nhpc',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Ms.', 'Ms.'), ('Miss', 'Miss')], max_length=5, null=True),
        ),
    ]