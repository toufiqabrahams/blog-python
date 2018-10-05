import pandas

with open('D:\\data\\ExchangeRateDetail.csv') as f:
    lines = [line.rstrip() for line in f]

lines = list(filter(None, lines))
lines = lines[3:]
lines = [t for t in lines if not t.startswith('The')]

df = pandas.DataFrame(lines)
df['Date'] = pandas.to_datetime(df[0].str.split(',').str.get(0))
df['Rate'] = df[0].str.split(',').str.get(1)
df = df.drop([0], axis=1)

