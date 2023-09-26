import qrcode
import image

qr= qrcode.QRCode(
    version =15, #15 means the version of the qrcode high the number bigger the image and complicated picture
    box_size= 10,   # the size of the box where the qr will be displayed
    border= 5, #Its the white part of the image
)

data1= "https://www.google.com/"
#The path of which the qr will be generated
# data2= "I Love You so much, Tuli."
data2= "DANGER!!!  YOUR PHONE HAS BEEN HACKED!"

qr.add_data(data2)
qr.make(fit= True)
img= qr.make_image(fill= "black", back_color="white")
img.save("qr.png")