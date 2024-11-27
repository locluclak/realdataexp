import pandas as pd 
import numpy as np 

def Walmart_sales_holiday():
    df = pd.read_csv('Walmart_sales_holiday.csv')

    response = "Weekly_Sales"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

def Walmart_sales_noholiday():
    df = pd.read_csv('Walmart_sales_noholiday.csv')

    response = "Weekly_Sales"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

if __name__ == "__main__":
    print(Walmart_sales_noholiday()[1])