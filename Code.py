import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('violence_data.csv')
data_cleaned = data.dropna(subset=['Value'])
data_cleaned['Value'] = pd.to_numeric(data_cleaned['Value'])
print("Dataset Info:")
data_cleaned.info()
print("Summary Statistics:")
print(data_cleaned.describe())