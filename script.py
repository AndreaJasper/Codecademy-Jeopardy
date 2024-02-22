import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('jeopardy.csv')
print(df)