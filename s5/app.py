from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    # _integrantes = ['Crecencio Garcia', 'Johan la antigua', 'Magdelin Encarnacion', 'Robinson Reyes', 'Samuel Dleon']
    
    q = '''
        SELECT (e.nombre || ' ' || e.apellido) as nombre_completo 
        FROM estudiantes as e; 
    '''

    with sqlite3.connect('data/asistencia_db.sqlite3') as conn:
        cur = conn.cursor()

    cur.execute(q)
    _integrantes = list(cur)
    _integrantes = [item[0] for item in _integrantes]
    
    return render_template('info.html', integrantes = _integrantes)

@app.route('/lista/<nombre>')
def lista(nombre):
    return nombre.title()

if __name__ == '__main__':
    app.run(debug=True, port=8000)