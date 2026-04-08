from openpyxl import Workbook
import os

FILE_PATH = "data/bim_normativas.xlsx"

def update_data(data):
    print("Creando Excel desde cero...")

    os.makedirs("data", exist_ok=True)

    wb = Workbook()
    ws = wb.active

    # Cabeceras
    headers = [
        "nombre", "pais", "region",
        "fecha_publicacion", "entrada_vigor",
        "version", "estado", "fuente"
    ]

    ws.append(headers)

    # Datos
    for row in data:
        ws.append([
            row.get("nombre"),
            row.get("pais"),
            row.get("region"),
            row.get("fecha_publicacion"),
            row.get("entrada_vigor"),
            row.get("version"),
            row.get("estado"),
            row.get("fuente")
        ])

    wb.save(FILE_PATH)

    print("✅ Excel creado correctamente")
