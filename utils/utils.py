import random


def otp_generator(size):
    otp = ""
    for x in range(size):
        otp += f"{random.randint(0, 9)}"
    return otp
