import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', 24)

df = pd.read_csv(r"E:\DataAnalysis\NetflixProject\8. Netflix Dataset.csv")

# ---------------------------------------------------------------------------------------------------------------------#

# Show the top 5 rows of the dataset.
# print("Top 5 rows of the dataset")
# print(df.head())

# ---------------------------------------------------------------------------------------------------------------------#

# Show the bottom 5 rows of the dataset.
# print("Bottom 5 rows of the dataset")
# print(df.tail())

# ---------------------------------------------------------------------------------------------------------------------#

# Show the number of Rows x Columns of the dataset.
# print("Number of Rows x Columns")
# print(df.shape)

# ---------------------------------------------------------------------------------------------------------------------#

# Show the total number of values in the dataset.
# print("Total number of values in the dataset")
# print(df.size)

# ---------------------------------------------------------------------------------------------------------------------#

# Show the names of all columns.
# print("Columns names")
# print(df.columns)

# ---------------------------------------------------------------------------------------------------------------------#

# Show the datatypes of all columns.
# print("Columns Datatypes")
# print(df.dtypes)

# ---------------------------------------------------------------------------------------------------------------------#

# Show the data type of the variable that carries the dataset, number of total values, number of columns, Non-null
# values in each column, columns names, columns data types and memory usage.
# print("Dataset info")
# print(df.info())

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 1
# Check if there are duplicate values in the dataset and if there is any, remove them.

# Check if any of the rows is a duplicate (true or false list).
# print(df.duplicated())

# Get rows which have duplicates in the dataset.
# duplicatelist = [df.duplicated()]
#
# for i in range(7788):
#     if duplicatelist[0][i]:
#         print(df.iloc[i, :])
#         print("-------------------")

# Alternate way to get rows which have duplicates in the dataset.
# print(df[df.duplicated()]) # new dataframe including only the 'True' indices in the df.duplicated() list

# Remove Duplicates.
# nodup_df = df.copy()
# nodup_df.drop_duplicates(inplace=True)    # 'inplace=True' attribute is used to make the change permanent in the original dataframe not just in the displayed dataframe.

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 2
# Check if there are any mising values in the dataset and if there is any, show with heatmap.
# print(df.isna())    # true or false list

# print(df.isna().sum())  # Shows the number of missing values in each column

# Shows a heatmap representing the existence of missing values in the dataset
# sns.heatmap(df.isna())
# plt.show()

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 3
# Show all the rows where the title  name is 'House of Cards'
# 'str.contains()' will function the same as 'isin()' but only for string values

# var = df['Title'].isin(['House of Cards'])
# for i in range(len(var)):
#     if var[i]:
#         print(df.loc[[i]])

# alternate way

# print(df[df['Title'].isin(['House of Cards'])])

# ---------------------------------------------------------------------------------------------------------------------#


# TASK 4
# Show the number of occurences of each year in the dataframe by bargraph #

# new_df = df.copy()
# new_df['year'] = new_df.Release_Date.str[-4:]   # the datatype of the new 'year' column is string
#
# print(new_df.groupby(['year'])['year'].count())
#
# new_df.groupby(['year'])['year'].count().plot(kind='bar')
# plt.show()

# alternate way

# new_df = df.copy()
# new_df['date'] = pd.to_datetime(new_df['Release_Date'])
# print(new_df['date'].dt.year.value_counts())
# new_df['date'].dt.year.value_counts().plot(kind='bar')
# plt.show()

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 5
# Show the number of movies and tv shows in a bar graph #

# df.groupby(['Category'])['Category'].count().plot(kind='bar')
# plt.show()

# alternate way

# sns.countplot(data=df, x="Category")
# plt.show()


# ---------------------------------------------------------------------------------------------------------------------#

# TASK 6
# Show all the movies that were released in the year '2000'#


# new_df = df.copy()
# new_df['year'] = new_df.Release_Date.str[-4:]

# print(new_df[(new_df['Title'].isin(['2000'])) & (new_df['Category'] == 'Movie')])

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 7
# Show only the titles and directors of all the TV shows that were released in India#

# op_df = df[(df['Country'] == 'India' & (df['Category'] == 'TV Show')]

# print (op_df['Title'])

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 8
# Show Top 10 Directors with the most Movies or TV show on Netflix #

# print(df.groupby(['Director'])['Director'].count().head(10))

# alternate way

# print(df['Director'].value_counts().head(10))

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 9

# Show all the records were 'Category is movie and type is comedy' or 'Country is United kingdom' #

# op_df = df[(df['Category']=='Movie' & df['Type']=='Comedies']) | (df['Country '] == 'United Kingdom')]

# print(op_df)

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 10
# Show how many movies 'Tom Cruise' was cast in #

# Counter = 0

# for i in range(len(df)):
#     if not df.loc[i:'Cast'] .isnull():
#      if 'Tom Cruise' in df.loc[i:'Cast']:
#        counter += 1

# print(Counter)

# alternate way

# new_df = df.dropna()

# print(new_df[new_df['Cast'].str.contains('Tom Cruise ')]) 

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 11
# Show all the different ratings categories defined by Netflix#

# df['Rating'].nunique() #this shows the number of different ratings categories #

# df['Rating'].unique() #this shows all the different ratings categories #

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 12
# Show all the movies rated 'TV-14' in Canada #

# op_df = df[df['Rating'] == 'TV-14' & df['Category'] == 'Movie' & df['Country '] == 'Canada']

# print(len(op_df))

# alternate way

# print(op_df.shape)

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 13
# Show all the TV shows rated 'R' after 2018 #


# op_df = df.copy()
# op_df['date'] = pd.to_datetime(op_df['Release_Date'])
# op_df['year'] = op_df['date'].dt.year


# op_df = df[df['Rating'] == 'R' & df['Category'] == 'TV Show' & df['year'] > 2018]

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 14

# show the duration of the longest movie #

# movies_df = df[df['Title'] == 'Movie']

# movies_df['Minutes'] = movies_df['Duration'].str.split(' ', expand=True)[0]

# movies_df['Minutes'].max()

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 15

# Show the country which released the most tv shows

# tv_df = df[df['Category'] == 'TV Show']
# print(tv_df.groupby(['Country'])['Country'].count().head(1))

# alternate way (InPlace)

# print(df[df['Category'] == 'TV Show'].groupby(['Country'])['Country'].count().head(1))

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 16

# sort dataframe entries according to the year column #

# op_df = df.copy()
# op_df['date'] = pd.to_datetime(op_df['Release_Date'])
# op_df['year'] = op_df['date'].dt.year

# op_df.sort_values(by='Year', ascending=False)

# ---------------------------------------------------------------------------------------------------------------------#

# TASK 17

# Show all the drama movies and kids tv shows

# print(df[(df['Category'] == 'Movie'] & df['Type'] == 'Dramas') | (df['Category'] == 'TV Show' & df['Type'] == 'Kids\' Tv')]) 
