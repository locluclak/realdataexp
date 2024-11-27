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
    rawData = pd.read_csv('data_Facebook.csv')

    Link = rawData[rawData['Type'] == "Link"]
    Photo = rawData[rawData['Type'] == "Photo"]
    Status = rawData[rawData['Type'] == "Status"]
    Video = rawData[rawData['Type'] == "Video"]
    
    Link.to_csv('FbLink.csv', index=False)
    Photo.to_csv('FbPhoto.csv', index=False)
    Status.to_csv('FbStatus.csv', index=False)
    Video.to_csv('FbVideo.csv', index=False)

def cutfeature():
    df = pd.read_csv('FbVideo.csv')
    columns = ['Total Interactions'] + [col for col in df.columns if col != 'Total Interactions']
    df_reordered = df[columns]
    columns_to_drop = ['Type', 'Paid', 'Category']
    
    new_df = df_reordered.drop(columns=columns_to_drop)
    new_df.to_csv('FbVideo_dataset.csv',index=False)

if __name__ == "__main__":
    cutfeature()
