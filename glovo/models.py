from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    couriers = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return self.name
