# Generated by Django 4.1 on 2022-10-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_remove_total_balance_ledger_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_balance',
            name='c_balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='total_balance',
            name='c_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
