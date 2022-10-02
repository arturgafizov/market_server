from rest_framework import serializers


class WBReportPeriodQueryParamsSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()


class WBOrderListSerializer(serializers.Serializer):
    date_from = serializers.DateField()


class WBSaleListSerializer(serializers.Serializer):
    date_from = serializers.DateField()


class WBStockListSerializer(serializers.Serializer):
    date_from = serializers.DateField()
