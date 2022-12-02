#! /usr/bin/env python3
"""
Creates a QR code for each URL in a file - urls.txt

Requires the pillow library, install like this:
pip install pillow
"""

import qrcode

with open('urls.txt') as urlFile:
  lines = urlFile.readlines()

for url in lines:

  img = qrcode.make(url)
  filename=url.split('//')[1]  #Strip the 'https://'' to make the filename
  img.save(f'{filename}.png')

