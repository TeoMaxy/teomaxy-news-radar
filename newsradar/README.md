cat <<EOF > README.md
# 🛡️ TeoMaxy News Radar
### Автоматизирана система за анализ на медийни манипулации в България.

Този проект е **OSINT инструмент**, който следи връзките между официални източници и жълти медии.

## 🚀 Функции:
- **Entity Mapping:** Свързва сайтове чрез Whois, имейли и автори.
- **AI Analysis:** Използва Llama 3.1 за откриване на логически противоречия.
- **Auto-Publish:** Резултатите се качват автоматично тук: [https://teomaxy.github.io/teomaxy-news-radar/](https://teomaxy.github.io/teomaxy-news-radar/)

## 🏗️ Структура:
- \`/scripts\`: Логиката на скрапера и анализатора.
- \`/data\`: SQLite база данни с "черния списък".
- \`index.html\`: Фронтендът на твоя радар.

---
© 2026 TeoMaxy | Built on Pop!_OS
EOF
