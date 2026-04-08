import os

def run():
    print("Creando archivo de prueba...")

    os.makedirs("data", exist_ok=True)

    with open("data/test.txt", "w") as f:
        f.write("ESTO FUNCIONA")

    print("Archivo creado")

if __name__ == "__main__":
    run()
