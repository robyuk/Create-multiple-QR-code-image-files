#! /usr/bin/env python3
"""
Creates a QR code in an image file

Requires the pillow library, install like this:
pip install pillow
"""

import qrcode

img = qrcode.make('https://www.raycomputing.com')
img.save('qr.png')

# Test the QR code
import cv2
import webbrowser
image=cv2.imread('qr.png')
detector=cv2.QRCodeDetector()
url, coords, pixels = detector.detectAndDecode(image)

print(pixels, url, coords )
webbrowser.open(url)

'''
""" To use an image captured from the camera, 
copy the code below to a device with python3 and a camera:"""

#! /usr/bin/env python3
"""
Finds a QR code in an image captured from the camera and decodes it

Requires CV2, install like this:
pip install opencv-python
"""

import cv2
import webbrowser

video=cv2.VideoCapture(1)  # the integer may be 0 or 2 depending on your hardware configuration
success,frame = video.read()
detector=cv2.QRCodeDetector()

while success:
    url, coords, pixels = detector.detectAndDecode(frame)
    if url:
        webbrowser.open
        break
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
    success, frame = video.read()

video.release()
cv2.destroyAllWindows()

'''