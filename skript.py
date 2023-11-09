import pandas as pd
pd.options.display.max_rows=2
df = pd.read_csv('data.csv')
strr = df.to_string()
print(strr)
print(df.head(1))
print(df.tail(2))
print(df.info())