import pandas as pd
import datetime

pd.set_option('display.max_colwidth', None)

# Loads data
jeopardy_data = pd.read_csv('jeopardy.csv')

# Renames misformatted columns
jeopardy_data = jeopardy_data.rename(columns={' Air Date': 'Air Date', ' Round': 'Round', ' Category': 'Category', ' Value': 'Value', ' Question': 'Question', ' Answer': 'Answer'})
print(jeopardy_data['Air Date'])

# adds date time column insteald of Air Date string
jeopardy_data['date'] = jeopardy_data['Air Date'].apply(lambda x: pd.to_datetime(x))

# filter by list of words
def filter_data(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data['Question'].apply(filter)]

# checks filter
filtered = filter_data(jeopardy_data, ['king', 'england'])
# print(filtered['Question'])

# convert value to float
jeopardy_data['Float Value'] = jeopardy_data['Value'].apply(lambda x: float(x[1:].replace(',','')) if x != 'no value' else 0)

# finds average value of question
filtered = filter_data(jeopardy_data, ['King'])
# print(jeopardy_data['Float Value'].mean())

# number of unique answers
filtered = filter_data(jeopardy_data, ['king'])
# print(filtered['Question'].nunique())

# filter by date
filtered_by_computer = filter_data(jeopardy_data, ['computer'])
filtered_by_computer_90s = filtered_by_computer[(filtered_by_computer.date > datetime.datetime(1990, 1, 1)) & (filtered_by_computer.date < datetime.datetime(1999, 12, 31))]
filtered_by_computer_00s = filtered_by_computer[(filtered_by_computer.date > datetime.datetime(2000, 1, 1)) & (filtered_by_computer.date < datetime.datetime(2009, 12, 31))]
