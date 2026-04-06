import sqlite3
def setup():
    conn = sqlite3.connect('data/propaganda_map.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS sites (id INTEGER PRIMARY KEY, domain TEXT UNIQUE, trust_score INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS entities (id INTEGER PRIMARY KEY, value TEXT UNIQUE, type TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS relations (site_id INTEGER, entity_id INTEGER)')
    conn.commit()
    conn.close()
    print("✅ Базата данни е инициализирана в data/")
if __name__ == "__main__":
    setup()
