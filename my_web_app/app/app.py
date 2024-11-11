from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration
DB_HOST = 'my_web_app_db_1'  # This is the service name in docker-compose
DB_USER = 'root'
DB_PASSWORD = 'password'
DB_NAME = 'mydb'

def get_db_connection():
    """Establish and return a MySQL database connection."""
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return connection

@app.route('/')
def home():
    """Fetch all entries from the database and render them in the index page."""
    # Establish the connection
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    # Fetch all entries from the database
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()

    # Close the connection
    cursor.close()
    connection.close()

    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

