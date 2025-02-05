from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = {'Age': [20, 30, 40, 50, 60], 'Salary': [20000, 30000, 40000, 50000, 60000]}
df = pd.DataFrame(data)

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
print(df_scaled)
