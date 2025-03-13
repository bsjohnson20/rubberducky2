# Class to manage the database
import sqlite3


class SQL:
    def __init__(self):
        self.conn = sqlite3.connect("hosts.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS hosts (
                uuid TEXT PRIMARY KEY,
                ip TEXT
            )
        """)
        self.conn.commit()

    def check_exists(self, uuid):
        self.cursor.execute("SELECT * FROM hosts WHERE uuid = ?", (uuid,))
        return self.cursor.fetchone()

    def add_host(self, uuid, ip):
        if self.check_exists(uuid):
            return
        
        self.cursor.execute("INSERT INTO hosts (uuid, ip) VALUES (?, ?)", (uuid, ip))
        self.conn.commit()
        
    def get_ip(self, uuid):
        self.cursor.execute("SELECT ip FROM hosts WHERE uuid = ?", (uuid,))
        return self.cursor.fetchone()[0]
    
    def fetch_all(self):
        self.cursor.execute("SELECT * FROM hosts")
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()
        