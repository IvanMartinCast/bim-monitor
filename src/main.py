raise Exception("ESTO ES UNA PRUEBA")
from updater import update_data

def run():
    test_data = [
        {
            "nombre": "TEST BIM",
            "pais": "España",
            "region": "Madrid",
            "fecha_publicacion": "2024",
            "entrada_vigor": "2024",
            "version": "1.0",
            "estado": "vigente",
            "fuente": "https://test.com"
        }
    ]

    update_data(test_data)

if __name__ == "__main__":
    run()
