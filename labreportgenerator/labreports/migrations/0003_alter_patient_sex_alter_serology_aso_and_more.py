# Generated by Django 4.0.6 on 2023-10-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labreports', '0002_remove_report_created_at_patient_custom_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='aso',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='crp',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='dengue_igg_igm',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='dengue_ns1_ag',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='h_pylori_igg_igm',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='hbsag',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='hcv',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='hiv_1_2_ab',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='hiv_i_ii',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='ra',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='scrub_typhus_igg_igm',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='typhoid_igg_igm',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='serology',
            name='vdrl_rpr',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='stool',
            name='blood',
            field=models.CharField(blank=True, choices=[('', ''), ('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT')], help_text='Blood presence (Present or Absent)', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stool',
            name='consistency',
            field=models.CharField(blank=True, choices=[('', ''), ('LOOSE', 'LOOSE'), ('SOLID', 'SOLID'), ('SEMI-SOLID', 'SEMI-SOLID')], help_text='Stool consistency (loose, solid, semi-solid)', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stool',
            name='mucus',
            field=models.CharField(blank=True, choices=[('', ''), ('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT')], help_text='Mucus presence (Present or Absent)', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='blood_group_rh',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='rdt_for_mp',
            field=models.CharField(blank=True, choices=[('POSITIVE', 'POSITIVE'), ('NEGATIVE', 'NEGATIVE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='urine',
            name='appearance',
            field=models.CharField(blank=True, choices=[('', ''), ('CLEAR', 'CLEAR'), ('S.TURBID', 'S.TURBID'), ('TURBID', 'TURBID'), ('CLOUDY', 'CLOUDY')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='urine',
            name='color',
            field=models.CharField(blank=True, choices=[('', ''), ('L.YELLOW', 'L.YELLOW'), ('D.YELLOW', 'D.YELLOW'), ('WATERY', 'WATERY'), ('YELLOWISH', 'YELLOWISH'), ('REDDISH', 'REDDISH')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='urine',
            name='protein',
            field=models.CharField(blank=True, choices=[('', ''), ('NIL', 'NIL'), ('TRACE', 'TRACE'), ('1+', '1+'), ('2+', '2+'), ('3+', '3+'), ('4+', '4+')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='urine',
            name='reaction',
            field=models.CharField(blank=True, choices=[('', ''), ('ACIDIC', 'ACIDIC'), ('ALKALINE', 'ALKALINE')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='urine',
            name='sugar',
            field=models.CharField(blank=True, choices=[('', ''), ('NIL', 'NIL'), ('TRACE', 'TRACE'), ('1+', '1+'), ('2+', '2+'), ('3+', '3+'), ('4+', '4+')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='widaltest',
            name='anti_ah',
            field=models.CharField(blank=True, choices=[('NEGATIVE', 'NEGATIVE'), ('1:80', '1:80'), ('1:160', '1:160'), ('1:320', '1:320')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='widaltest',
            name='anti_bh',
            field=models.CharField(blank=True, choices=[('NEGATIVE', 'NEGATIVE'), ('1:80', '1:80'), ('1:160', '1:160'), ('1:320', '1:320')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='widaltest',
            name='anti_h',
            field=models.CharField(blank=True, choices=[('NEGATIVE', 'NEGATIVE'), ('1:80', '1:80'), ('1:160', '1:160'), ('1:320', '1:320')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='widaltest',
            name='anti_o',
            field=models.CharField(blank=True, choices=[('NEGATIVE', 'NEGATIVE'), ('1:80', '1:80'), ('1:160', '1:160'), ('1:320', '1:320')], max_length=10, null=True),
        ),
    ]
