from flask import Flask
import json
import requests
import datetime
import hashlib
  
current_time = datetime.datetime.now()
  
time_stamp = str(current_time.timestamp())
apipublic = '41bd6949f5020938a6dd09c89fb65412'
apipriv = '3d30327222f05d08a11a34be04a29ba91ec9ba7c'

app = Flask(__name__)


@app.route('/')
def hello():
    host = 'http://developer.marvel.com/v1/public/characters'
    hash_generado = generar_hash_md5(time_stamp, apipublic, apipriv)
    
    body = {
        "apikey": apipublic,
        "ts": time_stamp,
        "hash": hash_generado
    }
    r = requests.get(host,body)
    r = r.json()
    print(r)
    return 'Hello, World!'

def generar_hash_md5(ts, apikeypublic, apikeyprivate):
    # Concatenar las variables en una cadena
    cadena_a_hashear = ts + apikeyprivate + apikeypublic

    # Crear un objeto hash MD5
    hash_md5 = hashlib.md5()

    # Actualizar el hash con la cadena codificada en bytes
    hash_md5.update(cadena_a_hashear.encode('utf-8'))

    # Obtener el hash en formato hexadecimal
    hash_resultado = hash_md5.hexdigest()
    return hash_resultado