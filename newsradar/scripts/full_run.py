import feedparser
import datetime
import os

def run_real_analysis():
    print("📡 Вземам новини от БТА в реално време...")
    
    # 1. Четем истинските новини от БТА
    feed = feedparser.parse("https://www.bta.bg/bg/rss/bulgaria")
    findings = []
    
    for entry in feed.entries[:5]: # Вземаме последните 5
        findings.append({
            "source": "БТА",
            "title": entry.title,
            "type": "official"
        })

    # 2. Добавяме един "ШОК" пример за сравнение (ръчно засега)
    findings.append({
        "source": "Жълт Сайт",
        "title": "ШОК! НЕВЕРОЯТНО РАЗКРИТИЕ ЗА БЮДЖЕТА - ВИЖТЕ ТУК!",
        "type": "clickbait"
    })

    now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    
    # 3. Генерираме HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="bg">
    <head>
        <meta charset="UTF-8">
        <title>News Radar - Live</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; max-width: 800px; margin: auto; padding: 40px; background: #1a1a2e; color: #e1e1e1; }}
            .card {{ background: #16213e; padding: 20px; border-radius: 10px; border-left: 5px solid #0f3460; margin-bottom: 20px; }}
            .fake {{ border-left-color: #e94560; }}
            .official {{ border-left-color: #4db8ff; }}
            .tag {{ font-size: 0.7em; padding: 3px 8px; border-radius: 3px; background: #0f3460; }}
            .tag-fake {{ background: #e94560; }}
        </style>
    </head>
    <body>
        <h1>🛡️ News Radar: На Живо</h1>
        <p>Последно обновяване: {now}</p>
    """

    for item in findings:
        cls = "fake" if item['type'] != 'official' else "official"
        tag_cls = "tag-fake" if item['type'] != 'official' else ""
        html_content += f"""
        <div class="card {cls}">
            <span class="tag {tag_cls}">{item['type']}</span>
            <strong>{item['source']}</strong>
            <p>{item['title']}</p>
        </div>
        """

    html_content += "</body></html>"

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ index.html е обновен с реални новини!")

if __name__ == "__main__":
    run_real_analysis()
