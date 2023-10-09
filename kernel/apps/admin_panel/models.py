from django.db import models

from apps.users.models import MyUser


class Percentage(models.Model):
    default_percentage = models.IntegerField(default=0)
    increase_percentage = models.IntegerField(default=0)
    increase_days = models.IntegerField(default=0)


class PercentageHistory(models.Model):
    default_percentage = models.IntegerField(null=False, blank=False)
    increase_percentage = models.IntegerField(null=False, blank=False)
    increase_days = models.IntegerField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)


class NetWorks(models.Model):
    network_title = models.CharField(max_length=255, null=False, blank=False)


class PaymentMethods(models.Model):
    payment_method_title = models.CharField(max_length=255, null=False, blank=False)
    qr_code = models.ImageField(upload_to='qr_codes/', null=False, blank=False)
    wallet_address = models.CharField(max_length=255, null=False, blank=False)
    method_status = models.BooleanField(default=False)
    network = models.CharField(max_length=255, null=False, blank=False)


class Clients(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    telegram = models.CharField(max_length=255, null=False, blank=False)
    contribution_amount = models.IntegerField(null=False, blank=False)
    payout_amount = models.IntegerField(null=False, blank=False)
    percent = models.IntegerField(null=False, blank=False)
    payment_method_id = models.ForeignKey(PaymentMethods, on_delete=models.CASCADE)
    check_code = models.CharField(max_length=17, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=False)

