from django.db import models

# Create your models here.


class Transacation(models.Model):
    payment_id = models.CharField(max_length=100, verbose_name="Payment Id" )
    order_id = models.CharField(max_length=100, verbose_name="Order Id")
    signature = models.CharField(max_length=200, verbose_name="Signature")
    amount = models.IntegerField(verbose_name="Amount")
    datetime = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.id)

