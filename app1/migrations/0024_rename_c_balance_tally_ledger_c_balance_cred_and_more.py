# Generated by Django 4.1 on 2022-10-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_remove_tally_ledger_c_blnc_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tally_ledger',
            old_name='c_balance',
            new_name='c_balance_cred',
        ),
        migrations.AddField(
            model_name='tally_ledger',
            name='c_balance_deb',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]