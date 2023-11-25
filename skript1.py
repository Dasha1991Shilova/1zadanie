import pandas as pd
import matplotlib.pylot as plt

pd.options.display.max_rows=2
df = pd.read_csv('data.csv')
strr = df.to_string()
print(strr)
print(df.head(1))
print(df.tail(2))
print("Информация о данных:")
print(df.info())

numeric_summary=df.describe()
print("Простой анализ числовых данных:")
print(numeric_summary)

df['numeric_column'].hist(bins=20)
plt.title('Гистограмма распределени данных')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.show()

plt.scatter(df['column1'], df['column2']
plt.title('График зависимости между column1 и column2')
plt.xlabel('column1')
plt.ylabel('column2')
plt.show()

# научилась подключать библиотеки в питоне, 
устанавливать пандас и матплотлиб, 
читать сsv файл и извлекать значения из него