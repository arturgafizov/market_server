from django.urls import path

from . import views

app_name = 'apps.wildberries'


urlpatterns = [
    path('orders/', views.GetOrderListView.as_view(), name='my_orders_list'),
    path('sales/', views.GetSaleListView.as_view(), name='my_sales_list'),
    path('stocks/', views.GetStockListView.as_view(), name='my_stocks_list'),
    path('report-detail/', views.GetReportDetailByPeriodView.as_view(),
         name='my_report_detail_by_period'),
]
