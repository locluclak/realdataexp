import pandas as pd 
import numpy as np 

def link():
    df = pd.read_csv('FbLink.csv')

    response = "Total Interactions"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

def photo():
    df = pd.read_csv('FbPhoto_dataset.csv')

    response = "Total Interactions"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

def status():
    df = pd.read_csv('FbStatus_dataset.csv')

    response = "Total Interactions"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

def video():
    df = pd.read_csv('FbVideo_dataset.csv')

    response = "Total Interactions"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    return X, y

if __name__ == "__main__":
    print(status()[0])