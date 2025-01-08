from django.urls import path
from .api.api_razorpay import CreateOrderAPIView


urlpatterns = [
    path("order/create/", CreateOrderAPIView.as_view(), name="create_order_api")
]
