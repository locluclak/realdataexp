import pandas as pd 
import numpy as np 

def gasoline_fuel():
    df = pd.read_csv('gasoline_fuel.csv')

    response = "CO2 Emissions(g/km)"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

def other_fuel():
    df = pd.read_csv('other_fuel.csv')

    response = "CO2 Emissions(g/km)"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

if __name__ == "__main__":
    print(other_fuel()[1])