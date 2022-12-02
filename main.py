#! /usr/bin/env python3
"""
Creates a QR code for each URL in a file - urls.txt

Requires the pillow library, install like this:
pip install pillow
"""

import qrcode

with open('urls.txt') as urlFile:
  content = urlFile.read()

urls=content.split('\n')

for url in urls:

  img = qrcode.make(url)
  filename=url.split('//')[1]
  img.save(f'{filename}.png')

