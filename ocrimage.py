import pytesseract
import requests
from PIL import ImageFilter
from PIL import Image
from io import BytesIO
#from pyzbar.pyzbar import decode
import json
import logging
import sys
import cv2
import numpy
from pyzbar.pyzbar import decode

logger = logging.getLogger('scope.name')

def procesar_imagen(url):
	imagen = _get_image(url)
	imagen.filter(ImageFilter.SHARPEN)
	texto= tesseract_proc(imagen)
	#resultado=texto.encode('utf-8')
	#json_str = json.dumps(texto).encode('utf8')
	sys.stdout.write(texto)
	return texto

def  _get_image(url):
	return Image.open(BytesIO(requests.get(url).content))

def tesseract_proc(imagen):
	return pytesseract.image_to_string(imagen,lang='spa')

def cortar_imagen(url):
	imagen = _get_image(url)
	imagen.filter(ImageFilter.SHARPEN)
	opencvImage = cv2.cvtColor(numpy.array(imagen), cv2.COLOR_RGB2BGR)	
	crop_img = opencvImage[100:140, 400:500]
	texto= tesseract_proc(crop_img)
	#resultado=texto.encode('utf-8')
	sys.stdout.write(str(texto))
	return texto

def leerqr(url):
	imagen = _get_image(url)
	imagen.filter(ImageFilter.SHARPEN)
	#opencvImage = cv2.cvtColor(numpy.array(imagen), cv2.COLOR_RGB2BGR)	
	data = str(decode(imagen))
	return data