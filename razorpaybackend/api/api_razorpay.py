from rest_framework.views import APIView
from rest_framework import status
from .razorpay_serializers import CreateOrderSerializer, TransactionModelSerilaiser
from rest_framework.response import Response 


from razorpaybackend.api.razorpay.main import RazorpayClient


rz_client = RazorpayClient()


class CreateOrderAPIView(APIView):
    def post(self, request):
        create_order_serializer = CreateOrderSerializer(
            data = request.data
        )
        if create_order_serializer.is_valid():
            order_response = rz_client.create_order(
                amount= create_order_serializer.validated_data.get("amount"),
                currency=create_order_serializer.validated_data.get("currency")
            )
            reponse = {
                "status_code": status.HTTP_201_CREATED,
                "message": "successfully order created",
                "data":order_response
            }
            return Response(reponse, status=status.HTTP_201_CREATED)
        else:
            reponse = {
                "status_code" : status.HTTP_400_BAD_REQUEST,
                "message":"bad request",
                "error" : create_order_serializer.errors
            }
            return Response(reponse, status=status.HTTP_400_BAD_REQUEST)
        
        
class TransactionAPIView(APIView):
    def post(self, request):
        transaction_serializer = TransactionModelSerilaiser(
            data = request.data
        )
        if transaction_serializer.is_valid():
            rz_client.verify_payment(
                razorpay_order_id=transaction_serializer.validated_data.get("order_id"),
                razorpay_payment_id=transaction_serializer.validated_data.get("payment_id"),
                razorpay_signature=transaction_serializer.validated_data.get("signature")

            )
            transaction_serializer.save()
            response = {
                "status_code":status.HTTP_201_CREATED,
                "message": "Transaction created"
            }
            return Response(response, status=status.HTTP_201_CREATED)

        else:
            response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": "Bad Request",
                "error": transaction_serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)