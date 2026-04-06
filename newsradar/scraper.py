import requests
from bs4 import BeautifulSoup
import json
from rapidfuzz import fuzz

def get_simple_text(url):
    try:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        # Вземаме само заглавието и първия параграф за по-леко
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else ""
        p = soup.find('p').get_text(strip=True) if soup.find('p') else ""
        return title, p
    except:
        return "", ""

def main():
    topic = "Зеленски" # Нека пробваме с по-конкретна дума
    print(f"🚀 Търся връзка за: {topic}")
    
    # Източник 1: БТА
    bta_url = "https://www.bta.bg/bg/news/bulgaria"
    res_bta = requests.get(bta_url, headers={'User-Agent': 'Mozilla/5.0'})
    soup_bta = BeautifulSoup(res_bta.text, 'html.parser')
    
    bta_articles = []
    for h in soup_bta.find_all('h3')[:10]:
        txt = h.get_text(strip=True)
        if topic.lower() in txt.lower():
            link = h.find('a')['href'] if h.find('a') else ""
            if link:
                full_link = "https://www.bta.bg" + link if not link.startswith('http') else link
                t, p = get_simple_text(full_link)
                bta_articles.append({"title": t, "content": p})

    # Източник 2: Blitz (директно търсене в техния списък)
    blitz_url = "https://blitz.bg"
    res_blitz = requests.get(blitz_url, headers={'User-Agent': 'Mozilla/5.0'})
    soup_blitz = BeautifulSoup(res_blitz.text, 'html.parser')
    
    matches = []
    for h in soup_blitz.find_all(['h3', 'a'])[:50]:
        blitz_txt = h.get_text(strip=True)
        for bta_art in bta_articles:
            # Математическо сравнение на заглавията
            similarity = fuzz.partial_ratio(bta_art['title'], blitz_txt)
            if similarity > 65: # Ако си приличат над 65%
                print(f"🎯 Намерено подобие ({similarity}%): {blitz_txt[:50]}")
                link = h.get('href') if h.name == 'a' else (h.find('a')['href'] if h.find('a') else "")
                if link:
                    full_link = "https://blitz.bg" + link if not link.startswith('http') else link
                    t, p = get_simple_text(full_link)
                    matches.append({
                        "official": bta_art,
                        "yellow": {"title": t, "content": p},
                        "score": similarity
                    })

    with open('deep_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(matches, f, ensure_ascii=False, indent=4)
    print(f"✅ Готово. Намерени {len(matches)} двойки за сравнение.")

if __name__ == "__main__":
    main()
