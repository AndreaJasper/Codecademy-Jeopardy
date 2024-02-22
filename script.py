import pandas as pd
pd.set_option('display.max_colwidth', -1)

# Loads data
jeopardy_data = pd.read_csv('jeopardy.csv')

# Renames misformatted columns
jeopardy_data = jeopardy_data.rename(columns={' Air Date': 'Air Date', ' Round': 'Round', ' Category': 'Category', ' Value': 'Value', ' Question': 'Question', ' Answer': 'Answer'})
print(jeopardy_data['Question'])

# filter by list of words
def filter_data(data, words):
  filter = lambda x: all(word in x for word in words)
  return data.loc[data['Question'].apply(filter)]

# checks filter
filtered = filter_data(jeopardy_data, ['King', 'England'])
print(filtered['Question'])
