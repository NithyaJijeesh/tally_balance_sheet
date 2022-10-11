# Generated by Django 4.1 on 2022-10-10 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_tally_ledger_c_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='total_balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_debit', models.IntegerField(null=True)),
                ('total_credit', models.IntegerField(null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_group')),
                ('ledger', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_ledger')),
                ('voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger_voucher')),
            ],
        ),
    ]
