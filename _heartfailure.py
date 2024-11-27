import pandas as pd 
import numpy as np 
from random import sample
from sklearn.preprocessing import normalize

def undereq50(num = 20):
    df = pd.read_csv('dataset/Heart_failure_undereq50_data.csv')

    response = "time"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    y = np.random.choice(y.flatten(), size=num).reshape(-1, 1)
    X = X[np.random.choice(X.shape[0], num)]
    
    X = normalize(X, axis=0)
    y = normalize(y, axis=0)
    return X, y

def larger50(num = 100):
    df = pd.read_csv('dataset/Heart_failure_larger50_data.csv')

    response = "time"
    y = df[[response]].to_numpy()
    X = df[[col for col in df.columns if col != response]].to_numpy()
    y = np.random.choice(y.flatten(), size=num).reshape(-1, 1)
    X = X[np.random.choice(X.shape[0], num)]
    
    X = normalize(X, axis=0)
    y = normalize(y, axis=0)
    return X, y

if __name__ == "__main__":
    print(larger50()[1])