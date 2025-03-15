import streamlit as st
import psycopg2

# Database connection details
DB_HOST = "postgres-db"
DB_PORT = "5432"
DB_NAME = "mydb"
DB_USER = "myuser"
DB_PASS = "mypassword"

# Connect to PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Streamlit UI
st.title("Streamlit & PostgreSQL")

if st.button("Fetch Data"):
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        data = cur.fetchone()
        st.write(f"Database Time: {data}")
        cur.close()
        conn.close()