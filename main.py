import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('house_data.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Get an overview of the DataFrame, including column names, data types, and non-null values
print(df.info())

# Calculate summary statistics of numeric columns
print(df.describe())

# Plot a histogram of house prices
plt.hist(df['price'], bins=20)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Distribution of House Prices')
plt.show()

# Create a scatter plot of the number of bedrooms versus house prices
plt.scatter(df['bedrooms'], df['price'])
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price')
plt.title('Number of Bedrooms vs. House Prices')
plt.show()

# Calculate the correlation matrix of numeric variables
correlation_matrix = df.corr()
print(correlation_matrix)

# Check for missing values in the dataset
print(df.isnull().sum())

# Remove rows with missing values
df = df.dropna()

# Identify and handle outliers (e.g., using z-scores or IQR method)

