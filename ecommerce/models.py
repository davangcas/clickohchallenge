from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    date_time = models.DateTimeField()

    def __str__(self):
        return str(self.date_time)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Product: {self.product.name} , Date: {self.order.date_time}, Quantity: {self.quantity}"
