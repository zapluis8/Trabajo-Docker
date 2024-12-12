from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacenar los puzzles en una lista en memoria
puzzles = []

# Endpoints CRUD (Crear, Leer, Actualizar, Eliminar)

# Crear un nuevo puzzle
@app.route('/puzzles', methods=['POST'])
def create_puzzle():
    # Obtener los datos del cuerpo de la solicitud
    data = request.json
    # Crear un nuevo puzzle con un ID único
    new_puzzle = {
        'id': len(puzzles) + 1,
        'nombre': data['nombre'],  # Nombre del puzzle
        'dificultad': data['dificultad'],  # Dificultad del puzzle
        'descripcion': data.get('descripcion')  # Descripción opcional del puzzle
    }
    # Agregar el nuevo puzzle a la lista
    puzzles.append(new_puzzle)
    # Devolver el puzzle creado con un código de estado 201 (Creado)
    return jsonify(new_puzzle), 201

# Obtener todos los puzzles
@app.route('/puzzles', methods=['GET'])
def get_puzzles():
    # Devolver la lista completa de puzzles
    return jsonify(puzzles)

# Obtener un puzzle por su ID
@app.route('/puzzles/<int:id>', methods=['GET'])
def get_puzzle(id):
    # Buscar el puzzle por su ID en la lista
    puzzle = next((p for p in puzzles if p['id'] == id), None)
    # Si no se encuentra, devolver un error 404 (No encontrado)
    if puzzle is None:
        return jsonify({'error': 'Puzzle no encontrado'}), 404
    # Devolver el puzzle encontrado
    return jsonify(puzzle)

# Actualizar un puzzle
@app.route('/puzzles/<int:id>', methods=['PUT'])
def update_puzzle(id):
    # Obtener los datos del cuerpo de la solicitud
    data = request.json
    # Buscar el puzzle por su ID en la lista
    puzzle = next((p for p in puzzles if p['id'] == id), None)
    # Si no se encuentra, devolver un error 404 (No encontrado)
    if puzzle is None:
        return jsonify({'error': 'Puzzle no encontrado'}), 404
    # Actualizar los campos del puzzle
    puzzle['nombre'] = data['nombre']
    puzzle['dificultad'] = data['dificultad']
    puzzle['descripcion'] = data.get('descripcion', puzzle['descripcion'])
    # Devolver el puzzle actualizado
    return jsonify(puzzle)

# Eliminar un puzzle
@app.route('/puzzles/<int:id>', methods=['DELETE'])
def delete_puzzle(id):
    global puzzles
    # Filtrar la lista para eliminar el puzzle con el ID especificado
    puzzles = [p for p in puzzles if p['id'] != id]
    # Devolver una respuesta vacía con un código de estado 204 (Sin contenido)
    return '', 204

if __name__ == '__main__':
    # Ejecutar la aplicación en el host 0.0.0.0 y el puerto 5000
    app.run(host='0.0.0.0', port=5000)
