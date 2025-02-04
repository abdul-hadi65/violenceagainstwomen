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

# Visualization 1: Bar plot of average 'Value' by Gender
plt.figure(figsize=(10, 6))
sns.barplot(x='Gender', y='Value', data=data_cleaned, ci=None, palette='pastel')
plt.title('Average Survey Value by Gender')
plt.ylabel('Average Value')
plt.xlabel('Gender')
plt.show()

# Visualization 2: Distribution of Values by Gender using Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Value', data=data_cleaned, palette='Set2')
plt.title('Distribution of Values by Gender')
plt.ylabel('Value')
plt.xlabel('Gender')
plt.show()

# Visualization 3: Heatmap of Value by Country and Gender
pivot_table = data_cleaned.pivot_table(index='Country', columns='Gender', values='Value', aggfunc='mean')
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt='.1f', cmap='coolwarm', cbar=True)
plt.title('Average Value by Country and Gender')
plt.ylabel('Country')
plt.xlabel('Gender')
plt.show()

# Visualization 4: Pie chart of gender distribution
gender_counts = data_cleaned['Gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.title('Gender Distribution')
plt.show()