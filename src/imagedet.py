import string
import sys
from PIL import Image

#arguments: image object
#function: calculate hex string for image
def dhash(image):
	count = 0
	resized_image = image.convert('LA').resize((9,8), Image.ANTIALIAS)
	pixels = list(image.getdata())
	diff= []
	for row in xrange(8):
		for col in xrange(8):
			pixel_l = resized_image.getpixel((col,row))
			pixel_r = resized_image.getpixel((col+1,row))
			diff.append(pixel_l >pixel_r)	
	dec_val = 0
	hexs=[]
	for index,value in enumerate(diff):
		if value:
			dec_val +=2**(index%8)
		if(index%8) == 7:
			hexs.append(hex(dec_val)[2:].rjust(2,'0'))
			dec_val = 0
	return hexs
	

	

