import pandas as pd
import os

FILE_PATH = "data/bim_normativas.xlsx"

def update_data(new_data):
    print("DATOS RECIBIDOS:", len(new_data))

    if not new_data:
        print("⚠️ No hay datos para guardar")
        return

    if os.path.exists(FILE_PATH):
        df_existing = pd.read_excel(FILE_PATH)
    else:
        df_existing = pd.DataFrame()

    df_new = pd.DataFrame(new_data)

    df_final = pd.concat([df_existing, df_new], ignore_index=True)

    df_final.to_excel(FILE_PATH, index=False)

    print("✅ Excel actualizado")
