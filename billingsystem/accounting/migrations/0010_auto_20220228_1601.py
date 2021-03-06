# Generated by Django 3.2.12 on 2022-02-28 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0009_rename_ledger_detail_ledger_description_ledgerdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger_description',
            name='ledgerDetail',
        ),
        migrations.CreateModel(
            name='ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledgerDetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.ledgerdetail')),
                ('ledger_description', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounting.ledger_description')),
            ],
        ),
    ]
