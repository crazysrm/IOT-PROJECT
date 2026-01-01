from flask import Flask, render_template
import mysql.connector
import time

app = Flask(__name__)

# MySQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="env_db"
)
cursor = db.cursor(dictionary=True)

@app.route("/")
def index():
    cursor.execute("SELECT * FROM sensor_data ORDER BY id DESC LIMIT 50")
    rows = cursor.fetchall()
    
    latest = rows[0] if rows else {
        "temperature": "--",
        "humidity": "--",
        "gas": "--",
        "timestamp": "--"
    }
    
    if rows:
        latest['timestamp_display'] = latest['timestamp']
    else:
        latest['timestamp_display'] = '--'

    return render_template("index.html", rows=rows, latest=latest)

if __name__ == "__main__":
    print("🚀 Flask Dashboard LIVE - Auto-refresh every 5s!")
    print("📱 Open: http://127.0.0.1:5000")
    print("💾 subscriber.py must run in another terminal!")
    app.run(debug=True, use_reloader=True, port=5000)  # ✅ AUTO-RELOAD + PORT
