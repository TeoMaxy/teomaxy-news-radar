import sqlite3

def setup_db():
    conn = sqlite3.connect('propaganda_map.db')
    cursor = conn.cursor()

    # Таблица за сайтове
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY,
            domain TEXT UNIQUE,
            ip_address TEXT,
            whois_owner TEXT,
            trust_score INTEGER DEFAULT 100
        )
    ''')

    # Таблица за свързани лица/контакти
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entities (
            id INTEGER PRIMARY KEY,
            value TEXT UNIQUE, -- имейл, телефон или име на автор
            type TEXT -- 'email', 'phone', 'author'
        )
    ''')

    # Таблица за връзки (кой субект в кой сайт е намерен)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS relations (
            site_id INTEGER,
            entity_id INTEGER,
            FOREIGN KEY(site_id) REFERENCES sites(id),
            FOREIGN KEY(entity_id) REFERENCES entities(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Базата данни е готова!")

setup_db()
