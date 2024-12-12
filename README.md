# Trabajo Docker

# Para ejecutar el codigo y crear un nuevo puzzle tienes que poner la ruta con un POST
http://127.0.0.1:5000/crear
{
  "Content-Type": "application/json"
}
{
  "nombre": "Sudoku",
  "dificultad": "Medio",
  "descripcion": "Un puzzle de lógica y estrés."
}

# Para ejecutar el codigo y ver todos los puzzles tienes que poner la ruta con un GET.
http://127.0.0.1:5000/puzzles

# Para ejecutar el codigo y ver un puzzles por la ID tienes que poner la ruta con un GET.
http://127.0.0.1:5000/puzzles/1
El 1 es la ID que quieras obtener

# Para ejecutar el codigo y actualizar un puzzle tienes que poner la ruta con un PUT.
http://127.0.0.1:5000/actualizar
{
  "Content-Type": "application/json"
}
{
  "nombre": "Sudoku Avanzado",
  "dificultad": "Dificil",
  "descripcion": "Un puzzle más difícil para mejorar tu mentalidad."
}

# Para eliminiar un puzzle tienes que poner la ruta con un DELETE.
http://127.0.0.1:5000/eliminar

