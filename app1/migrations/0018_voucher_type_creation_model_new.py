# Generated by Django 4.1 on 2022-10-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_rename_cbalance_ledger_vouchers_new_c_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher_type_creation_model',
            name='new',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
