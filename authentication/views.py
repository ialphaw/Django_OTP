from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import Driver
from .models import AuthUser

from utilities.auth_code import random_with_N_digits
from utilities.send_sms import send_sms


@api_view(['POST'])
def auth_driver(request):
    phone = request.data.get('phone')
    isDriver = Driver.objects.filter(phone=phone).exists()

    if isDriver:
        driver = Driver.objects.get(phone=phone)
        if driver.authorized:
            return Response({'Message': 'Your Phone Is Authenticated'})
        auth_code = random_with_N_digits(5)
        send_sms(phone, auth_code)
        AuthUser.objects.create(phone=phone, auth_code=auth_code)
        return Response({'Message': 'Authentication Code Sent To Your Phone'})
    else:
        return Response({'Message': '-1'})


@api_view(['POST'])
def validate_driver(request):
    phone = request.data.get('phone')
    check_auth_code = request.data.get('auth_code')
    main_auth_code = AuthUser.objects.filter(phone=phone)
    driver = Driver.objects.get(phone=phone)

    if main_auth_code.exists():
        if str(main_auth_code.last()) == check_auth_code:
            driver.authorized = True
            driver.save()
            print(driver.authorized)
            print(driver)
            return Response({'Message': 'Phone Activated'})
        else:
            return Response({'Message': 'Auth Code Is Wrong'})
    else:
        return Response({'Message': 'Authorize Your Phone First'})
