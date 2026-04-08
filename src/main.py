import json
from scraper import fetch_links
from validator import is_official, is_bim_relevant
from parser import parse_document
from updater import update_data

def run():
    print("🚀 INICIO DEL MONITOR BIM")

    # Cargar configuración
    with open("config/countries.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    results = []

    # Recorrer países
    for country, data in config.items():
        print(f"\n🌍 Procesando país: {country}")

        regions = data.get("regions", [])
        sources = data.get("sources", [])

        for region in regions:
            print(f"  📍 Región: {region}")

            for source in sources:
                print(f"    🔎 Fuente: {source}")

                links = fetch_links(source)

                for link in links:
                    title = link.get("title", "")
                    url = link.get("url", "")

                    # Validación
                    if not is_official(url):
                        continue

                    if not is_bim_relevant(title):
                        continue

                    # Parseo
                    parsed = parse_document(link, country, region)
                    results.append(parsed)

    print(f"\n📊 TOTAL DOCUMENTOS DETECTADOS: {len(results)}")

    # Guardar resultados
    update_data(results)

    print("✅ FIN DEL MONITOR BIM")


if __name__ == "__main__":
    run()
