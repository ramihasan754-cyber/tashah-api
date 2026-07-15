from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host='mysql-2802b869-ramihasan754-ef74.k.aivencloud.com',
        port=25906,
        user='avnadmin',
        password='AVNS_gpkX5Qo75qzxukuZ257',
        database='defaultdb'
    )

@app.route('/api/get-data', methods=['GET'])
def get_data():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        # تأكد أن اسم الجدول هو نفسه الموجود في الداتابيز
        cursor.execute("SELECT * FROM restaurants") 
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
