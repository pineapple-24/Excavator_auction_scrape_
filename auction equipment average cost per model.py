import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = r"place_csv_file_path_here"  # Replace with the path to your CSV file
equipment_data = pd.read_csv(file_path)

# Calculate the average price for each model, ignoring missing values
average_price_per_model = equipment_data.groupby('model')['price'].mean().sort_values(ascending=False)

# Create a bar chart
plt.figure(figsize=(12, 8))
average_price_per_model.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Price per Machine Model', fontsize=16)
plt.xlabel('Machine Model', fontsize=14)
plt.ylabel('Average Price (in USD)', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display the chart
plt.show()
