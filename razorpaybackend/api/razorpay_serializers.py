from rest_framework import serializers
from ..models import  Transacation

class CreateOrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()
    


class TransactionModelSerilaiser(serializers.Serializer):
    
    class meta:
        model = Transacation
        fields = ["payment_id", "order_id", "signature", "amount"]