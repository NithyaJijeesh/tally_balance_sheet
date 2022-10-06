# Generated by Django 4.1 on 2022-10-05 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_ledger_vouchers_new_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='ledger_voucher_values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_balance', models.IntegerField()),
                ('debit', models.IntegerField(null=True)),
                ('credit', models.IntegerField(null=True)),
                ('closing_balance', models.IntegerField()),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_ledger')),
                ('vocher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger_vouchers_new')),
            ],
        ),
    ]