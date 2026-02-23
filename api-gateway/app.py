from flask import Flask, jsonify, request
import logging
import psycopg2
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def get_db():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'database-service'),
        database=os.getenv('DB_NAME', 'microservicesdb'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'postgres')
    )

def init_db():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS services (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                status VARCHAR(50),
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cur.execute("INSERT INTO services (name, status) VALUES ('API Gateway', 'running') ON CONFLICT DO NOTHING")
        cur.execute("INSERT INTO services (name, status) VALUES ('Frontend', 'running') ON CONFLICT DO NOTHING")
        cur.execute("INSERT INTO services (name, status) VALUES ('Database', 'running') ON CONFLICT DO NOTHING")
        conn.commit()
        cur.close()
        conn.close()
        app.logger.info("Database initialized successfully")
    except Exception as e:
        app.logger.error(f"Database init error: {e}")

@app.route('/')
def home():
    app.logger.info("API Gateway home called")
    return jsonify({
        'service': 'API Gateway',
        'status': 'running',
        'version': '1.0.0'
    })

@app.route('/api/services', methods=['GET'])
def get_services():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('SELECT * FROM services ORDER BY id')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        services = [{'id': r[0], 'name': r[1], 'status': r[2]} for r in rows]
        app.logger.info(f"Returning {len(services)} services")
        return jsonify({'services': services})
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({'services': [], 'error': str(e)})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'api-gateway'})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
