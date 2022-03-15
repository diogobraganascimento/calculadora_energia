from flask import Flask, render_template, request, redirect, url_for
from calculadora import app
from datetime import datetime


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        medicao_atual = int(request.form['medicao_atual'])
        medicao_anterior = int(request.form['medicao_anterior'])
        return redirect(url_for('resultado', medicao_atual=medicao_atual, medicao_anterior=medicao_anterior))
    else:
        print("NOK")
    return render_template('calculadora.html')


@app.route('/resultado')
def resultado():
    medicao_atual = int(request.args.get('medicao_atual'))
    medicao_anterior = int(request.args.get('medicao_anterior'))
    valor_energia = 1.27447
    data = datetime.today().strftime('%d/%m/%Y')
    if medicao_atual > medicao_anterior:
        resultado = round((medicao_atual - medicao_anterior) * valor_energia, 2)

        return render_template('resultado.html',
                               resultado=resultado,
                               medicao_atual=medicao_atual,
                               medicao_anterior=medicao_anterior,
                               valor_energia=str(valor_energia).replace('.', ','),
                               data=data,
                               )
    else:
        return render_template('resultado.html', resultado="NOK")
