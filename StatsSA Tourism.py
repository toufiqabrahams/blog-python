import pandas
df = pandas.read_excel('D:\\data\\excel\\tourism.xlsx')

df['H04a'] = df['H04'].str.split(' - ').str.get(0)
df['H04b'] = df['H04'].str.split(' - ').str.get(1)

df = df.drop(['H01','H02','H03','H04','H15','H25'], axis=1)

months = []
headers = []

for col in list(df):
    if 'MO' in col:
        months.append(col)
    else:
        headers.append(col)

df2 = pandas.melt(df, id_vars=headers, value_vars=months, var_name='Date')

df2 = df2[df2.H04b != 'Total industry']

df2['Date'] = pandas.to_datetime(df2['Date'].str[4:9] + '-' + df2['Date'].str[2:4] + '-01')

def noscale(row):
    if row['H17'] == 'Thousand':
        return row['value'] * 1000
    elif row['H17'] =='R million':
        return row['value'] * 1000000 
    elif row['H17'] =='Percentage':
        return row['value'] / 100
    else:
        return row['value']

df2['FullValue'] = df2.apply(noscale, axis=1)
df2 = df2.drop(['value','H17'], axis=1)

df2.columns = ['ValueType','Metric','Category','Date','Value']
