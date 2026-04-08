import requests
from bs4 import BeautifulSoup

def search_bim(country):
    query = f"BIM regulation {country} ISO 19650 standard government"
    url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        for a in soup.select("li.b_algo h2 a"):
            title = a.get_text()
            link = a["href"]

            results.append({
                "title": title,
                "url": link
            })

        print(f"🌐 {country}: {len(results)} resultados encontrados")

        return results

    except Exception as e:
        print(f"Error buscando {country}: {e}")
        return []
