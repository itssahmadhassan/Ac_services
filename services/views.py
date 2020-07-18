from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from _datetime import datetime
from . import models
from twilio.rest import Client
import json


def index(request):
    return render(request, "index.html")


@csrf_exempt
def submitted(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mail = request.POST.get('email')
    location = request.POST.get('map')
    address = request.POST.get('address')
    message = request.POST.get('message')
    data_added_date = datetime.now()
    text = {'name': name, 'phone': phone, 'mail': mail,
            'location': location, 'address': address,
            'message': message}

    # /////     to convert dictionary to string /////

    result = json.dumps(text)

    notification = "New Order for AC services  is here ........" + result

    if name:
        models.Order.objects.create(name=name, phone=phone, mail=mail, message=message, created=data_added_date,
                                    address=address, )

        # /////   to send message to wats_app using twilio.com  /////
        try:
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=notification,
                to='whatsapp:+923474523358'
            )
        except:
            pass

        # ////////     to send text message ///////
        try:
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            sms = client.messages.create(
                from_='+12057368797',
                body=notification,
                to='+923114006992'
            )
        except:
            pass

    return render(request, "submitted.html")
