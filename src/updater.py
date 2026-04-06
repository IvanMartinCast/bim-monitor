import pandas as pd
import os

FILE_PATH = "data/bim_normativas.xlsx"

COLUMNS = [
    "nombre", "pais", "region",
    "fecha_publicacion", "entrada_vigor",
    "version", "estado", "fuente"
]

def load_data():
    if os.path.exists(FILE_PATH):
        return pd.read_excel(FILE_PATH)
    return pd.DataFrame(columns=COLUMNS)


def save_data(df):
    df.to_excel(FILE_PATH, index=False)


def update_data(new_rows):
    df = load_data()

    for row in new_rows:
        exists = df["fuente"].str.contains(row["fuente"]).any()

        if not exists:
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

    save_data(df)
