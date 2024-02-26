from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = (SearchFilter,)
    search_fields = ('description', 'title',)



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('products',)

# class ProductViewSet(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     search_fields = ['title', 'description']
#     pagination_class = LimitOffsetPagination
#
# class StockViewSet(ModelViewSet):
#     queryset = Stock.objects.all()
#     serializer_class = StockSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     search_fields = ['products__title', 'products__description']
#     filterset_fields = ['products', ]
#     pagination_class = LimitOffsetPagination
