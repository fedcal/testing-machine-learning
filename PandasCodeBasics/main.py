import pandas as pd

def simpleOperations(df):
    print('Max Temperature: ' + str(df['Temperature'].max()))
    print(df['EST'][df['Events'] == 'Rain'])
    print(df['WindSpeedMPH'].mean())

def dataMunging(df):
    df.fillna(0)
    print(df['WindSpeedMPH'].mean())

def createDictionary():
    dictionaryData = {
        'day': ['1/11/2017','1/2/2017','1/3/2017'],
        'temp': [32,35,15],
        'wind': [5,15,25],
        'event': ['Sunny', 'Sunny','Rain']
    }
    return dictionaryData

def conditionalQueryDf(df):
    df[['day','temperature']][df.temperature==df.temperature.max()]

def spreadShape(df):
    print(df)
    rows, columns = df.shape
    print(rows)
    df.tail(1)
    df[2:5]  # esclusa l'ultima

def spreadExcel():
    df = pd.read_excel('Prova.xlsx', 'Sheet1',skiprows=1)
    print(df)
    dict = {
        'Date': ['2023-06-23','2023-06-24'],
        'Value': [19,20]
    }
    df2 = pd.DataFrame(dict)

    #generare un nuovo csv
    df2.to_excel("new_excel.xlsx",index=False)


if __name__ == '__main__':
    #df = pd.read_csv('nyc_weather.csv')
    #simpleOperations(df)
    #dataMunging(df)

    #df2 =pd.DataFrame(createDictionary())
    #spreadShape(df)

    #spreadExcel()


