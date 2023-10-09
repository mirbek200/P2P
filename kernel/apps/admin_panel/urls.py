from django.urls import path
from .views import (PercentageListView, PercentageUpdateView, NetWorksListCreateView, NetWorksRetrieveUpdateDestroyView,
                    PaymentMethodsListView, PaymentMethodsCreateView, PaymentMethodsRetrieveUpdateDestroyView,
                    ClientsListView, ClientsCreateView, ClientsUpdateView,
                    PercentageHistoryDeleteView, PercentageHistoryListCreateView)

urlpatterns = [
    path('persentage_list/', PercentageListView.as_view(), name='persentage_list'),
    path('persentage_update/<int:pk>/', PercentageUpdateView.as_view(), name='persentage_update'),

    path('networks/', NetWorksListCreateView.as_view(), name='networks-list-create'),
    path('networks/<int:pk>/', NetWorksRetrieveUpdateDestroyView.as_view(), name='networks-retrieve-update-destroy'),

    path('payment_methods_list/', PaymentMethodsListView.as_view(), name='payment_methods-list'),
    path('payment_methods_create/', PaymentMethodsCreateView.as_view(), name='payment_methods-create'),
    path('payment_methods/<int:pk>/', PaymentMethodsRetrieveUpdateDestroyView.as_view(),
         name='payment_methods-retrieve-update-destroy'),

    path('clients_list/', ClientsListView.as_view(), name='clients_list'),
    path('clients_create/', ClientsCreateView.as_view(), name='clients_create'),
    path('clients_update/<int:pk>/', ClientsUpdateView.as_view(), name='clients_update'),

    path('persentage_history/', PercentageHistoryListCreateView.as_view(), name='persentage_history-list-create'),
    path('persentage_history/<int:pk>/', PercentageHistoryDeleteView.as_view(), name='persentage_history-delete'),
]
