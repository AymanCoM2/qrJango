# A6u8u
from django.shortcuts import render, redirect
import qrcode
from PIL import Image
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
script_directory = os.path.join(BASE_DIR, 'qrProject/static')
image_path = os.path.join(script_directory, "code.png")


def getTheQr(request):
    if request.method == 'GET':
        sample_data = request.GET.get('data')
        context = {
            'sample_data': sample_data,
        }
        data = sample_data
        size_and_resolution_list = [
            (90, 90, 72),  # Size: 100x100 pixels, Resolution: 72 DPI
            # (100, 100, 72),  # Size: 100x100 pixels, Resolution: 72 DPI
            # (200, 200, 300),  # Size: 200x200 pixels, Resolution: 300 DPI
            # (300, 300, 600),  # Size: 300x300 pixels, Resolution: 600 DPI
        ]

        # Generate QR code images with different sizes and resolutions
        for size, resolution, dpi in size_and_resolution_list:
            qr = qrcode.QRCode(
                version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img = img.resize((size, size), Image.ANTIALIAS)
            img.save(image_path, dpi=(dpi, dpi))
            return render(request, 'home.html', context)