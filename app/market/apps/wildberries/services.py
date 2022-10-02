from django.conf import settings
from urllib.parse import urljoin
import requests


class WildBerriesService:
    APIKEY_IE = settings.WB_API_KEY_IE
    APIKEY_OOO = settings.WB_API_KEY_OOO
    WB_URL = settings.WB_URL

    def get_orders(self, date_from: str):
        url = urljoin(self.WB_URL, 'api/v1/supplier/orders')
        params = {'key': self.APIKEY_OOO, 'dateFrom': date_from, 'flag': 1}
        print(url, params)
        response = requests.get(url, params=params)
        order_list = response.json()
        return order_list

    def get_sales(self, date_from: str):
        url = urljoin(self.WB_URL, 'api/v1/supplier/sales')
        params = {'key': self.APIKEY_OOO, 'dateFrom': date_from, 'flag': 1}
        response = requests.get(url, params=params)
        sale_list = response.json()
        return sale_list

    def get_stocks(self, date_from: str):
        url = urljoin(self.WB_URL, 'api/v1/supplier/stocks')
        params = {'key': self.APIKEY_OOO, 'dateFrom': date_from}
        response = requests.get(url, params=params)
        stock_list = response.json()
        return stock_list

    def get_report_detail_by_period(self, date_from: str, date_to: str):
        url = urljoin(self.WB_URL, 'api/v1/supplier/reportDetailByPeriod')
        params = {'key': self.APIKEY_OOO, 'dateFrom': date_from, 'dateTo': date_to, 'limit': 50000}
        response = requests.get(url, params=params)
        report_detail_by_period = response.json()
        return report_detail_by_period
