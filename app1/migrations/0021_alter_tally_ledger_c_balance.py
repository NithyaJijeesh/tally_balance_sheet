# Generated by Django 4.1 on 2022-10-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_remove_ledger_vouchers_new_c_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tally_ledger',
            name='c_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]