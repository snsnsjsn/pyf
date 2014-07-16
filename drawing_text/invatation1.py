#!/usr/bin/env  python

import os
import Image
import ImageDraw
import ImageFont

img = Image.open("res/invatation1.jpg")
name = os.sys.argv[1]

draw = ImageDraw.Draw(img)
#font = ImageFont.truetype("font/msyh.ttc", 35)
font = ImageFont.truetype("font/xingkai.TTF", 35)

#draw.text((120,300), unicode(name, 'utf-8'), (255,255,255),font=font)
draw.text((700, 764), unicode(name, 'utf-8'), (0,0,0),font=font)

#img.save(name+'01.png')
img.save('./output/'+name+'02.jpg')

