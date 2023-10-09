from rest_framework import serializers
from .models import Percentage, PercentageHistory, NetWorks, PaymentMethods, Clients


class PercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Percentage
        fields = '__all__'


class PercentageHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PercentageHistory
        fields = '__all__'


class NetWorksSerializer(serializers.ModelSerializer):

    class Meta:
        model = NetWorks
        fields = '__all__'


class PaymentMethodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentMethods
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = '__all__'
