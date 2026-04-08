from updater import update_data

def run():
    test_data = [
        {
            "nombre": "Normativa BIM Test",
            "pais": "España",
            "region": "Madrid",
            "fecha_publicacion": "2024-01-01",
            "entrada_vigor": "2024-02-01",
            "version": "1.0",
            "estado": "vigente",
            "fuente": "https://example.com"
        }
    ]

    print("Enviando datos de prueba...")
    update_data(test_data)

if __name__ == "__main__":
    run()
