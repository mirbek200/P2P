from .models import Percentage, NetWorks, PaymentMethods, Clients, PercentageHistory
from .serializers import (PercentageSerializer, NetWorksSerializer, PaymentMethodsSerializer, ClientsSerializer,
                          PercentageHistorySerializer)
from rest_framework import generics
from rest_framework import permissions


# Percentage

class PercentageListView(generics.ListAPIView):
    queryset = Percentage.objects.all()
    serializer_class = PercentageSerializer


class PercentageUpdateView(generics.UpdateAPIView):
    queryset = Percentage.objects.all()
    serializer_class = PercentageSerializer
    permission_classes = [permissions.IsAdminUser]


# NetWorks
class NetWorksListCreateView(generics.ListCreateAPIView):
    queryset = NetWorks.objects.all()
    serializer_class = NetWorksSerializer
    permission_classes = [permissions.IsAdminUser]


class NetWorksRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NetWorks.objects.all()
    serializer_class = NetWorksSerializer
    permission_classes = [permissions.IsAdminUser]


# PaymentMethods
class PaymentMethodsListView(generics.ListAPIView):
    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentMethodsCreateView(generics.CreateAPIView):
    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer
    permission_classes = [permissions.IsAdminUser]


class PaymentMethodsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer
    permission_classes = [permissions.IsAdminUser]


# Clients
class ClientsListView(generics.ListAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [permissions.IsAdminUser]


class ClientsCreateView(generics.CreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientsUpdateView(generics.UpdateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    permission_classes = [permissions.IsAdminUser]


# Percentage History

class PercentageHistoryListCreateView(generics.ListCreateAPIView):
    queryset = PercentageHistory.objects.all()
    serializer_class = PercentageHistorySerializer
    permission_classes = [permissions.IsAdminUser]


class PercentageHistoryDeleteView(generics.DestroyAPIView):
    queryset = PercentageHistory.objects.all()
    serializer_class = PercentageHistorySerializer
    permission_classes = [permissions.IsAdminUser]
