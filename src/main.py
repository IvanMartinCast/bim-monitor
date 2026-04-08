import os
from updater import update_data

def run():
    print("🚀 INICIO DEL SCRIPT")

    # Ver contenido de carpeta data antes
    if os.path.exists("data"):
        print("📂 Archivos en data (ANTES):", os.listdir("data"))
    else:
        print("📂 Carpeta data no existe")

    # Datos de prueba (forzados)
    test_data = [
        {
            "nombre": "TEST BIM",
            "pais": "España",
            "region": "Madrid",
            "fecha_publicacion": "2024-01-01",
            "entrada_vigor": "2024-02-01",
            "version": "1.0",
            "estado": "vigente",
            "fuente": "https://test.com"
        }
    ]

    print("📊 Enviando datos al updater...")
    update_data(test_data)

    # Ver contenido de carpeta data después
    if os.path.exists("data"):
        print("📂 Archivos en data (DESPUÉS):", os.listdir("data"))

        # Mostrar tamaño del archivo
        file_path = "data/bim_normativas.xlsx"
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"📄 Excel generado. Tamaño: {size} bytes")
        else:
            print("❌ Excel NO encontrado después de ejecutar updater")
    else:
        print("❌ Carpeta data sigue sin existir")

    print("✅ FIN DEL SCRIPT")


if __name__ == "__main__":
    run()
