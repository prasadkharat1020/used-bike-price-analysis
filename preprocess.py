import pandas as pd  # Import pandas

# Load the raw dataset
df = pd.read_csv('../data/used_bikes.csv')

# Handling missing values by dropping rows with missing data in important columns
df = df.dropna(subset=['price', 'brand', 'year', 'engine_capacity'])

# Convert year to bike age
df['bike_age'] = 2025 - df['year']

# Encode categorical variables
df = pd.get_dummies(df, columns=['brand', 'owner_type'], drop_first=True)

# Remove outliers (e.g., very high price or engine capacity)
df = df[df['price'] < 500000]
df = df[df['engine_capacity'] < 1500]

# Save cleaned dataset to outputs folder
df.to_csv('../outputs/use_data.csv', index=False)

