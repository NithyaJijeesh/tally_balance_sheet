# Generated by Django 4.1 on 2022-10-05 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_ledger_voucher_values'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ledger_voucher_values',
        ),
    ]