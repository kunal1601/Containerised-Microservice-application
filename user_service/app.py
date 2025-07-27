from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="postgres",
        database="users",
        user="postgres",
        password="postgres"
    )

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "User registered successfully"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

