# Generated by Django 4.1 on 2022-10-09 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_ledger_vouchers_new_cb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ledger_vouchers_new',
            old_name='cb',
            new_name='cbalance',
        ),
        migrations.RemoveField(
            model_name='ledger_vouchers_new',
            name='closing_balance',
        ),
    ]
