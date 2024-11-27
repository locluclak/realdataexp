import pandas as pd 

def rm_nonascii():
    with open('SeoulBikeData.csv','r') as file:
        fout = open("Seoulbike.csv","w")

        while 1:
            char = file.read(1)
            if not char:
                break
            if 0 <= ord(char) <= 127:
                print(char,end='')
                fout.write(char)

def splitfile():
    rawData = pd.read_csv('heart_failure.csv')

    leq40 = rawData[rawData['age'] <= 50]
    g40 = rawData[rawData['age'] > 50]

    leq40.to_csv('Heart_failure_underequal50.csv', index=False)
    g40.to_csv("Heart_failure_larger50.csv", index=False)

def cutfeature():
    df = pd.read_csv('Heart_failure_larger50.csv')
    columns = ['time'] + [col for col in df.columns if col != 'time']
    df_reordered = df[columns]
    columns_to_drop = ['age', 'anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking', 'DEATH_EVENT']
    
    new_df = df_reordered.drop(columns=columns_to_drop)
    new_df.to_csv('Heart_failure_larger50_data.csv',index=False)
if __name__ == "__main__":
    # splitfile()
    cutfeature()
