import pandas as pd 
import numpy as np 

def holiday():
    df = pd.read_csv('SeoulBikeHoliday_dataset.csv')

    response = "Rented Bike Count"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

def no_holiday():
    df = pd.read_csv('SeoulBikeNoHoliday_dataset.csv')

    response = "Rented Bike Count"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

if __name__ == "__main__":
    print(holiday()[1])