from flask import Flask, request, jsonify

app = Flask(__name__)

Opciones = [
    {
        "id": 1,
        "title": "1. Cargar con un archivo CSV."
    },
    {
        "id": 2,
        "title": "2. Insertar de forma manual."
    },
    {
        "id": 3,
        "title": "3. Buscar un registro."
    },
    {
        "id": 4,
        "title": "4. Mostrar la informacion del grupo."
    },
    {
        "id": 5,
        "title": "5. Salir."
    }
]

@app.route('/')
def index():
    return "hello word!"

@app.route('/api/o1/opciones/')
def get_all_opciones():
    return jsonify(Opciones)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)