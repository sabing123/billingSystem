# Generated by Django 3.2.12 on 2022-02-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ledgerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200, null=True)),
                ('c_FY', models.CharField(max_length=200, null=True)),
                ('c_date_form_start', models.CharField(max_length=200, null=True)),
                ('c_date_form_end', models.CharField(max_length=200, null=True)),
                ('c_code', models.CharField(max_length=200, null=True)),
                ('c_description', models.CharField(max_length=200, null=True)),
                ('c_current_date', models.CharField(max_length=200, null=True)),
                ('c_debt_amt', models.CharField(max_length=200, null=True)),
                ('c_credit_amt', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
