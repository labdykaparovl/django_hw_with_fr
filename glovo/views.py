from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from .models import Order, Courier


class Index(generic.ListView):
    model = Courier


def order_view(request):
    return HttpResponse(f'Название:{Order.name} - Цена:{Order.price} - Кол-во:{Order.quantity}')

