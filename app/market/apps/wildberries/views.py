from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator

from .services import WildBerriesService
from . import swagger_schemas as schemas


class MarketPageNumberPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 10
    page_size_query_param = 'page_size'


class GetOrderListView(APIView):
    permission_classes = []

    @swagger_auto_schema(**schemas.tags_orders_list, )
    def get(self, request):
        date_from = request.query_params.get('date_from')
        wb_orders = WildBerriesService().get_orders(date_from)
        return Response(wb_orders)


class GetSaleListView(APIView):
    permission_classes = []

    @swagger_auto_schema(**schemas.tags_sales_list, )
    def get(self, request):
        date_from = request.query_params.get('date_from')
        wb_sales = WildBerriesService().get_sales(date_from)
        return Response(wb_sales)


class GetStockListView(APIView):
    permission_classes = []

    @swagger_auto_schema(**schemas.tags_stock_list, )
    def get(self, request):
        date_from = request.query_params.get('date_from')
        wb_stocks = WildBerriesService().get_stocks(date_from)
        return Response(wb_stocks)


class GetReportDetailByPeriodView(APIView):
    permission_classes = []

    @swagger_auto_schema(**schemas.tags_report_detail_by_period, )
    def get(self, request):
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')
        wb_report_detail = WildBerriesService().get_report_detail_by_period(date_from, date_to)
        return Response(wb_report_detail)
