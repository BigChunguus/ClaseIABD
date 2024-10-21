import pandas as pd

ruta_csv = '..\\..\\..\\..\\David2\\2019-Nov.csv'

df = pd.read_csv(ruta_csv)

ruta_parquet = '..\\..\\..\\..\\David2\\2019-Nov.parquet'

df.to_parquet(ruta_parquet, index=False)