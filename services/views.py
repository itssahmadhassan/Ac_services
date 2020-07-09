from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from _datetime import datetime
from .models import Order
from . import models


def index(request):
    return render(request, "index.html")


@csrf_exempt
def submitted(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mail = request.POST.get('email')
    location = request.POST.get('location')
    address = request.POST.get('address')
    message = request.POST.get('message')
    data_added_date = datetime.today()
    models.Order.objects.create(name=name, phone=phone, mail=mail, message=message, created=data_added_date,
                                address=address, )

    return render(request, "submitted.html")
