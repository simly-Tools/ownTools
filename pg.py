import random
def passgen():
    print("                                         ")
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    symbols="!@#$%^&*"
    all_chars=lower+upper+numbers+symbols
    length=int(input("Enter a length:"))
    password="".join(random.sample(all_chars,length))
    print("Generated Password:",password)