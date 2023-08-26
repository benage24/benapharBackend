import django_filters

from Caisse.models import DailySales


class DailySalesFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = DailySales
        fields = []
