import pandas as pd
import os

FILE_PATH = "data/bim_normativas.xlsx"

def update_data(new_data):
    print("📊 DATOS RECIBIDOS:", new_data)

    df_new = pd.DataFrame(new_data)

    print("📊 DataFrame nuevo:")
    print(df_new)

    # Crear carpeta si no existe
    os.makedirs("data", exist_ok=True)

    # Guardar SIEMPRE (sobrescribe para test)
    df_new.to_excel(FILE_PATH, index=False)

    print(f"✅ Excel guardado en {FILE_PATH}")
