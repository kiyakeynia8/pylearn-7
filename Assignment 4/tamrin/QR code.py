import qrcode

name = input("input your name: ")
number = input("your number: ")

QR = name + number

img = qrcode.make(QR)
img.save("my_number.png")