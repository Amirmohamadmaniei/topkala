import random
from account.models import OTP
from account import melipayamak

# def create_send_otp(phone):
#     OTP.objects.filter(phone=phone).delete()
#     code = random.randint(1000, 9999)
#     OTP.objects.create(code=code, phone=phone)
#     print(code)


def create_send_otp(phone):
    OTP.objects.filter(phone=phone).delete()
    code = random.randint(1000, 9999)
    OTP.objects.create(code=code, phone=phone)

    username = '09018496657'
    password = 'RPN9G'
    api = melipayamak.Api(username, password)
    sms = api.sms('soap')
    to = phone
    _from = '50004001496657'
    text = f' تاپ کالا \n کد تایید : {code}'
    response = sms.send(to, _from, text)
