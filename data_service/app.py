from flask import Flask, jsonify
import psycopg2
import redis

app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)

def get_db_connection():
    return psycopg2.connect(
        host="postgres",
        database="users",
        user="postgres",
        password="postgres"
    )

@app.route('/user/<name>')
def get_user(name):
    cached_email = cache.get(name)
    if cached_email:
        return jsonify({"name": name, "email": cached_email.decode('utf-8') + " (from cache)"}), 200

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT email FROM users WHERE name = %s", (name,))
    result = cur.fetchone()
    cur.close()
    conn.close()

    if result:
        email = result[0]
        cache.set(name, email)
        return jsonify({"name": name, "email": email}), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

