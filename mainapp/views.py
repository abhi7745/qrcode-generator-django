from email import generator
from email.mime import image
import imp
from turtle import pd
from django.shortcuts import render,redirect

# Create your views here.

import qrcode #for generating qr-codes
import os

from PIL import Image #in this case - converting png to pdf

# index page
def index(request):
    if request.method=='POST':
        Mytext=request.POST.get('qr-text')
        # print(Mytext)
        
        # Qr_code generator
        img=qrcode.make(Mytext)
        img.save("static/MyQrcode.png")
        
        # pdf generator
        path = 'static/MyQrcode.png'
        pdf = Image.open(path) # PIL will read the png file
        pdf.save("static/MyQrcode.pdf") #PIL will generate a pdf
        print('pdf done')

        return redirect(download)

    return render(request,'index.html',{})

# download Image
def download(request):
    # img=qrcode.make("Hai Abhijith KR")
    # img.save("myimage.png")
    # img_url=os.listdir('static/')
    # print(img_url)
    # for x in img_url:
    #     print(x)
    return render(request,'download.html',{})