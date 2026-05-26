from sciencelabx import Data
import pandas as pd
import sciencelabx as scx

print(scx.welcome())

df = pd.read_csv(r"tests\datos_limpios.csv", sep=(","))

Data.summary_data(df, metric=["mean", "median", "mode", "count", "quantiles","min", "max", "NaN", "var", "std"], 
                decimals=2, return_metrics=False, return_str=True)