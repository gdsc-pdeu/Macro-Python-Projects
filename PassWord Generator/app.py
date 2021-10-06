import random
import qrcode

inp = int(input("Enter the length of password : "))
string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
gen_pass =  "".join(random.sample(string, inp))

print("Random generated password : ", gen_pass)

image = qrcode.make(gen_pass)
image.save("PASSWORD.jpg")
