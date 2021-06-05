from flask import Flask, 

app = Flask(__name__)

@app.route('/')
# Decorador que modifica el metodo que viene despues
def funcion_inicio():
    app.logger.debug('Mensaje desde debug')
    app.logger.info('Mensaje desde debug')
    app.logger.warning('Mensaje desde warning')
    app.logger.error('Mensaje desde error')
    return f'Hola Mundo desde Flask'