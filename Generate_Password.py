import random
password_len=int(input("Enter The Length Of The Passwoard:"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p="".join(random.sample(s,password_len))
print(p)
