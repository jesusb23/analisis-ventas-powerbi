import pandas as pd

# Cargar el dataset
df = pd.read_csv(
    r"C:\Users\jesus\Documents\proyecto de dattos\data\Sample - Superstore.csv",
    encoding="latin1"
)

# Mostrar primeras filas
print(df.head())

# Revisar información general
print(df.info())

# Revisar valores nulos
print(df.isnull().sum())

# Revisar duplicados
print(df.duplicated().sum())

# Eliminar duplicados
df = df.drop_duplicates()

# Convertir fechas
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Mostrar tipos de datos actualizados
print(df.dtypes)

# Guardar dataset limpio
df.to_csv(
    r"C:\Users\jesus\Documents\proyecto de dattos\data\processed_data.csv",
    index=False
)

print("Limpieza completada correctamente")