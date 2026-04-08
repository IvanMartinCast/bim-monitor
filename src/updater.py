import pandas as pd
import os
import time

FILE_PATH = "data/bim_normativas.xlsx"

def update_data(new_data):
    print("📊 DATOS RECIBIDOS:", new_data)

    df = pd.DataFrame(new_data)

    # 🔥 Truco: añadir timestamp para forzar cambio
    df["timestamp"] = time.time()

    os.makedirs("data", exist_ok=True)

    df.to_excel(FILE_PATH, index=False)

    print("✅ Excel actualizado con timestamp")
