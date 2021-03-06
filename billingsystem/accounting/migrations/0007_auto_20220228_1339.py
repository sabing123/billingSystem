# Generated by Django 3.2.12 on 2022-02-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_rename_ledger_descriptio_ledger_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledgerdetail',
            name='c_FY_end',
        ),
        migrations.RemoveField(
            model_name='ledgerdetail',
            name='c_FY_start',
        ),
        migrations.AlterField(
            model_name='ledger_description',
            name='c_credit_amt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ledger_description',
            name='c_current_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ledger_description',
            name='c_debt_amt',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ledgerdetail',
            name='c_code',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='ledgerdetail',
            name='c_date_form_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ledgerdetail',
            name='c_date_form_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
