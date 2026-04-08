from datetime import datetime

def parse_document(item, country, region):
    return {
        "nombre": item["title"],
        "pais": country,
        "region": region,
        "fecha_publicacion": datetime.today().strftime("%Y-%m-%d"),
        "entrada_vigor": "",
        "version": "1",
        "estado": "vigente",
        "fuente": item["url"]
    }
