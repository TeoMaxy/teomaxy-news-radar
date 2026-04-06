import os

def create_structure():
    # Описваме структурата на папките
    folders = [
        'scripts',
        'data',
        '.github/workflows'
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Създадена папка: {folder}")

    # 1. Скрипт за базата данни
    db_script = """import sqlite3
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
"""
    with open('scripts/db_setup.py', 'w', encoding='utf-8') as f:
        f.write(db_script)

    # 2. Основният HTML за GitHub Pages
    index_html = """<!DOCTYPE html>
<html lang="bg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>News Radar - TeoMaxy</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; max-width: 900px; margin: auto; padding: 40px; background: #f0f2f5; color: #333; }
        .container { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h1 { color: #1a73e8; border-bottom: 2px solid #1a73e8; padding-bottom: 10px; }
        .status { background: #e8f0fe; border-left: 5px solid #1a73e8; padding: 15px; margin: 20px 0; }
        .footer { margin-top: 50px; font-size: 0.8em; color: #666; text-align: center; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ Радар за Дезинформация: TeoMaxy</h1>
        <p>Автоматизирана система за анализ на медийни манипулации и координирани мрежи.</p>
        
        <div class="status">
            <strong>Текущо състояние:</strong> Системата е в процес на първоначално сканиране. 
            <br>Очаквайте първия доклад след приключване на анализа на БТА vs Жълти медии.
        </div>

        <h3>🎯 Цели на проекта:</h3>
        <ul>
            <li>Идентифициране на "ферми за новини".</li>
            <li>Разкриване на скрити връзки между сайтове чрез Whois и метаданни.</li>
            <li>AI анализ на емоционалния заряд (Clickbait).</li>
        </ul>
    </div>
    <div class="footer">
        © 2026 TeoMaxy News Radar Project | Powered by Llama 3.1 & Pop!_OS
    </div>
</body>
</html>
"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)

    # 3. README за профила ти
    readme = """# 🛡️ TeoMaxy News Radar
Автоматизиран OSINT инструмент за анализ на българското информационно пространство.

## 🏗️ Структура
- `/scripts`: Python инструменти за скрапинг и анализ.
- `/data`: SQLite база данни (Relational Mapping).
- `index.html`: Динамичен фронтенд за GitHub Pages.

## 🚀 Стартиране
1. `python3 scripts/db_setup.py`
2. `python3 scripts/scout.py` (след като го добавиш)
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme)

    print("\n🚀 Всички локални файлове са подготвени!")
    print("Сега изпълни тези команди в терминала, за да ги качиш:")
    print("git add .")
    print("git commit -m 'Auto-setup of project structure'")
    print("git push origin main")

if __name__ == "__main__":
    create_structure()
