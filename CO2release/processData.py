import pandas as pd 



def splitfile():
    rawData = pd.read_csv('CO2_Emissions_Canada.csv')

    gasoline_fuel = rawData[rawData['Fuel Type'].isin(['X', 'Z'])]
    other_fuel = rawData[~rawData['Fuel Type'].isin(['X', 'Z'])]
    
    gasoline_fuel.to_csv('gasoline_fuel.csv', index=False)
    other_fuel.to_csv('other_fuel.csv', index=False)

def cutfeature():
    df = pd.read_csv('other_fuel.csv')

    columns_to_drop = ['Make', 'Model', 'Vehicle Class', 'Engine Size(L)', 'Fuel Type']
    
    new_df = df.drop(columns=columns_to_drop)
    new_df.to_csv('other_fuel.csv',index=False)

if __name__ == "__main__":
    cutfeature()
