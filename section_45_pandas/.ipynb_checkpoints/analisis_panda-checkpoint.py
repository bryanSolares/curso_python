import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./Referencia/players_20.csv')

first_ten = data.head(10)
last_ten = data.tail(10)
print(first_ten)
print(last_ten)