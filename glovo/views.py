from django.http import HttpResponse
from django.shortcuts import render
from .models import Order


def order_view(request):
    return HttpResponse(f'Название:{Order.name} - Цена:{Order.price} - Кол-во:{Order.quantity}')
