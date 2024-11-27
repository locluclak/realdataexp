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
    rawData = pd.read_csv('Seoulbike.csv')

    no_holiday = rawData[rawData['Holiday'] == 'No Holiday']
    holiday = rawData[rawData['Holiday'] != 'No Holiday']
    
    no_holiday.to_csv('Seoulbike_no_holiday.csv', index=False)
    holiday.to_csv('Seoulbike_holiday.csv', index=False)

def cutfeature():
    df = pd.read_csv('Seoulbike_holiday.csv')

    columns_to_drop = ['Date', 'Seasons', 'Holiday', 'Functioning Day']
    
    new_df = df.drop(columns=columns_to_drop)
    new_df.to_csv('SeoulBikeHoliday_dataset.csv',index=False)

if __name__ == "__main__":
    cutfeature()
