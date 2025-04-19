import os
import pandas as pd  # ✅ Add this line!

# Get the path relative to this script
csv_path = os.path.join(os.path.dirname(__file__), 'employee_attrition.csv')

df = pd.read_csv(csv_path)
print(df.head())