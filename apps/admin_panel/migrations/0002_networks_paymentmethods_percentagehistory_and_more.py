# Generated by Django 4.2.4 on 2023-09-18 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method_title', models.CharField(max_length=255)),
                ('qr_code', models.ImageField(upload_to='qr_codes/')),
                ('wallet_address', models.CharField(max_length=255)),
                ('method_status', models.BooleanField(default=False)),
                ('network', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PercentageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_percentage', models.IntegerField()),
                ('increase_percentage', models.IntegerField()),
                ('increase_days', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Persentage',
            new_name='Percentage',
        ),
        migrations.RenameField(
            model_name='percentage',
            old_name='default_persentage',
            new_name='default_percentage',
        ),
        migrations.RenameField(
            model_name='percentage',
            old_name='increase_persentage',
            new_name='increase_percentage',
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.CharField(max_length=255)),
                ('contribution_amount', models.IntegerField()),
                ('payout_amount', models.IntegerField()),
                ('percent', models.IntegerField()),
                ('check_code', models.CharField(blank=True, max_length=17, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('payment_method_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.paymentmethods')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]