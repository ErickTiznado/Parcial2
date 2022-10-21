import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from urllib import parse
from http.server import BaseHTTPRequestHandler, HTTPServer

temperaturas = pd.read_csv('Libro.csv', engine="python")
print(temperaturas)
c = temperaturas['C']
f = temperaturas['F']
modelo = tf.keras.Sequential()
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
modelo.compile(optimizer=tf.keras.optimizers.Adam(1), loss="mean_squared_error")
epocas = modelo.fit(f,c, epochs=100, verbose=1)
resp = modelo.predict([500])
print(resp)



class servidor_basico(BaseHTTPRequestHandler):
    def do_GET(self):
        print ("peticion hecha con GET")
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write('Hola Mundo/Python'.encode())

    def do_POST(self):
        print ('POST')
        content_length = int(self.headers['Content-Length'])    
        data= self.rfile.read(content_length)   
        data= data.decode()
        data= parse.unquote(data)
        data= float(data)

        predict = modelo.predict([data])
        print('La prediccion Fue:',predict)
        predict= str(predict[0][0])

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin','*')
        self.end_headers()
        self.wfile.write(predict.encode())

print('Iniciando el servidor... ')
server= HTTPServer(('localhost',3003), servidor_basico)
server.serve_forever()

