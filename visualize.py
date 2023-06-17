import pandas as pd
import mplfinance as mpf

df = pd.read_csv('D:\Matt\Data Science\EURUSD Scraping\csv\eurusd-1m-2023-05-24 02-24-02.csv')

df['Datetime'] = pd.to_datetime(df['Datetime'])
df.set_index('Datetime', inplace=True)

df_last_50 = df.tail(50)

mpf.plot(df_last_50, type='candle', style='yahoo', title='Gráfico de Velas Japonesas')