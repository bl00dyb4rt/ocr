import os
from flask import Flask, jsonify, request
from ocrimage import procesar_imagen, cortar_imagen, leerqr

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def index():
    if (request.method == 'POST'):
#    try:
   		url = request.json['image_url']
   		output = procesar_imagen(url)
   		return jsonify({"text":output})

#    except:
#    	return jsonify(
#    		{ "error":"Did you mean to send:{'image_url': 'image_url'}"})
 
@app.route('/ocr/<string:image_url>', methods=['GET'])
def index2():
	if (request.method == 'GET'):
		url = request.json['image_url']
		output = procesar_imagen(url)
		return jsonify({"text":output})


@app.route('/imagencortada', methods=['POST'])
def index3():
    if (request.method == 'POST'):
#    try:
   		url = request.json['image_url']
   		#ancho = request.json['ancho']
   		#largo = request.json['largo']
   		output = cortar_imagen(url)
   		return jsonify({"text":output})


@app.route('/qrlector', methods=['POST'])
def index4():
    if (request.method == 'POST'):
#    try:
   		url = request.json['image_url']
   		#ancho = request.json['ancho']
   		#largo = request.json['largo']
   		output = leerqr(url)
   		return jsonify({"text":output})


 
@app.errorhandler(500)
def internal_error(error):
	print(str(error))

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 4000))
	app.run(debug=True, host='0.0.0.0', port=port)