import random
lower="qwertyuıopğüasdfghjklşizxcvbnmöç"
upper=lower.upper()
number="0123456789"
mark="!^+%&/()=*-"
total=lower+upper+number

password=random.choices(total,k=14)

password="".join(password)

print("Güçlü bir şifre arıyorsanız =",password)

