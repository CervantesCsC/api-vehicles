from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo
tasks = [
    {'id': 1, 'title': 'Tarea 1', 'done': False},
    {'id': 2, 'title': 'Tarea 2', 'done': True},
]

@app.route('/')
def hello_world():
    return 'HOLA MUNDO'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'data': tasks})

if __name__ == "__main__":
    app.run(debug=True)