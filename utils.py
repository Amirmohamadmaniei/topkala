import random

import ghasedakpack

from account.models import OTP

sms = ghasedakpack.Ghasedak("8a8ca392db0e62f24957d25e918dd380b29668b435a5b014a9de905535aa0a90")


s = sms.verification(
    {'receptor': '09336564176', 'type': '1', 'template': 'topkala', 'param1': 'سلام'})


print(s)


def create_send_otp(phone):
    code = random.randint(1000, 9999)
    OTP.objects.create(code=code, phone=phone)
    print(code)