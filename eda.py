import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('./data/used_bikes.csv')

# Create a new feature: bike_age
df['bike_age'] = 2025 - df['year']

# Plot 1: Price vs Bike Age (Boxplot)
sns.boxplot(x='bike_age', y='price', data=df)
plt.title("Price vs. Bike Age")
plt.xticks(rotation=45)
plt.show()

# Plot 2: Distribution of Prices (Histogram)
sns.histplot(df['price'], kde=True)
plt.title("Used Bike Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()


