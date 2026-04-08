import pandas as pd
import os

FILE_PATH = "data/bim_normativas.xlsx"

def update_data(new_data):
    print("📊 DATOS RECIBIDOS:", new_data)

    # Asegurar carpeta
    os.makedirs("data", exist_ok=True)

    # Crear DataFrame
    df = pd.DataFrame(new_data)

    print("📊 DataFrame:")
    print(df)

    # 🔥 BORRAR archivo anterior si existe
    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)
        print("🗑️ Excel anterior eliminado")

    # 🔥 CREAR nuevo Excel
    df.to_excel(FILE_PATH, index=False)

    print("✅ Nuevo Excel creado")
