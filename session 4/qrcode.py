
import qrcode

information = []

name = input("enter your name :")
information.append(name)

phone = input("enter your phone number :")
information.append(phone)

image = qrcode.make(information)
image.save("information_qrcode.png")




