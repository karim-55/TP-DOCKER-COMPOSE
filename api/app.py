from flask import Flask, jsonify, request
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Variables d'environnement
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route("/status")
def status():
    return jsonify({"status": "OK"})

@app.route("/items", methods=["GET"])
def get_items():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM items;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/items", methods=["POST"])
def add_item():
    try:
        data = request.json
        name = data.get("name")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO items (name) VALUES (%s) RETURNING id, name;", (name,))
        new_item = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": new_item[0], "name": new_item[1]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM items WHERE id=%s;", (item_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
