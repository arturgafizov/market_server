from .serializers import WBSaleListSerializer, WBOrderListSerializer, WBStockListSerializer, \
    WBReportPeriodQueryParamsSerializer

tags_wb = ['WildBerries']


tags_orders_list = {
    'operation_description': '## Апи для получение списка казов',
    'operation_summary': 'Апи для получения списка заказов',
    'tags': tags_wb,
    'query_serializer': WBOrderListSerializer,
}

tags_sales_list = {
    'operation_description': '## Апи для получение списка продаж',
    'operation_summary': 'Апи для получения списка продаж',
    'tags': tags_wb,
    'query_serializer': WBSaleListSerializer,
}

tags_stock_list = {
    'operation_description': '## Апи для получение списка остатков',
    'operation_summary': 'Апи для получения списка остатков',
    'tags': tags_wb,
    'query_serializer': WBStockListSerializer,
}

tags_report_detail_by_period = {
    'operation_description': '## Апи для  списка остатков за отчетный период',
    'operation_summary': 'Апи для получения списка остатков за отчетный период',
    'tags': tags_wb,
    'query_serializer': WBReportPeriodQueryParamsSerializer,
}
