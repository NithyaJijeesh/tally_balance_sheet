# Generated by Django 4.1 on 2022-10-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_remove_voucher_type_creation_model_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledger_vouchers_new',
            name='c_balance',
        ),
        migrations.AddField(
            model_name='tally_ledger',
            name='c_balance',
            field=models.IntegerField(null=True),
        ),
    ]
