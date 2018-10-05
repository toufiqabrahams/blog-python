import pandas 
start_date = '1/1/2017'
end_date = '31/12/2018'
list_of_dates = pandas.date_range(start=start_date, end=end_date)

df = pandas.DataFrame(list_of_dates)
df.columns = ['Date'] 

df['Year'] = df['Date'].dt.strftime('%Y').apply(pandas.to_numeric)
df['MonthNumber'] = df['Date'].dt.strftime('%m').apply(pandas.to_numeric)
df['Month'] = df['Date'].dt.strftime('%b')
df['FinMonth'] = df['Date'].dt.strftime('%b') 
df['WeekdayNumber'] = df['Date'].dt.strftime('%w').apply(pandas.to_numeric)
df['Weekday'] = df['Date'].dt.strftime('%a')
df['Day'] = df['Date'].dt.strftime('%d').apply(pandas.to_numeric)

fy = pandas.DataFrame({
    'MonthNumber': [1,2,3,4,5,6,7,8,9,10,11,12],
    'FinMonthNumber': [10,11,12,1,2,3,4,5,6,7,8,9],
    'Quarter': [1,1,1,2,2,2,3,3,3,4,4,4],
    'FinQuarter': [4,4,4,1,1,1,2,2,2,3,3,3],
    'FinYearDiff': [0,0,0,1,1,1,1,1,1,1,1,1],
    })

Calendar = pandas.merge(df, fy, on='MonthNumber', how='outer')
Calendar['FinYear'] = Calendar['Year'] + Calendar['FinYearDiff']
Calendar = Calendar.drop(['FinYearDiff'], axis=1)

Calendar.to_csv('D:\\data\\Calendar.csv', sep='\t', encoding='utf-8')
