# Generated by Django 3.2.12 on 2022-02-28 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0011_ledger_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledger_description',
            name='ledgerDetail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.ledgerdetail'),
        ),
    ]
