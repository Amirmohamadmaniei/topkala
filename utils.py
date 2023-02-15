import random
from account.models import OTP
import requests


def create_send_otp(phone):
    OTP.objects.filter(phone=phone).delete()
    code = random.randint(1000, 9999)
    OTP.objects.create(code=code, phone=phone)

    data = {'from': '', 'to': phone, 'text': f' تاپ کالا \n کد تایید : {code}'}
    requests.post('https://console.melipayamak.com/api/', json=data)
