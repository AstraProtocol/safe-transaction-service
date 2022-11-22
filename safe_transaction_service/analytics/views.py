from django.db.models import Count

import django_filters
from rest_framework.generics import ListAPIView

from safe_transaction_service.analytics import serializers
from safe_transaction_service.history import filters
from safe_transaction_service.history.models import MultisigTransaction


class AnalyticsMultisigTxsByOriginListView(ListAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = filters.AnalyticsMultisigTxsByOriginFilter
    pagination_class = None
    queryset = (
        MultisigTransaction.objects.values("origin")
        .annotate(transactions=Count("*"))
        .order_by("-transactions")
    )
    serializer_class = serializers.AnalyticsMultisigTxsByOriginResponseSerializer


class AnalyticsMultisigTxsBySafeListView(ListAPIView):
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = filters.AnalyticsMultisigTxsBySafeFilter
    queryset = (
        MultisigTransaction.objects.safes_with_number_of_transactions_executed_and_master_copy()
    )
    serializer_class = serializers.AnalyticsMultisigTxsBySafeResponseSerializer
