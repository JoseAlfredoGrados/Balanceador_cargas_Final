from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    temperatura = float(request.form['temperatura'])
    unidad = request.form['unidad']

    if unidad == 'celsius':
        resultado = (temperatura * 9/5) + 32
        unidad_resultado = 'Fahrenheit'
    elif unidad == 'fahrenheit':
        resultado = (temperatura - 32) * 5/9
        unidad_resultado = 'Celsius'
    else:
        resultado = None
        unidad_resultado = None

    return render_template('resultado.html', temperatura=temperatura, unidad=unidad, resultado=resultado, unidad_resultado=unidad_resultado)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

