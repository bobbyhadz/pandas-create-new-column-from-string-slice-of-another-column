# Pandas: Make new Column from string Slice of another Column

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'age': [29, 30, 31, 32],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

print(df)

df['initials'] = df['name'].str[:1]

print('-' * 50)

print(df)