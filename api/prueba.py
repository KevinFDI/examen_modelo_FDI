from flask import Flask, jsonify

app = Flask(__name__)
books = []
@app.route('/')
def saludo():
    return jsonify({'message':'Hola'})

@app.route('/api/academic-books/books/<ISBN>',methods=['GET'])


    app.run(debug=True, port=6000)


#def libroGet(libro):
#    libros=[]
 #   for l in libros:
  #      if l['ISBN'] == libro:
   #         return jsonify({'libro' : libro[0], 'titule' : libro, 'author' : libro, 'price' : libro})
    #return jsonify({'busqueda' : libro, 'status' : 'not found'})

#request
#url = ...
#response = requests.get(url)
#status_code = response.status_code
#if status_code == 200:
#   json = response.json()
#   print('tipo: ', type(json))
#   print(json
#else:
#   print('Error en la solicitud')

#@app.route('/api/academic-books/books', methods=['GET'])
#def obtener_libros():



