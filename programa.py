from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2  # O mysql.connector para MySQL

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "54.165.241.112"}})

# Conexión a la base de datos (reemplaza con tus credenciales y la IP de la base de datos en otra instancia)
conn = psycopg2.connect(
    database="users", user='parcial', password='123', host='54.242.52.73', port='5432'
)

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        nombres = data['nombres']
        apellidos = data['apellidos']
        fecha_nacimiento = data['fecha_nacimiento']
        password = data['password']
        
        # Insertar en la base de datos
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (nombres, apellidos, fecha_nacimiento, password) VALUES (%s, %s, %s, %s)", 
                       (nombres, apellidos, fecha_nacimiento, password))
        conn.commit()
        cursor.close()
        
        return jsonify({"message": "Usuario registrado exitosamente"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT nombres, apellidos FROM users")
        users = cursor.fetchall()
        cursor.close()
        
        return jsonify(users)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
