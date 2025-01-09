from django.urls import path
from .api.api_razorpay import CreateOrderAPIView, TransactionAPIView


urlpatterns = [
    path("order/create/", CreateOrderAPIView.as_view(), name="create_order_api"),
    path("order/complete/", TransactionAPIView.as_view(), name="complete_order_api"),

    
]
