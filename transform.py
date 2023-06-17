import os
import pandas as pd

def rename_date_column(file_path):
    df = pd.read_csv(file_path)
    if 'Date' in df.columns:
        df.rename(columns={'Date': 'Datetime'}, inplace=True)
        df.to_csv(file_path, index=False)

rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\AAPL\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\AMZN\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\GOOGL\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\MSFT\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\TSLA\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\NVDA\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\JPM\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\JNJ\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\V\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\PFE\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\KO\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\EQUITY\MCD\1d.csv');

rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CURRENCY\EURUSD=X\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CURRENCY\GBPUSD=X\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CURRENCY\USDJPY=X\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CURRENCY\AUDUSD=X\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CURRENCY\USDCAD=X\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CURRENCY\NZDUSD=X\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CURRENCY\USDCHF=X\1d.csv');

rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\FUTURE\GC=F\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\FUTURE\SI=F\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\FUTURE\CL=F\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\FUTURE\BZ=F\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\FUTURE\NG=F\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\FUTURE\CT=F\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\FUTURE\ZW=F\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\FUTURE\ZS=F\1d.csv');


rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\INDEX\^GSPC\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\INDEX\^DJI\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\INDEX\^STOXX50E\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\INDEX\^GDAXI\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\INDEX\^IXIC\1d.csv');


rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CRYPTOCURRENCY\ADA-USD\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CRYPTOCURRENCY\LTC-USD\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CRYPTOCURRENCY\XRP-USD\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CRYPTOCURRENCY\BTC-USD\1d.csv');
rename_date_column(r'E:\Matt2\Data Science\PythonTradingLab\transformedData\CRYPTOCURRENCY\ETH-USD\1d.csv');