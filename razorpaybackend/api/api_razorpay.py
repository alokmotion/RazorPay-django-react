from rest_framework.views import APIView
from rest_framework import status
from .razorpay_serializers import CreateOrderSerializer
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