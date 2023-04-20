from django.http import HttpResponse
from django.views import generic

from .models import Courier


class Index(generic.ListView):
    model = Courier
