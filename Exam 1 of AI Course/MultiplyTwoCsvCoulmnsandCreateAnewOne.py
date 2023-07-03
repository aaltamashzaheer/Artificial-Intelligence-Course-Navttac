import pandas as pd
df = pd.read_csv('Iris.csv')
df.drop(['Id'], axis=1, inplace=True)
df["Total"]=df['SepalLengthCm'].multiply(df['SepalWidthCm'], axis=0)
print(df)