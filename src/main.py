import json
from scraper import search_bim
from validator import is_official, is_bim_relevant
from parser import parse_document
from updater import update_data

def run():
    print("🚀 INICIO DEL MONITOR BIM GLOBAL")

    # Cargar países
    with open("config/countries.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    results = []

    # Recorrer países
    for country in config.keys():
        print(f"\n🌍 Buscando en: {country}")

        # 🔎 búsqueda global tipo buscador
        search_results = search_bim(country)

        for item in search_results:
            title = item.get("title", "")
            url = item.get("url", "")

            # Validación de fuente oficial
            if not is_official(url):
                continue

            # Validación de contenido BIM
            if not is_bim_relevant(title):
                continue

            # Parseo
            parsed = parse_document(item, country, "Nacional")
            results.append(parsed)

    print(f"\n📊 TOTAL DOCUMENTOS FILTRADOS: {len(results)}")

    # Guardar resultados en Excel
    update_data(results)

    print("✅ FIN DEL MONITOR BIM GLOBAL")


if __name__ == "__main__":
    run()
