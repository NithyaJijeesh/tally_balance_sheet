# Generated by Django 4.1 on 2022-10-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_alter_tally_ledger_c_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='tally_ledger',
            name='c_blnc_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
