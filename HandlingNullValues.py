import pandas as pd
import numpy as np

file = pd.read_csv("Penguins Data.csv")

print(file)

print(file.isnull().any())

print(file.isnull().sum())

print(file.fillna(1.0).isnull().any())

print(file.dropna().isnull().any())
