# For data manipulation
import os
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import requests

class PythonTradingLab:

    def __init__(self):
        print("\nWelcome to PythonTradingLab! \n\nIf this is your first time using the app and you're not sure how it works, I recommend typing the following command in the terminal: \033[1m\033[4minfo()\033[0m \n\nOtherwise, may the force be with you!\n")

    def currentTime(self):
        currentTime = datetime.now()
        currentTime = currentTime.strftime("%Y-%m-%d %H-%M-%S")
        currentTime = currentTime.replace(":", "-").replace(".", "-").replace(" ", "-")
        return currentTime

    def download(self, symbol, period, interval):
        print(f'{symbol} loading...')

        try:
            symbolType = yf.Ticker(symbol).info['quoteType']
            print(f'{symbol} =', symbolType)
        except requests.exceptions.HTTPError as e:
            print(f'\nException: {str(e)} \n')
            return f'Error: Failed to retrieve quoteType from symbol \n'

        currentTime = self.currentTime()
        print(currentTime, '\n')

        directory = f'./transformedData/{symbolType}/{symbol}'
        if not os.path.exists(directory):
            os.makedirs(directory)
            os.chmod(directory, 0o777)
            permissions = oct(os.stat(directory).st_mode)[-3:]
        
        filePath = f'{directory}/{interval}.csv'
        if not os.path.exists(filePath):
            print('Downloading... ', filePath)
            
            df = yf.download(symbol, period=period, interval=interval)  
            df.rename_axis('Datetime', inplace=True)
            df.index = pd.to_datetime(df.index)

            df['Split'] = df['Close'] / df['Adj Close']
            del df['Adj Close']
            if symbolType == 'CURRENCY':
                del df['Volume']
            
            df.to_csv(filePath, index=True)
            print(f"File saved successfully: {filePath} \n")
        else:
            print("The file already exists. If you want to update the data, use \033[1m\033[4mupdate()\033[0m \n", filePath, '\n')

    def update(self, symbol, period, interval):
        print(f'{symbol} loading...')

        try:
            symbolType = yf.Ticker(symbol).info['quoteType']
            print(f'{symbol} =', symbolType)
        except KeyError:
            return f'Error: Failed to retrieve quoteType from symbol'
            
        currentTime = self.currentTime()
        print(currentTime, '\n')

        directory = f'./transformedData/{symbolType}/{symbol}'
        filePath = f'{directory}/{interval}.csv'

        if os.path.exists(filePath):
            print('Updating... ', filePath, '\n')
            df2 = pd.read_csv(filePath)
            
            df2.rename_axis('Datetime', inplace=True)
            df2.set_index('Datetime', inplace=True)
            df2.index = pd.to_datetime(df2.index)

            if not df2.empty:
                firstIndex = df2.index[0]
                lastIndex = df2.index[-1]
            else:
                print("\033[1m\033[4mError:\033[0m The DataFrame is empty.\n")
                os.remove(filePath)
                print(f"{filePath} was \033[1m\033[4mDELETED\033[0m\n")
                return f"{filePath} didn't exist. \n"
            print(f"The initial value updated in {filePath} was: {firstIndex}")
            print(f"The last value updated in {filePath} was: {lastIndex}")

            df = yf.download(symbol, period=period, interval=interval)
            df.index = pd.to_datetime(df.index)

            firstIndex = df.index[0]
            lastIndex = df.index[-1]
            print(f"The initial value in the file containing the newly acquired data is: {firstIndex}")
            print(f"The last value in the file containing the newly acquired data is: {lastIndex} \n")

            mask = df.index > lastIndex
            df = df[mask]
            df.loc[:, 'Split'] = df['Close'] / df['Adj Close']
            del df['Adj Close']
            if symbolType == 'CURRENCY':
                del df['Volume']

            with open(filePath, 'a') as f:
                df.to_csv(f, header=False, index=True, lineterminator='\n')
                print(f"File updated successfully: {filePath} \n")
        else:
            print("The file doesn't exist. If you want to create it, use \033[1m\033[4mdownload()\033[0m \n", filePath, '\n')