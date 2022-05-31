from django.db import models

# Create your models here.
from backend.apps.accounts.models import User
from backend.apps.product.models import Product


class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_CONFIRMED = "confirmed"
    STATUS_SEND = "send"
    STATUS_DELIVERED = "delivered"
    STATUS_REJECTED = "rejected"
    ORDER_STATUSES = (
        (STATUS_NEW,"Новый"),
        (STATUS_CONFIRMED,"Подтвержден"), 
        (STATUS_SEND, "Отправлен"), 
        (STATUS_DELIVERED, "Доставлен"),
        (STATUS_REJECTED, "Отменен"),
    )
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField("Адрес",max_length=255)
    postal_code = models.CharField("Почтовый индекс", max_length=10)
    mobile = models.CharField("Номер телефона", max_length=10)
    notice = models.CharField("Комментарий", max_length=255)
    status = models.CharField(
        "Статус", 
        max_length=9, 
        choices=ORDER_STATUSES,
        default=STATUS_NEW
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created']

    def __str__(self):
        return f"Заказ-{self.id}"



class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name="Товар")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField("Количество", default=1)

    def __str__(self):
        return f"{self.id}"
